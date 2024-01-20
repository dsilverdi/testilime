from django import forms

class CreateProjectForm(forms.Form):
    template_name = "core/forms/create_project_form.html"
    name = forms.CharField(
        max_length=50,
        label="Project name",
        error_messages={"required": "You need to enter your project's name."},
        widget=forms.TextInput(attrs={"placeholder": "Project Name"}),
    )
    slug = forms.CharField(
        max_length=50,
        label="project slug",
        error_messages={"required": "You need to enter project slug."},
        widget=forms.TextInput(attrs={"placeholder": "project slug"}),
    )
    description = forms.CharField(
        max_length=200,
        label="Description",
        widget=forms.TextInput(attrs={"placeholder": "Description"}),
    )

class ImportTextTestimonial(forms.Form):
    name = forms.CharField(
        max_length=50,
        label="Name",
        error_messages={"required": "Name is required"},
        widget=forms.TextInput(attrs={"placeholder": "Name"}),
    )
    tagline = forms.CharField(
        max_length=50,
        label="Tagline",
        widget=forms.TextInput(attrs={"placeholder": "Tagline"}),
    )
    testimonial = forms.CharField(
        max_length=240,
        label="Testimonial",
        widget=forms.TextInput(attrs={"placeholder": "Testimonial"}),
    )