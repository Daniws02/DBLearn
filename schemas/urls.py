from django.urls import path
from . import views

urlpatterns = [
    path('<str:model_name>/', views.list, name='list'),
    path('<str:model_name>/create/', views.create, name='create'),
    path('<str:model_name>/<str:id>/', views.detail, name='detail'),
    path('<str:model_name>/<str:id>/update/', views.update, name='update'),
    path('<str:model_name>/<str:id>/delete/', views.delete, name='delete'),
]