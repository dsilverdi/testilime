import uuid
from django.db import models

class Projects(models.Model):
    user = models.ForeignKey(
        "testilime_auth.User",
        related_name="projects",
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50, unique=True, default=uuid.uuid4, editable=False)
    description = models.TextField()

    def __str__(self):
        return self.name

class TestimonialCollectionPageConfig(models.Model):
    project = models.OneToOneField(
        Projects, 
        on_delete=models.CASCADE
    )
    header_title = models.CharField(max_length=50)
    message = models.TextField()
    enable_ratings = models.BooleanField(default=True)
    is_active = models.BooleanField()

    def __str__(self):
        return f"{self.project.name} - {self.header_title}"
 
class TestimonialItem(models.Model):
    project = models.ForeignKey(
        Projects,
        related_name="testimonial_item",
        on_delete=models.CASCADE
    )
    author_name = models.CharField(max_length=255)
    author_position = models.CharField(max_length=255, blank=True, null=True)
    has_ratings = models.BooleanField(default=True)  # New field for ratings configuration
    ratings = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
