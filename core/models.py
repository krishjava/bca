from django.db import models
from django.shortcuts import reverse
from django.conf import settings
from django.contrib.auth.models import User


STATUS_CHOICE=(
    ("Rent","Rent"),
    ("Sale","Sale"),
    ("O","Rented"),
)

class Item(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS_CHOICE,max_length=8)
    image = models.ImageField(upload_to='media')
    price = models.FloatField()
    squarefoot = models.FloatField(default=100.00)
    city = models.CharField(max_length=100)
    town_address = models.CharField(max_length=100)
    bedroom = models.IntegerField(default=2)
    bedroom_img = models.ImageField(upload_to='media/bedroom_img')
    kitchen_img = models.ImageField(upload_to='media/kichen_img')
    # kitchen = models.IntegerField(default=1)
    let_bath = models.IntegerField(default=2)
    swimming_pool = models.ImageField(upload_to='media/swim_pool',default='/media/default/item_default.png')
    property_structure=models.ImageField(upload_to='media/proerty_structure',default="default.png")
    property_type=models.CharField(max_length=30,default="1BHK")


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    post_id = models.ForeignKey(Item ,on_delete=models.CASCADE)
    message = models.TextField('Message')
    comment_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.message

STATUS_BUY_CHOICE=(
    ("Sale","Sale"),
    ("Buy","Buy"),
)
class Property_Buy(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE )
    email=models.EmailField(max_length=256,default=False)
    moblie=models.CharField(max_length=10,default=False)
    status=models.CharField(max_length=10,choices=STATUS_BUY_CHOICE,default="Sale")
    property_image=models.ImageField(upload_to='media/user_booked',default='default.png')
    price=models.IntegerField()
    property_type=models.CharField(max_length=19,default="1BHK")
    property_id=models.IntegerField(primary_key=True,default=1)
    on_buy = models.BooleanField(default=False)

STATUS_RENT_CHOICE=(
    ("Rent","Rent"),
    ("Rented","Rented"),
)
class Property_Rent(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE )
    mobile=models.IntegerField()
    email=models.EmailField(max_length=256)
    addhar_id=models.IntegerField()
    residence_address=models.CharField(max_length=256,default="kuch nhi")
    profession=models.CharField(max_length=20,default="Student")
    voter_id=models.IntegerField()
    image=models.ImageField(upload_to='media/rent',default='default.png')
    status=models.CharField(choices=STATUS_RENT_CHOICE,default="Rent",max_length=10)
    price=models.CharField(max_length=100000000,default="100")
    property_type=models.CharField(max_length=10,default="1BHK")
    property_id=models.IntegerField(primary_key=True,default=1)
    on_rent = models.BooleanField(default=False)

class Apartment(models.Model):
    title = models.CharField(max_length=30)
    city = models.CharField(max_length=90)
    local_address = models.CharField(max_length=200)
    price_range = models.CharField(max_length=9)

class Apartment_All(models.Model):
    image = models.ImageField(upload_to='media')
    title = models.CharField(max_length=30)
    city = models.CharField(max_length=90)
    local_address = models.CharField(max_length=200)
    price_range = models.CharField(max_length=9)

class User_Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_image = models.ImageField(default='default.',upload_to='media/Profile_image')

    def __str__(self):
        return f'{self.user.username} User_Profile'

class Uploaded(models.Model):
    image=models.ImageField(upload_to='media/test',default='/media/item_default.png')
    status=models.CharField(max_length=10)