from django.urls import path
from .views import *

urlpatterns = [
    path('check/<str:id>', checkUser),
    path('detail/<str:id>', getUserDetails),
    path('repos/<str:id>', getUserReposDetails),
]
