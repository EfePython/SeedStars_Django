from django.shortcuts import render
from django.http import HttpResponse



def index(request):
    return HttpResponse("Hello, world. You're at the users index.")

def list_users(request):
    # return HttpResponse("Hello, world. You're at the users list_users.")

    context = {
        'users': [{
            'name' : "Efe Ariaroo",
            'email' : "efeariaroo@gmail.com"
        }],
    }
    # Will automatically look for 'list_users.html' inside the 'templates' directory
    return render(request, 'list_users.html', context)

def add_user(request):
    return HttpResponse("Hello, world. You're at the users add_user.")
