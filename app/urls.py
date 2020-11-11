from django.urls import path
from .views import HomeView, DetailView, AddPostView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('detail/<int:pk>', DetailView.as_view(), name='detail_post'),
    path('new-post/', AddPostView.as_view(), name='new_post')
]
