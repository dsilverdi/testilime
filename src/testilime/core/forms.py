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
    template_name = "core/forms/import_text_testimonial_form.html"
    name = forms.CharField(
        max_length=50,
        label="Name",
        error_messages={"required": "Name is required"},
        widget=forms.TextInput(attrs={"placeholder": "Tony Stark"}),
    )
    tagline = forms.CharField(
        max_length=50,
        label="Tagline",
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "CEO of Stark Industries"}),
    )
    testimonial = forms.CharField(
        max_length=240,
        label="Testimonial",
        error_messages={"required": "Testiminial field is required"},
        widget=forms.TextInput(attrs={"placeholder": "Testimonial"}),
    )
    provider_index = forms.IntegerField()

class ImportTextTestimonialView(ImportTextTestimonial):
    def __init__(self, has_ratings, *args, **kwargs):
        super(ImportTextTestimonialView, self).__init__(*args, **kwargs)
        self.has_ratings = has_ratings

class ImportTextTestimonialValidation(ImportTextTestimonial):
    pass

class ImportUrlTestimonial(forms.Form):
    
    template_name = "core/forms/import_url_testimonial_form.html"
    url = forms.URLField(error_messages={"required": "Name is required"},)
    provider_index = forms.IntegerField()

class ImportUrlTestimonialView(ImportUrlTestimonial):
    def __init__(self, title_param, placeholder_param, *args, **kwargs):
        super(ImportUrlTestimonialView, self).__init__(*args, **kwargs)
        self.title = title_param
        self.placeholder = placeholder_param

class ImportUrlTestimonialValidation(ImportUrlTestimonial):
    pass