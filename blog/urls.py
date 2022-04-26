from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogListView.as_view(), name='home'),
    path('post/<int:pk>', views.BlogDetailView.as_view(), name='detail'),
    path('post/new/', views.BlogCreateView.as_view(), name='create')
]