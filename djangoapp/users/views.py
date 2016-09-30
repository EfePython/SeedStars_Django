from django.shortcuts import render
from django.http import HttpResponse

from .userforms import AddUserForm
from .models import User


def index(request):
    # Will automatically look for 'list_users.html' inside the 'templates' directory
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
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)

            post.name = request.user_name
            post.email = request.user_email
            post.save()

            return redirect('list_users', pk=post.pk)
    else:
        form = PostForm()
    return render(request,'add_users.html', {'form': form})
