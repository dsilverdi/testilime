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
    def __init__(self, has_ratings, *args, **kwargs):
        super(ImportTextTestimonial, self).__init__(*args, **kwargs)
        self.has_ratings = has_ratings

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
        widget=forms.TextInput(attrs={"placeholder": "CEO of Stark Industries"}),
    )
    testimonial = forms.CharField(
        max_length=240,
        label="Testimonial",
        widget=forms.TextInput(attrs={"placeholder": "Testimonial"}),
    )

class ImportUrlTestimonial(forms.Form):
    def __init__(self, title_param, placeholder_param, *args, **kwargs):
        super(ImportUrlTestimonial, self).__init__(*args, **kwargs)
        self.fields['url'] = forms.URLField(label=title_param, widget=forms.TextInput(attrs={'placeholder': placeholder_param}))
    
    template_name = "core/forms/import_url_testimonial_form.html"
