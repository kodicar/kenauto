from django.db import models

# Create your models here.

class Contact(models.Model):
    listing = models.CharField(max_length=200)
    listing_id = models.IntegerField()
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(auto_now=True, blank=True)
    user_id = models.IntegerField(blank=True)

    class Meta:
        verbose_name_plural = 'Inquiries'

    def __str__(self) -> str:
        return self.name

