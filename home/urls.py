
from django.urls import path
from . import views
urlpatterns = [
    path('', views.ShowNewsList.as_view(), name="home"),
    path('discount/<int:pk>/', views.NewsDetailView.as_view(), name='discount_detail'),
]
