from celery import Celery
from celery import task
from Requests.models import Volunteer_ngo_request
from Registration.models import NGODomains

@task
def duplicate(a):
    NGODomains.objects.create(domain = a)
    b=a+"poop"
    return NGODomains.objects.all()
@task
def sum(a,b):
    return a+b
