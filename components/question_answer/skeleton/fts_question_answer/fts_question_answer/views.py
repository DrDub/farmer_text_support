from django.http import Http404, HttpResponseRedirect,HttpResponseForbidden, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext

def stub(request,**kwargs):
    return HttpResponse('<h1>Not implemented</h1>')
