from django.shortcuts import render, redirect
from . models import EventSite

def first_page(request):
    return redirect('page/1')

def page(request, pk):
    nav_objects = EventSite.objects.values('id','site_nav', 'site_nav_position').filter(site_nav_position__gt=0).order_by('site_nav_position')
    print("nav_objects: ", nav_objects)
    content_object = EventSite.objects.values().get(id=pk)
    print("content_object:\n", content_object)
    context = {'pk': pk, 'nav_objects': nav_objects, 'content_object': content_object}
    return render(request, 'event/page.html', context)
