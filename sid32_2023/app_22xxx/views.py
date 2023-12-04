from django.shortcuts import render
from django.views.generic import ListView
from .models import *

# Create your views here.
def home(request):
    mymsg = request.GET.get('message')
    return render(request, 'home.html', {'user_message': mymsg})

def list(request):
    mymsg = request.GET.get('message')
    return render(request, 'home.html', {'user_message': mymsg})

class DepartementList(ListView):
    model = Department
