from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('merchandise/', views.merchandise, name='merchandise'),
    path('', views.stalks, name='stalks'),
    path('services/', views.services, name='services'),
    path('addstalks', views.addStalks, name='addingstalks'),

    path('addstalks', views.addStalks, name='addingstalks'),

    path('updatestalks/<int:id>/', views.updatestalks, name='updatestalks'),
    path('deletemerchandise/<int:id>/', views.deletestalks, name='deletemerchandise'),  # Ensure trailing slash and int:id



]