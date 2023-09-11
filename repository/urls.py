from django.urls import path
from repository import views


urlpatterns = [
    path('', views.home),
    path('sheet/<int:id>/', views.sheet),

]