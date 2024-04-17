from django.db import models

class User(models.Model):
    name = models.CharField(max_length=250)
    surname = models.CharField(max_length=250)
    birthday = models.DateField(null=True, blank=True)
    email = models.EmailField(max_length=250)
    phone_number = models.CharField(max_length=250)
    password = models.CharField(max_length=250)

    def age(self):
        import datetime
        return int((datetime.datetime.now() - self.birthday).days / 365.25  )
    age = property(age)    

    def __str__(self):
        return self.name

class University(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='university/%Y/%m/%d', blank=True)
    location = models.CharField(max_length=250)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    documents = models.CharField(max_length=250)
    grants = models.CharField(max_length=250)
    dedline = models.CharField(max_length=250)

    def __str__(self):
        return self.name
