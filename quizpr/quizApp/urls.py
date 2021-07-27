from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='index'),
    path('leader/', leader, name='quizadmin'),
]
