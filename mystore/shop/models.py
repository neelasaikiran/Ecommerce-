from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=50)
    password = models.CharField(max_length=200)
    
    # static method
    def email_exists(email):
        return Customer.objects.filter(email=email).exists()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
# To check if the email exists and fetch the user


def get_email(email):
    try:
        return Customer.objects.get(email=email)  
    except Customer.DoesNotExist:
        return None  
