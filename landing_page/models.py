from django.db import models

# Create your models here.

class Capability(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='capabilites/', blank=True, null=True)
    # link_url = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Capabilites" # Correct plural for admin display

    def __str__(self):
        return self.title
    
class Testimonial(models.Model):
    quote = models.TextField()
    customer_name = models.CharField(max_length=100)
    customer_title = models.CharField(max_length=100, blank=True, null=True)
    customer_company = models.CharField(max_length=100, blank=True, null=True)
    customer_logo = models.ImageField(upload_to='testimonials/logos/', blank=True, null=True)

    class Meta:
        ordering = ['customer_name']

    def __str__(self):
        return f'"{self.quote[:50]}..." - {self.customer_name}'
        
    

class Lead(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    newsletter_opt_in = models.BooleanField(default=False)
    submission_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email