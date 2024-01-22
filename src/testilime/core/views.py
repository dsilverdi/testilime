from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404,redirect, render
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_http_methods, require_POST
from testilime.core.forms import CreateProjectForm
from testilime.core.models import Projects
from testilime.core.helper import available_import_provider, get_provider_form_mapping

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
                slug = form.cleaned_data["slug"]
                description = form.cleaned_data["description"]

                # Create Projects instance and save it to the database
                _ = Projects.objects.create(
                    user=request.user,
                    name=name,
                    slug=slug,
                    description=description,
                )

                return redirect("testilime-core:dashboard")

            except IntegrityError as e:
                if 'unique constraint' in str(e):
                    form.add_error('slug', 'This slug is already in use. Please choose a different one.')
                else:
                    form.add_error(None, 'Error When Creating Project')

    projects = Projects.objects.filter(user=request.user)
    context["projects"] = projects

    return render(request, "core/pages/dashboard.html", context)

@never_cache
@require_GET
@login_required
def project_detail_view(request, slug):
    project = get_object_or_404(Projects, slug=slug, user=request.user)

    context = {
        'project': project,
        # Add any additional context variables you need
    }

    return render(request, 'core/pages/space_testimonial_page.html', context)

@never_cache
@require_GET
@login_required
def embeds_and_sharing_view(request, slug):
    project = get_object_or_404(Projects, slug=slug, user=request.user)

    context = {
        'project': project,
        # Add any additional context variables you need
    }

    return render(request, 'core/pages/space_embeds_and_sharing.html', context)

@never_cache
@require_GET
@login_required
def domain_settings_view(request, slug):
    project = get_object_or_404(Projects, slug=slug, user=request.user)

    context = {
        'project': project,
        # Add any additional context variables you need
    }

    return render(request, 'core/pages/space_domain_settings.html', context)

@never_cache
@require_GET
@login_required
def space_settings_view(request, slug):
    project = get_object_or_404(Projects, slug=slug, user=request.user)

    context = {
        'project': project,
        # Add any additional context variables you need
    }

    return render(request, 'core/pages/space_settings_page.html', context)

@require_http_methods(["GET", "POST"])
@login_required
def create_and_import_testimonial(request, slug):
    if request.method == "POST":
        provider_index = request.POST.get('provider_index')
        form_data = request.POST.dict()

        # Assuming you have a dictionary to map provider indices to their respective form classes
        provider_form_mapping = get_provider_form_mapping()
        form_class = provider_form_mapping.get(provider_index)

        if form_class:
            form = form_class(form_data)
            if form.is_valid():
                print(form.cleaned_data)
                data = {'message': 'Form submitted successfully!'}
                return JsonResponse(data)
            else:
                # If the form is not valid, return an error message
                errors = {'error': 'Invalid form submission', 'errors': form.errors}
                return JsonResponse(errors, status=400)
        else:
            # Handle the case when the provider_index is not valid
            return JsonResponse({'error': 'Invalid provider index'}, status=400)

    else:
        providers = available_import_provider()
        context = {
            'slug': slug,
            'providers': providers
        }
        return render(request, 'core/pages/import.html', context)