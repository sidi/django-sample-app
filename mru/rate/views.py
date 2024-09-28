from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import *
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

# Create your views here.

def home(request):
    
    if request.method == 'GET' and 'cur' in request.GET:
        ccode = request.GET['cur']
    else:
        ccode = "USD"
    
    currency = get_object_or_404(Currency, code=ccode)
    #Module.objects.filter(department=self.department)

    labels = []
    values = []

    stats = Rate.objects.filter(currency=currency).order_by('date')

    for row in stats:
        labels.append(row.date)
        values.append(row.sell)

    context = {
        "labels": labels,
        "values": values,
        "currency": ccode,
        "labels_2": ['MRU','USD', 'EUR'],
        "values_2": [20,55,35],
    }

    return render(request, 'home.html', context)

def home_pie(request):
    

    context = {
        "labels": ['MRU','USD', 'EUR'],
        "values": [20,55,35],

    }

    return render(request, 'home_pie.html', context)

class CurrencyList(ListView):
    model = Currency

class CurrencyDetail(DetailView):
    model = Currency  

class CurrencyCreate(CreateView):
    model = Currency
    fields = '__all__'
    success_url = reverse_lazy('currency_list')

class CurrencyDelete(DeleteView):
    model = Currency
    success_url = reverse_lazy('currency_list')

class CurrencyUpdate(UpdateView):
    model =  Currency
    fields = '__all__'
    success_url = reverse_lazy('currency_list')

class RateList(ListView):
    model = Rate

class RateDetail(DetailView):
    model = Rate

class RateCreate(CreateView):
    model = Rate
    fields = '__all__'
    success_url = reverse_lazy('rate_list')

class RateDelete(DeleteView):
    model = Rate
    success_url = reverse_lazy('rate_list')

class RateUpdate(UpdateView):
    model =  Rate
    fields = '__all__'
    success_url = reverse_lazy('rate_list')

def import_currency_csv(request):
    if "GET" == request.method:
        return render(request, "csv_import.html", {'oname': "Currency", 'opath': "currency"})
    try:
        object_list = []
        csv_file = request.FILES["formFile"]
        file_data = csv_file.read().decode("utf-8")
        #code, label
        lines = file_data.split("\n")
        for line in lines:			
            fields = line.split(",")
            ob = Currency()
            ob.code = fields[0]
            ob.label = fields[1]
            object_list.append(ob)
        
        Currency.objects.bulk_create(object_list)

    except Exception as e:
        print("Error! Unable to upload file. " + repr(e))
        return HttpResponseRedirect(reverse("currency_import"))

    return HttpResponseRedirect(reverse("currency_list"))

def import_rate_csv(request):
    if "GET" == request.method:
        return render(request, "csv_import.html", {'oname': "Rate", 'opath': "rate"})
    try:
        object_list = []
        csv_file = request.FILES["formFile"]
        file_data = csv_file.read().decode("utf-8")
        lines = file_data.split("\n")
        #print(len(lines))
        for line in lines:			
            fields = line.split(",")
            ob = Rate()
            if len(fields) == 5 :   
                ob.date = fields[0]
                ob.unit = fields[1]
                ccode = fields[2]
                currency = get_object_or_404(Currency, code=ccode)
                ob.currency = currency
                ob.sell = fields[3]
                ob.buy = fields[4]
                object_list.append(ob)
            else:
                print(fields)
        
        Rate.objects.bulk_create(object_list)

    except Exception as e:
        print("Error! Unable to upload file. " + repr(e))
        return HttpResponseRedirect(reverse("rate_import"))

    return HttpResponseRedirect(reverse("rate_list"))