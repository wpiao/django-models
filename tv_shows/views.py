from django.views.generic import ListView, DetailView
from .models import TvShow

# Create your views here.
class TvShowListView(ListView):
    template_name = 'tvshows_list.html'
    model = TvShow
    context_object_name = 'tvshows_list'


class TvShowDetailView(DetailView):
    template_name = 'tvshows_detail.html'
    model = TvShow