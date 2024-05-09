from django.urls import path, include
from . import views

urlpatterns = [
 path('', views.home, name="Home"),
 path('/logout', views.exit, name="exit"), 
 path('accounts/', include('django.contrib.auth.urls')),
]