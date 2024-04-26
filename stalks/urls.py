from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('merchandise/', views.merchandise, name='merchandise'),
    path('', views.stalks, name='stalks'),
    path('services/', views.services, name='services'),
    path('addstalks', views.addstalks, name='addingstalks'),

    path('addstalks', views.addstalks, name='addingstalks'),

    path('updatestalks/<id>', views.updatestalks, name='updatestalks'),
    path('deletestalks/<id>', views.deletestalks),



]