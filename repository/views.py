from django.shortcuts import render

def home(request):
    return  render(request, 'repository/pages/home.html')

def sheet(request, id):
    return  render(request, 'repository/pages/sheet-detail.html')
