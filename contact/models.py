from django.db import models

# Create your models here.

class Contact(models.Model):
    car = models.CharField(max_length=200)
    car_id = models.IntegerField()
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(auto_now=True, blank=True)
    user_id = models.IntegerField(blank=True)

    class Meta:
        verbose_name_plural = 'Contacts'

    def __str__(self) -> str:
        return self.name

