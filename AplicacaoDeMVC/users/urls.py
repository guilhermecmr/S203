from django.urls import path
from . import views

urlpatterns = [
    path('show_users/',views.show_users, name='show_users')
]
