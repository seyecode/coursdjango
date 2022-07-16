from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'gestion/index.html')

def accueil(request, id=None):
    if id is not None:
        return render(request, 'gestion/accueil.html', {'id': id})
    
    return render(request, 'gestion/accueil.html')

def about(request):
    return render(request, 'gestion/apropos.html')

def contact(request):
    return render(request, 'gestion/contact.html')