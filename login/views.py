from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from.forms import *
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, User
from django.contrib.auth.decorators import user_passes_test
from braces.views import GroupRequiredMixin
from django.views.generic import TemplateView


# Create your views here.
def home(request):
    return render (request, 'home.html')

@login_required


def products(request):
    return render(request, 'products.html')

def exit (request):
    logout(request)
    return redirect('home')

def homeA(request):
    return render (request, 'homeA.html')





#esta funcion nos permite validar y registrar a los nuevos usuarios usando registros directamente de django

def register(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST' :
        user_creation_form = CustomUserCreationForm(data=request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save()

            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)
            return redirect('home') # Redirigir a la página principal si no es un administrador

    return render (request,'registration/register.html',data )

# Verificar si el usuario pertenece al grupo de administradores
@user_passes_test(lambda user: user.groups.filter(name='Administradores').exists(), login_url='home')
def admin_home(request):
  return render(request, 'templates/homeA.html')

















