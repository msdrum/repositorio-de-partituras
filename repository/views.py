from django.shortcuts import render

def home(request):
    return  render(request, 'repository/pages/home.html')
