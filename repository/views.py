from django.shortcuts import render

from utils.repository.sheets import make_sheet

def home(request):
    return  render(request, 'repository/pages/home.html', context={
        'repository': [make_sheet() for _ in range (6)], 
    })

def sheet(request, id):
    return  render(request, 'repository/pages/sheet-detail.html', context={
        'sheet': make_sheet(),
    })
