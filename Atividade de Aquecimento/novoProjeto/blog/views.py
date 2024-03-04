from django.shortcuts import render

posts = [
    {
        'author': 'Jorge',
        'title': 'Post 1',
        'content': 'Primeiro Post!',
        'date': '31 de Abril, 2023'
    },
    {
        'author': 'Carlos',
        'title': 'Post 2',
        'content': 'Segundo Post!',
        'date': '01 de Maio, 2023'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    context = {
        'title': 'Sobre'
    }
    return render(request, 'blog/about.html', context)