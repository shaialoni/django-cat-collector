from django.urls import path
from . import views

# This has to be called 'urlpatterns'
urlpatterns = [
    # path to localhost/ home path
    # inside of django leading / isn't a thing.
    # never add a leading /
    path('', views.index, name='index'),
    path('cats/', views.cat_index, name='cat_index'),
    path('cats/<int:cat_id>/', views.cat_show, name='cats_show'),
    path('cats/create/', views.CatCreate.as_view(), name='cat_create'),
    path('cats/<int:pk>/update/', views.CatUpdate.as_view(), name='cat_update'),
    path('cats/<int:pk>/delete/', views.CatDelete.as_view(), name='cat_delete'),
    path('user/<username>/', views.profile, name='profile'),
]