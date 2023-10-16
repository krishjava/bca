
from django.contrib import admin
from django.urls import path,include
import core
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('',include('core.urls'),name="core"),
    path('ratings/',include('star_ratings.urls'))

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
