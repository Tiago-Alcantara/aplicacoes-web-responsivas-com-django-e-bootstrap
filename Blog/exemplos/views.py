from django.shortcuts import render

# Create your views here.

def get_bootstrap(request):
    return render(request,'exemplos/07_layouts.html')