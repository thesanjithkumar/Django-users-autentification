from django.urls import path
from basicapp import views
from django.conf import settings
from django.conf.urls.static import static
app_name = "basicapp"

urlpatterns = [
    path('register/', views.register, name = 'register'),
    path('user_login/', views.user_login, name = 'user_login'),
    path('special/', views.special, name = 'special'),
 ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
