from django.db import models
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from movies.models import Movie

# Create your models here.


class MovieResources(ModelResource):
    class Meta:
        queryset = Movie.objects.all()
        resource_name = 'movies'
        authorization = Authorization()
        excludes = ['date_created']
