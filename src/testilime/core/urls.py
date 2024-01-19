from django.urls import path
from testilime.core import views

app_name = "testilime-core"

urlpatterns = [
    path("dashboard/", views.dashboard_view, name="dashboard"),
    path("space/<slug:slug>", views.project_detail_view, name="project-detail"),
    path("space/<slug:slug>/embeds-and-sharing", views.embeds_and_sharing_view, name="project-detail-embeds-and-sharing"),
    path("space/<slug:slug>/domain", views.domain_settings_view, name="project-detail-domain-settings"),
    path("space/<slug:slug>/space-settings", views.space_settings_view, name="project-detail-space-settings"),
    path("space/import-testimonial", views.create_and_import_testimonial)
]
