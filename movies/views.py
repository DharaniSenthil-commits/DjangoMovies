from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Movie
# Create your views here.


def index(request):
    movie = Movie.objects.all()
    # output = ','.join([m.title for m in movie])
    # return HttpResponse(output)

    return render(request, 'movies/index.html', {'movies': movie})


def detail(request, movie_id):
    movie_detail = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movies/detail.html', {'movie_detail': movie_detail})
    # return HttpResponse(movie_id)
    # try:
    #     movie_detail = Movie.objects.get(pk=movie_id)
    #     return render(request, 'movies/detail.html', {'movie_detail': movie_detail})
    #     # return HttpResponse(movie_id)
    # except Movie.DoesNotExist:
    #     raise Http404()
