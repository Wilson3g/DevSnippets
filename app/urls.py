from django.urls import path
from .views import HomeView, DetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('detail/<int:pk>', DetailView.as_view(), name='detail_post')
]
