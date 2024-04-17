from django.shortcuts import render
from .models import Users

# Create your views here.
def show_users(request):  
    
    novo_user = Users.objects.create(username="GuiCotta", email="guilhermecottamr@hotmail.com", password="123456", first_name="Guilherme", last_name="Cotta", is_staff=False, is_superuser=False)
    novo_user2 = Users.objects.create(username="CarlinhosDonato", email="carlosdonato@gmail.com", password="654321", first_name="Carlos", last_name="Donato", is_staff=False, is_superuser=False)
    novo_user3 = Users.objects.create(username="LucasRibeiro", email="lucasribeiro@outlook.com", password="132456", first_name="Lucas", last_name="Ribeiro", is_staff=False, is_superuser=False)
    
    users = Users.objects.all()
    
    return render(request, 'users/show_users.html', {'users':users})