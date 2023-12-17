from django.conf import settings
# from google.auth.transport import requests
# from google.oauth2 import id_token
import requests
import json


# def validate_google_id_token(request):
#     csrf_token_cookie = request.COOKIES.get("g_csrf_token", None)
#     if not csrf_token_cookie:
#         raise Exception("No CSRF token in Cookie.")

#     csrf_token_body = request.POST.get("g_csrf_token", None)
#     if not csrf_token_body:
#         raise Exception("No CSRF token in post body.")
#     if csrf_token_cookie != csrf_token_body:
#         raise Exception("Failed to verify double submit cookie.")

#     id_token_body = request.POST.get("credential", None)
#     print("got id_token_body ", id_token_body)
#     print("\nOAUTH CLIENT ID ", settings.GOOGLE_OAUTH_CLIENT_ID)
#     try:
#         idinfo = id_token.verify_oauth2_token(
#             id_token_body, requests.Request(), settings.GOOGLE_OAUTH_CLIENT_ID
#         )
#         print("\n got idinfo >>>>> ", idinfo)
#     except ValueError:
#         raise Exception("Invalid token.")

#     return idinfo

client = settings.GOOGLE_OAUTH_CLIENT

def get_google_provider_cfg():
    return requests.get(settings.GOOGLE_DISCOVERY_URL).json()

def validate_google_id_token(request):
    code = request.GET.get("code")
    if not code:
        raise Exception("No Data Code.")

    google_provider_cfg = get_google_provider_cfg()
    token_endpoint = google_provider_cfg["token_endpoint"]

    token_url, headers, body = client.prepare_token_request(
        token_endpoint,
        authorization_response=request.get_full_path(),
        redirect_url=request.build_absolute_uri(settings.GOOGLE_OAUTH2_REDIRECT_URI),
        code=code
    )

    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(settings.GOOGLE_OAUTH_CLIENT_ID, settings.GOOGLE_OAUTH_CLIENT_SECRET),
    )

    client.parse_request_body_response(json.dumps(token_response.json()))
    userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)


    if userinfo_response.json().get("email_verified"):
        return userinfo_response.json()
    else:
        raise Exception("User email not available or not verified by Google.")

def google_authorization_url(request):
    google_provider_cfg = get_google_provider_cfg()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]
    redirect_uri = request.build_absolute_uri(settings.GOOGLE_OAUTH2_REDIRECT_URI)

    # Construct the authorization URL
    authorization_url = client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri=redirect_uri,
        scope=['openid', 'profile', 'email'],
    )

    return authorization_url