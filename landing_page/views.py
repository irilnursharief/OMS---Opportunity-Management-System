from django.shortcuts import render
from .models import Capability, Testimonial, Lead

# Create your views here.

def landing_page_view(request):
    capabilities = Capability.objects.all()
    testimonials = Testimonial.objects.all()
    leads = Lead.objects.all()

    context = {
        'capabilities': capabilities,
        'testimonials': testimonials,
        'page_title': 'Education & Enterprise Customer Portal',
        'hero_headline': 'Empowering Your Business with Apple Solutions',
        'hero_subheading': 'Transforming Enterprise and Education with Power Mac Center'
    }
    return render(request, 'landing_page/index.html', context)

