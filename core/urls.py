from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name="core"

urlpatterns = [
path('',views.Home.as_view(),name="home"),
path('item_detail/<int:id>/',views.item_detail,name="item_detail"),
path ('search/',views.search,name="search"),
path('create/',views.create,name="create"),
path('apartment/',views.apartment,name="apartment"),
path('apt_detail/',views.apt_detail,name="apt_detail"),
path('desh/',views.desh,name="desh"),
path('official',views.official,name="official"),
]