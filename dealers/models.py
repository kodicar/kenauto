from django.db import models

# Create your models here.

class Dealers(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50, unique=True)
    is_mvp = models.BooleanField(default=False)
    deal_date = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = 'Dealers'
