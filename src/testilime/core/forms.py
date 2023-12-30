from django import forms

class CreateProjectForm(forms.Form):
    template_name = "core/forms/create_project_form.html"
    name = forms.CharField(
        max_length=50,
        label="Project name",
        error_messages={"required": "You need to enter your project's name."},
        widget=forms.TextInput(attrs={"placeholder": "Project Name"}),
    )
    header_title = forms.CharField(
        max_length=50,
        label="Header Title",
        error_messages={"required": "You need to enter Header Title."},
        widget=forms.TextInput(attrs={"placeholder": "Header Title"}),
    )
    message = forms.CharField(
        max_length=200,
        label="Message",
        widget=forms.TextInput(attrs={"placeholder": "Message"}),
    )
    enable_ratings = forms.BooleanField(
        label="Enable Ratings",
        required=False,
        initial=True,  # Default value, adjust as needed
    )