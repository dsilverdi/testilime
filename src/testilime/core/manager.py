from testilime.core.helper import IsTextTestimonial, IsUrlTestimonial
from testilime.core.models import Projects, TestimonialItem
from django.shortcuts import get_object_or_404

from datetime import datetime

# TODO: add success alert on success creation in html template
def process_testimonial_creation(data, slug):
    provider_index = data['provider_index']
    project = get_object_or_404(Projects, slug=slug)

    if IsTextTestimonial(provider_index):
        data = {
            'project': project,
            'author_name': data['name'],
            'author_tagline': data['tagline'],
            'has_ratings': False, # temporary need to solve if has ratings
            'ratings': 1, # temporary need to solve if has ratings
            'testimonial': data['testimonial'],
            'created_at': datetime.now(),
        }
        testimonial_item = TestimonialItem(**data)
        testimonial_item.save()
