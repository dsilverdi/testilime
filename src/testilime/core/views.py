from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_http_methods, require_POST
from testilime.core.forms import CreateProjectForm
from testilime.core.models import Projects

@never_cache
@require_http_methods(["GET", "POST"])
@login_required
def dashboard_view(request):
    context = {}

    form = CreateProjectForm(request.POST or None)
    context["form"] = form

    if request.method == "POST":
        if form.is_valid():
            try:
                name = form.cleaned_data["name"]
                header_title = form.cleaned_data["header_title"]
                message = form.cleaned_data["message"]
                enable_ratings = form.cleaned_data["enable_ratings"]

                # Create Projects instance and save it to the database
                _ = Projects.objects.create(
                    user=request.user,
                    name=name,
                    header_title=header_title,
                    message=message,
                    enable_ratings=enable_ratings,
                )

            except Exception as e:
                form.add_error(None, "Error When Creating Project")

    projects = Projects.objects.filter(user=request.user)
    context["projects"] = projects

    print("GOT PROJECTS WITH SIZE =>>> ", len(projects))

    return render(request, "core/pages/dashboard.html", context)

@never_cache
@require_GET
@login_required
def project_detail_view(request, slug):
    return