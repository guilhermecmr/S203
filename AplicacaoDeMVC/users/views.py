from django.shortcuts import render
from .models import User

# Create your views here.
def show_users(request):
    users = User.objects.all()
    return render(request, 'users/show_users.html', {'users':users})