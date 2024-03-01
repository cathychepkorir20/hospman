from django.db import models


# Create your models here.
class Users(models.Model):
    fullname = models.CharField(max_length=200)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    age = models.IntegerField(default=18)
    year_of_birth = models.DateField(null=True)

    def __str__(self):
        return self.fullname


class Products(models.Model):
    product_name = models.CharField(max_length=200)
    product_price = models.CharField(max_length=20)
    product_quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.product_name


class Members(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.username


class Contacts(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name


class Message(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name