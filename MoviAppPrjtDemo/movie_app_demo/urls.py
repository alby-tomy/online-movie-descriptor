from django.urls import include, path
from . import views

app_name = 'movie_app_demo'

urlpatterns = [
    path('',views.index,name='index'),
    path('movie/<int:movieId>',views.detailsView, name='details'),
    path('addItems/',views.addItems, name='addItems'),
    path('update/<int:movieId>',views.updateField,name='updateName'),
    path('delete/<int:movieId>',views.deleteData, name='deleteName')
]
