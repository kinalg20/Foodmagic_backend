from django.db import models
from Dishes.models import Dishes
# Create your models here.
class DishRating(models.Model):
    dish_id=models.OneToOneField(Dishes,primary_key=True,on_delete=models.CASCADE)
    rating=models.IntegerField()
    reviews=models.TextField(max_length=200)
