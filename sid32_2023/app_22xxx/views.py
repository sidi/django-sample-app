from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import *
from django.urls import reverse_lazy

# Create your views here.
def home(request):
    mymsg = request.GET.get('message')
    return render(request, 'home.html', {'user_message': mymsg})

def list(request):
    mymsg = request.GET.get('message')
    return render(request, 'home.html', {'user_message': mymsg})

class DepartmentList(ListView):
    model = Department

class DepartmentDetail(DetailView):
    model = Department  

class DepartmentCreate(CreateView):
    model = Department
    fields = '__all__'
    success_url = reverse_lazy('department_list')

class DepartmentDelete(DeleteView):
    model = Department
    success_url = reverse_lazy('department_list')

class DepartmentUpdate(UpdateView):
    model =  Department
    fields = '__all__'
    success_url = reverse_lazy('department_list')
