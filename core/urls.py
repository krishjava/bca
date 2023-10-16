from django.urls import path
from . import views

app_name="core"

urlpatterns = [
path('',views.Home.as_view(),name="home"),
path('item_detail/<int:id>/',views.item_detail,name="item_detail"),
path ('search/',views.search,name="search"),
path('create/',views.create,name="create"),
path('desh/<int:id>/',views.deshboard,name="deshboard"),
path('go/<int:id>/',views.check_rent,name="go")

]