from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = "member"

urlpatterns = [
    path('login/', views.login , name ='login'),
    path('logout/', views.logout , name ='logout'),
    path('register/', views.register , name ='register'),
]