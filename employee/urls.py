from django.urls import path
from employee import views

urlpatterns = [
    path('index/',views.create, name="index"),
    path('read/',views.read, name='read'),
    path('delete/<int:id>/',views.delete, name='delete'),
    path('update/<int:id>/',views.update, name='usr_update')
]