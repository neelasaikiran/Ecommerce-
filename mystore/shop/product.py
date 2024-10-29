from django.db import models
from .category import Category

class Product(models.Model):
    
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category , on_delete=models.CASCADE , default=1 )
    image = models.ImageField(upload_to='images')
    desc = models.TextField()
    price = models.IntegerField()
    
    def __str__(self):
        return self.name 
    
    # static method
    
    @staticmethod
    def get_category_id(get_id):
        if get_id:
            return Product.objects.filter(category=get_id)
        else:
            return Product.objects.all()
    