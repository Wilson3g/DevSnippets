from django.urls import path
from .views import (
    HomeView, 
    DetailView, 
    AddPostView,
    UpdatePostView,
    DeletePostView,
    AddCategoryView,
    UpdateCategoryView,
    ListCategoryView,
    DeleteCategoryView
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('artigo/<int:pk>', DetailView.as_view(), name='detail_post'),
    path('artigo/novo/', AddPostView.as_view(), name='new_post'),
    path('artigo/atualizar/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('artigo/excluir/<int:pk>', DeletePostView.as_view(), name='delete_post'),
    path('categoria/novo/', AddCategoryView.as_view(), name='new_category'),
    path('categoria/atualizar/<int:pk>', UpdateCategoryView.as_view(), name='update_category'),
    path('categoria/lista/', ListCategoryView.as_view(), name='list_category'),
    path('categoria/excluir/<int:pk>/', DeleteCategoryView.as_view(), name='delete_category'),
]
