from urllib.parse import urlparse
from django.urls import path
from .views import BlockCreateView, BlockDeleteView, BlockDetailView, BlockListView, BlockUpdateView
urlpatterns = [
    path('',BlockListView.as_view(),name='home'),
    path('page/<int:pk>/',BlockDetailView.as_view(),name='detailview'),
    path('page/new/',BlockCreateView.as_view(),name='createview'),
    path('page/<int:pk>/change/',BlockUpdateView.as_view(),name='updateview'),
    path('page/<int:pk>/delete/',BlockDeleteView.as_view(),name='deleteview'),
    ]
