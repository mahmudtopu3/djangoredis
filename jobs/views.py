from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.core.cache import cache
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


from .models import Job
# Create your views here.
@api_view(['GET'])
def view_jobs(request):
 
    jobs = Job.objects.all()
    results = [job.to_json() for job in jobs]
    return Response(results, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def view_cached_jobs(request):
   
    if 'job' in cache:
        # get results from cache
        jobs = cache.get('job')
        print("from cache")
        return Response(jobs, status=status.HTTP_201_CREATED)
 
    else:
        jobs = Job.objects.all()
        results = [job.to_json() for job in jobs]
        # store data in cache
        print("store in cache")
        cache.set('job', results, timeout=CACHE_TTL)
        return Response(results, status=status.HTTP_201_CREATED)