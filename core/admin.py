from django.contrib import admin
from .models import Uploaded,Item,Comment,Property_Buy,Apartment,Apartment_All,User_Profile,Property_Rent

admin.site.register(Item)
admin.site.register(Comment)
admin.site.register(Property_Buy)
admin.site.register(Property_Rent)
admin.site.register(Apartment)
admin.site.register(Apartment_All)
admin.site.register(User_Profile)
admin.site.register(Uploaded)
