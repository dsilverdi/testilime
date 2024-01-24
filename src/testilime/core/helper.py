from testilime.core.forms import (
    ImportTextTestimonialView,
    ImportTextTestimonialValidation,
    ImportUrlTestimonialView,
    ImportUrlTestimonialValidation,
)
from enum import Enum, auto

class ImportProviderIndex(Enum):
    TextTestimonial = 1
    Twitter = 2
    Linkedin = 3
    Shopee = 4
    Shopify = 5
    Whatsapp = 6

class TextTestimonialProvider(Enum):
    TextTestimonial = ImportProviderIndex.TextTestimonial
    Shopee = ImportProviderIndex.Shopee
    Shopify = ImportProviderIndex.Shopify
    Whatsapp = ImportProviderIndex.Whatsapp

class UrlTestimonialProvider(Enum):
    Twitter = ImportProviderIndex.Twitter
    Linkedin = ImportProviderIndex.Linkedin

class ImportProvider():
    def __init__(self, index, label, form):
        self.index = index
        self.label = label
        self.form = form        

def available_import_provider():
    textForm = ImportTextTestimonialView(False)
    available_provider = [
        ImportProvider(ImportProviderIndex.TextTestimonial.value, 'Text Testimonial', textForm),
        ImportProvider(ImportProviderIndex.Twitter.value, 'Twitter', ImportUrlTestimonialView('Tweet Post URL', 'https://twitter.com/ShouldHaveCat/status/1748776181107671544')),
        ImportProvider(ImportProviderIndex.Linkedin.value, 'LinkedIn', ImportUrlTestimonialView('Linkedin Post URL', 'https://www.linkedin.com/posts/y-combinator_the-best-consumer-companies-incorporate-both-activity-7153078082029948930-6ewA?utm_source=share&utm_medium=member_desktop')),
        ImportProvider(ImportProviderIndex.Shopee.value, 'Shopee', textForm),
        ImportProvider(ImportProviderIndex.Shopify.value, 'Shopify', textForm),
        ImportProvider(ImportProviderIndex.Whatsapp.value, 'Whatsapp', textForm),
    ]
    return available_provider

def get_provider_form_mapping():
    return {
        ImportProviderIndex.TextTestimonial.value: ImportTextTestimonialValidation,
        ImportProviderIndex.Twitter.value: ImportUrlTestimonialValidation,
        ImportProviderIndex.Shopee.value: ImportTextTestimonialValidation
    }

def IsTextTestimonial(provider_index):
    if isinstance(provider_index, int):
        provider_index = ImportProviderIndex(provider_index)
        return any(member.value == provider_index for member in TextTestimonialProvider)
    
    return False

def IsUrlTestimonial(provider_index):
    if isinstance(provider_index, int):
        provider_index = ImportProviderIndex(provider_index)
        return any(member.value == provider_index for member in UrlTestimonialProvider)
    
    return False
