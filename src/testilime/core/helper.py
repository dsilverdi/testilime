from testilime.core.forms import ImportTextTestimonial
class ImportProvider():
    def __init__(self, index, label, form):
        self.index = index
        self.label = label
        self.form = form        

def available_import_provider(request):
    textForm = ImportTextTestimonial(request.POST or None)
    available_provider = [
        ImportProvider(1, 'Text Testimonial', textForm),
        ImportProvider(2, "Shopee", textForm),
        ImportProvider(3, "Shopify", textForm),
        ImportProvider(4, "Whatsapp", textForm),
    ]
    return available_provider
