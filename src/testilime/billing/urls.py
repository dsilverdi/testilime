from django.urls import path
from testilime.billing import views

app_name = "testilime-billing"

urlpatterns = [
    path("settings/billing/", views.billing_settings_view, name="billing-settings"),
    path(
        "billing/subscribe-checkout/create/",
        views.create_subscribe_checkout_view,
        name="create-subscribe-checkout",
    ),
    path(
        "billing/cancel-subscription/",
        views.cancel_subscription_view,
        name="cancel-subscription",
    ),
    path(
        "billing/reactivate-subscription/",
        views.reactivate_subscription_view,
        name="reactivate-subscription",
    ),
    path("billing/stripe/webhook/", views.stripe_webhook_view, name="stripe-webhook"),
]
