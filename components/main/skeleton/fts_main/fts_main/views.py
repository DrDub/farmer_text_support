from django.http import Http404, HttpResponseRedirect,HttpResponseForbidden, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext

from .models import Component

import requests

def home(request):
    return HttpResponse('<h1>Farmer Text Support</h1> See <a href="http://wiki.duboue.net/index.php/Farmer_Text_Support">Web site</a> for details.')

def register(request,component=None):
    if request.META['REMOTE_ADDR'] != '127.0.0.1':
        return HttpResponseForbidden()

    if request.method != 'POST':
        return HttpResponse('<h1>Use POST</h1>')

    if not 'url' in request.POST:
        return HttpResponse('<h1>Missing URL</h1>')

    Component(
        name=component.lower(),
        url=POST['url']
    ).save()
    
    return HttpResponse('<h1>Success</h1>')

def wrap(request, component, **kwargs):
    url = Component.objects.filter(name=component)
    if url.count() == 0:
        return HttpResponse('<h1>Not implemented</h1>')
    url = url[0].url
    if request.method == 'POST':
        return HttpResponse(requests.post(url + '/' + request.path,
                                          data=request.POST).text)
    else:
        return HttpResponse(requests.get(url + '/' + request.path).text)

def stub(request,**kwargs):
    return HttpResponse('<h1>Not implemented</h1>')
