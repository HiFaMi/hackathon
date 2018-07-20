from django.urls import path

from . import views

urlpatterns = [
    path('choose/', views.choose_category, name='category'),
    path('food/', views.show_foodstuff, name='food')
]
