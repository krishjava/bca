from django.contrib import admin
from django.urls import path,include
import core
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from users import views 
import random



urlpatterns = [
path('admin/', admin.site.urls),
path('',include('core.urls'),name="core"),
path('ratings/',include('star_ratings.urls')),
path('register/',views.register,name="register"),
path('login/',auth_views.LoginView.as_view(template_name="login.html"),name="login"),
path('logout/',auth_views.LogoutView.as_view(template_name="logout.html"),name="logout"),
path('password-reset/',auth_views.PasswordResetView.as_view(template_name="password_reset.html"),name="password_reset"),
path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name="password_reset_done.html"),name="password_reset_done"),
path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"),name="password_reset_confirm"), 
path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"),name="password_reset_complete"),
path('password-change/!#!#=132091839',auth_views.PasswordChangeView.as_view(template_name="password_change.html"),name="password_change"),
path('password-change-done',auth_views.PasswordChangeDoneView.as_view(template_name="password_change_done.html"),name="password_change_done"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)