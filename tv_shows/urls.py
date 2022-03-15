from django.urls import path
from .views import TvShowListView, TvShowDetailView

urlpatterns = [
    path('', TvShowListView.as_view(), name='tvshow_list'),
    path('<int:pk>', TvShowDetailView.as_view(), name='tvshow_detail'),
]
