from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=255)
    class Meta: #This updates the table name displayed in django administration page
        ordering =('name',) #order the fields by name,  comma is needed at the end because it is an iterable
        verbose_name_plural='Categories'
    def __str__(self):
        return self.name #display category name rather than object
    
class Item(models.Model):
    category=models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    description=models.TextField(blank=True, null=True)
    price=models.FloatField()
    image=models.ImageField(upload_to='item_images', blank=True, null=True) #upload_to is used to specify the folder where the image will be uploaded to
    is_sold=models.BooleanField(default=False)
    #link createdby to user table, related_name is used to get all the items created by the tied user, on_delete is used to delete all the items created by a user when the user is deleted
    created_by=models.ForeignKey(User, related_name='items', on_delete=models.CASCADE) 
    created_at=models.DateTimeField(auto_now_add=True) #auto_now_add is used to add the current date and time when the item is created
    def __str__(self):
        return self.name