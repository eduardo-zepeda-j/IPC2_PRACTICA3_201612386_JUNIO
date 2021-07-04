
from django.urls import path
from texto import views

urlpatterns = [
    path('',views.home, name = 'Home'),
    path('textopost/',views.post, name ='textopost'),
    path('textoput/',views.put, name ='textoput'),
    path('textodelete/',views.delete, name ='textodelete'),
    
]