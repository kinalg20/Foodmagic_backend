from django.db import models
# Create your models here.
class Categories(models.Model):
    Category_id=models.IntegerField(default=1)
    name=models.CharField(max_length=50)
