from django.urls import path

from . import views

app_name='item' #this is used to identify the app in the template(html files for href links)
urlpatterns=[
    path('<int:pk>/', views.detail, name='detail') #pk is the primary key of the item expected to be passed in the detail view
]