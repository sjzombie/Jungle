from django.shortcuts import render
from .models import User

def index(request):
    All_User = User.objects.all()
    return render(request, 'register/register.html', {'User': All_User})
