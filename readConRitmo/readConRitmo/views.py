from django.shortcuts import render, redirect
from user.forms import CustomUserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from readConRitmo import urls
from django.contrib import messages
from core.models import *

def index(request):
    return render(request, 'html/index.html')

