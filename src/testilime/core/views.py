from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_http_methods, require_POST
from testilime.core.forms import CreateProjectForm

@never_cache
@require_GET
def dashboard_view(request):
    context = {}

    form = CreateProjectForm(request.POST or None)
    context["form"] = form

    return render(request, "core/pages/dashboard.html", context)