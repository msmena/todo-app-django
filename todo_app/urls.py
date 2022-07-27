from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListListView.as_view(), name='index'),
    path('list/<int:list_id>/', views.ItemListView.as_view(), name='list'),
    # CRUD patters for ToDoList
    path('list/add/', views.ListCreate.as_view(), name='list_add'),
    path('list/<int:pk>/delete/', views.ListDelete.as_view(), name='list_delete'),
    # CRUD patters for ToDoItem
    path('list/<int:list_id>/item/add/',
         views.ItemCreate.as_view(), name='item_add'),
    path('list/<int:list_id>/item/<int:pk>/',
         views.ItemUpdate.as_view(), name='item_update'),
    path('list/<int:list_id>/item/<int:pk>/delete/',
         views.ItemDelete.as_view(), name='item_delete'),
]
