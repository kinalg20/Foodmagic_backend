from django.db import models
from category.models import Categories
# Create your models here.
def random_id_genrate():
    return random.randint(1,3910209312)
class Dishes(models.Model):
    dish_id=models.AutoField(primary_key=True,default=random_id_genrate)
    name=models.CharField(max_length=50)
    category_id=models.ForeignKey(Categories,on_delete=models.CASCADE,related_name='restaurant_address',null=True,blank=True)
    price=models.IntegerField(default=1)
    created=models.DateTimeField(auto_created=True)
    description=models.TextField(max_length=200)
    is_veg=models.BooleanField(default=False)
    is_available=models.BooleanField(default=False)