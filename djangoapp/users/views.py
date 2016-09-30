from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse

from .userforms import AddUserForm
from .models import User


def index(request):
    return render(request, 'index.html', {})

def list_users(request):
    users = User.objects.all()

    context = {
        'users': users,
    }
    return render(request, 'list_users.html', context)

def add_user(request):
    form = AddUserForm()
    return render(request, 'add_users.html',  {'form': form})

def post_new(request):
    if request.method == "POST":
        form = AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_users')
        else:
            return render(request, 'add_users.html', {'form': form})
    else:
        form = AddUserForm()
        return render(request, 'add_users.html', {'form': form})
