from django.db import models

# Create your models here.

class TimeStampedModel(models.Model):
    """ Time Stamped Model"""

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class AbstractItem(TimeStampedModel):
    """Abstract Item"""

    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True





class Category(models.Model):
    categories = (
        ('Car', 'Car'),
        ('classics', 'classics'),
        ('convertibles', 'convertibles'),
        ('Exotic & Luxury', 'Exotic & Luxury'),
        ('Minivans', 'Minivans'),
        ('Sports', 'Sports'),
        ('SUV', 'SUV'),
        ('Trucks', 'Trucks'),
        ('Vans', 'Vans')
    )
    cat_name = models.CharField(max_length=100, choices=categories, default='Car')
    cat_image = models.ImageField(upload_to = 'categories')

    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.cat_name

class Cars(models.Model):

    makes = (
        ('Tesla', 'Tesla'),
        ('Lamborghini', 'Lamborghini'),
        ('Jeep', 'Jeep'),
        ('Rolls Royce', 'Rolls Royce'),
        ('Mercedes Benz', 'Mercedes Benz'),
        ('Ferrari', 'Ferrari'),
        ('Maserati', 'Maserati'),
        ('Porsche', 'Porsche'),
        ('BMW', 'Subaru'),
        ('Acura', 'Acura'),
        ('Dodge', 'Dodge'),
        ('Toyota', 'Toyota'),
        ('Hyundai', 'Hyundai'),
        ('Apple', 'Apple'),
        ('Subaru', 'Subaru'),
        ('Bugatti', 'Bugatti'),

    )

    counties = (


        ('Mombasa','Mombasa'),
        ('Kwale','Kwale'),
        ('Kilifi','Kilifi'),
        ('Tana River','Tana River'),
        ('Lamu','Lamu'),
        ('Taita-Taveta', 'Taita-Taveta'),
        ('Garissa','Garissa'),
        ('Wajir','Wajir'),
        ('Mandera','Mandera'),
        ('Marsabit', 'Marsabit'),
        ('Isiolo', 'Isiolo'),
        ('Meru', 'Meru'),
        ('Tharaka-Nithi', 'Tharaka-Nithi'),
        ('Embu', 'Embu'),
        ('Kitui','Kitui'),
        ('Machakos', 'Machakos'),
        ('Makueni', 'Makueni'),
        ('Nyandarua', 'Nyandarua'),
        ('Nyeri', 'Nyeri'),
        ('Kirinyaga', 'Kirinyaga'),
        ('Murang', 'Murang'),
        ('Kiambu', 'Kiambu'),
        ('Turkana', 'Turkana'),
        ('West Pokot', 'West Pokot'),
        ('Samburu', 'Samburu'),
        ('Trans Nzoia','Trans Nzoia'),
        ('Uasin Gishu', 'Uasin Gishu'),
        ('Elgeyo-Marakwet', 'Elgeyo-Marakwet'),
        ('Nandi','Nandi'),
        ('Baringo', 'Baringo'),
        ('Laikipia', 'Laikipia'),
        ('Nakuru', 'Nakuru'),
        ('Narok', 'Narok'),
        ('Kajiado', 'Kajiado'),
        ('Kericho', 'Kericho'),
        ('Bomet', 'Bomet'),
        ('Kakamega','Kakamega'),
        ('Vihiga', 'Vihiga'),
        ('Bungoma', 'Bungoma'),
        ('Busia', 'Busia'),
        ('Siaya', 'Siaya'),
        ('Kisumu', 'Kisumu'),
        ('Homa Bay','Homa Bay'),
        ('Migori', 'Migori'),
        ('Kisii', 'Kisii'),
        ('Nyamira', 'Nyamira'),
        ('Nairobi', 'Nairobi'),
    )
    street_address = models.CharField(max_length=200)
    county = models.CharField(max_length=200, choices=counties, default='Nairobi')
    town = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100)

    # car information
    year = models.IntegerField()
    make = models.CharField(max_length=100, default='Tesla', choices=makes)
    model = models.CharField(max_length=100)
    # odometer = models.CharField(max_length=300)
    car_category = models.ForeignKey(Category, on_delete= models.CASCADE)
    colour = models.CharField(max_length=50)
    mpg = models.CharField(max_length=50)
    seats = models.IntegerField()
    doors = models.IntegerField()

    Transmissions= (
        ('Automatic', 'Automatic'),
        ('Manual', 'Manual'),
    )
    transmission = models.CharField(max_length=200, choices=Transmissions)
    car_details = models.TextField()
    description = models.TextField()
    price = models.IntegerField(default=100000)

    # features 
    # cretae single textfields to handle description
    usb_charger = models.BooleanField(default=False)
    gps = models.BooleanField()
    automatic = models.BooleanField()
    sunroof = models.BooleanField()
    apple_car_play = models.BooleanField()
    all_wheel_drive = models.BooleanField()
    bluetooth = models.BooleanField()
    audio_input = models.BooleanField()
    convertible = models.BooleanField()
    child_seat = models.BooleanField()
    longterm_car = models.BooleanField()
    bike_rack = models.BooleanField()
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now=True)
    # owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.make} - {self.model} - {self.year}'

    
    # def get_absolute_url(self):
    #     return reverse("model_detail", kwargs={"pk": self.pk})
    
    def save(self, *args, **kwargs):
        self.town = str.title(self.town)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Cars"
        ordering = ['-pk']
