from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

def index(request):
    return render(request, 'system/index.html')

def bike(request):
    return render(request, 'system/biker.html')

def truck(request):
    return render(request, 'system/trucker.html')

def transport(request):
    return render(request, 'system/transport.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')

    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request,'registration/register.html', context)

def bform(request):
    return render(request,'system/employee/bform.html')

def cform(request):
    return render(request,'system/employee/cform.html')
def tform(request):
    return render(request,'system/employee/tform.html')

def book(request):
    return render(request,'registration/book.html')

def about(request):
    return render(request,'system/about.html')
def house(request):
    return render(request,'system/services/house.html')
def corporate(request):
    return render(request,'system/services/corporate.html')
def office(request):
    return render(request,'system/services/office.html')
def personal(request):
    return render(request,'system/services/personal.html')
def housemore(request):
    return render(request,'system/services/housemore.html')
def corporatemore(request):
    return render(request,'system/services/corporatemore.html')
def officemore(request):
    return render(request,'system/services/officemore.html')
def personalmore(request):
    return render(request,'system/services/personalmore.html')

def cbook(request):
    return render(request,'registration/cbook.html')
def pbook(request):
    return render(request,'registration/pbook.html')
def ofbook(request):
    return render(request,'registration/ofbook.html')