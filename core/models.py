from django.db import models
from django.shortcuts import reverse
from django.conf import settings

STATUS_CHOICE=(
    ("R","Rent"),
    ("S","Sale"),
)

class Item(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS_CHOICE,max_length=2)
    image = models.ImageField(upload_to='media')
    price = models.FloatField()
    squarefoot = models.FloatField(default=100.00)
    city = models.CharField(max_length=100)
    town_address = models.CharField(max_length=100)
    bedroom = models.IntegerField(default=2)
    bedroom_img = models.ImageField(upload_to='media/bedroom_img')
    kitchen_img = models.ImageField(upload_to='media/kichen_img')
    kitchen = models.IntegerField(default=1)
    let_bath = models.IntegerField(default=2)
    swimming_pool = models.ImageField(upload_to='media/swim_pool')
    



class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    post_id = models.ForeignKey(Item ,on_delete=models.CASCADE)
    message = models.TextField('Message')
    comment_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.message

class Rent(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE )
    rent_id=models.ForeignKey(Item,on_delete=models.CASCADE,default=False)
    voter_id=models.CharField(max_length=10)
    addhar_no=models.CharField(max_length=12)
    profession=models.CharField(max_length=50)
    moblie=models.CharField(max_length=10,default=False)
    error=models.CharField(max_length=100,default="already on rent")
