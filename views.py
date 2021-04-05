from django.shortcuts import render, redirect
import requests
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.
def register(request):
    if request.method == 'POST':
       form = UserCreationForm(request.POST)
       if form.is_valid():
        form.save()
        return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data= request.POST)
        if form.is_valid():
            return index('home')
        else:
            form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})

def index(request):
    data = True
    result = None
    globalSummary = None
    countries = None;
    while(data):
        try:
         result = requests.get('https://api.covid19api.com/summary')
         json = result.json()
         globalSummary = json['Global']
         countries = json['Countries']
         data = False
        except:
            data = True
    return render(request ,'index.html',{'globalSummary' : globalSummary ,
                                         'countries' : countries})
