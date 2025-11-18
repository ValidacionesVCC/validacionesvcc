from django.shortcuts import render

def inicio_view(request):
    return render(request, 'core/inicio.html')
