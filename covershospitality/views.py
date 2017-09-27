from django.shortcuts import render


def index(request):
    return render(request, 'covershospitality/templates/index.html')