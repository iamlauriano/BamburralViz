from django.shortcuts import render

def consulta(request):
    return render(request, "plantas/index.html")

