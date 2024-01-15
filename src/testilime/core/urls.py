from django.urls import path
from testilime.core import views

app_name = "testilime-core"

urlpatterns = [
    path("dashboard/", views.dashboard_view, name="dashboard"),
    path("space/<slug:slug>", views.project_detail_view, name="project-detail")
]
