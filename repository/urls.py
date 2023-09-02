from django.urls import path
from repository.views import home


urlpatterns = [
    path('', home),

]