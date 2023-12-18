from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import *
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

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

class ModuleList(ListView):
    model = Module

class ModuleDetail(DetailView):
    model = Module

class ModuleCreate(CreateView):
    model = Module
    fields = '__all__'
    success_url = reverse_lazy('module_list')

class ModuleDelete(DeleteView):
    model = Module
    success_url = reverse_lazy('module_list')

class ModuleUpdate(UpdateView):
    model =  Module
    fields = '__all__'
    success_url = reverse_lazy('module_list')

class ModuleByDeptListView(ListView):
    template_name = "app_22xxx/module_list.html"

    def get_queryset(self):
        self.department = get_object_or_404(Department, name=self.kwargs["department"])
        return Module.objects.filter(department=self.department)
