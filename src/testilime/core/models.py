from django.db import models

class Projects(models.Model):
    user = models.ForeignKey(
        "testilime_auth.User",
        related_name="projects",
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=50)
    header_title = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.name
    
class TestimonialItem(models.Model):
    project = models.ForeignKey(

    )
    