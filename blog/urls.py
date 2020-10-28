from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    #post/ significa que la URL debería empezar con la palabra post seguida por una /.
    #<int:pk> significa que Django buscará un número entero y se lo pasará a la vista en una variable llamada pk.
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]