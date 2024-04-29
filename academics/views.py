from django.shortcuts import render
from django.http import HttpResponse

from academics.models import User
from .forms import UserForm

def index(request):
    return HttpResponse("Hello, world. You're at the academics index.")


def list_users(request):
    users=User.objects.all()
    return render(request, 'academics/list_users.html', {'users': users})
# Create your views here.
def crate_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserForm()
    return render(request, 'academics/create_user.html', {'form': form })