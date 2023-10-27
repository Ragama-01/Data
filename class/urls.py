from django.urls import path

from class import views


urlpatterns = [
    path('',views.home, name='home'),
    path('info',views.info, name='info')
]
