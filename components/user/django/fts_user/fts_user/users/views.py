from django.http import Http404, HttpResponseRedirect,HttpResponseForbidden, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext

from .models import FTS_User, Answer

def user_new(request):
    if request.method != 'POST':
        raise Http404('Use POST')

    if not 'phone_number' in request.POST:
        raise Http404('phone number missing')        
    
    user = FTS_User(
        phone_number=request.POST['phone_number']
    ).save()

    return HttpResponse(user.id)

def user_view(request, uid):
    return HttpResponse(json.dumps({'phone_number':FTS_User.objects.get(pk=uid)}),
                         content_type='application/x-javascript')

def user_view(request, uid):
    return HttpResponse(json.dumps({'phone_number':FTS_User.objects.get(pk=uid)}),
                         content_type='application/json')

def user_search(request, search_by=None):
    if request.method != 'GET':
        raise Http404('Use GET')
    try:
        if search_by == 'contact':
            return HttpResponse(json.dumps({'user_id':FTS_User.objects.get(phone_number=request.GET['phone_number'])}),
                                content_type='application/json')
        if search_by == 'question':
            return HttpResponse(json.dumps({'user_id':FTS_User.objects.get(question_id=int(request.GET['answer_id']))}),
                                content_type='application/json')
    except:
        return HttpResponse("[]", content_type='application/json')

def user_question_new(request, uid):
    if request.method != 'POST':
        raise Http404('Use POST')

    user = FTS_User.objects.get(pk=uid)
    Question(
        user=user,
        question_id = int(request.POST['question_id'])
    ).save()
    return HttpResponse("[]", content_type='application/json')

def user_answer_new(request, uid):
    if request.method != 'POST':
        raise Http404('Use POST')

    user = FTS_User.objects.get(pk=uid)
    Answer(
        user=user,
        answer_id = int(request.POST['answer_id'])
    ).save()
    return HttpResponse("[]", content_type='application/json')

def user_answer_status(request, uid, aid):
    if request.method == 'POST':
        if not 'accepted_yes_no' in request.POST:
            raise Http404('missing accepted_yes_no')
        status = Status.objects.get(
            user__id = uid,
            answer__answer_id = aid)
        status.status = request.POST['accepted_yes_no']
        status.save()
    else:
        return HttpResponse(Status.objects.get(
            user__id = uid,
            answer__answer_id = aid).status)
        
    return HttpResponse("", content_type='text/plain')


    

        
        
        
    




