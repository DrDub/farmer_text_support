from django.http import Http404, HttpResponseRedirect,HttpResponseForbidden, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from django.conf import settings

from .models import KnownUser, KnownQuestion, AskedAlready


import requests

def ignore(request):
    return HttpResponse()

def who(request):
    if request.method != 'POST':
        raise Http404('Use POST')
    if not 'question_id' in request.POST:
        raise Http404('Missing question_id')

    question = KnownQuestion.objects.get(question_id=request.POST['question_id'])
    
    users = KnownUser.objects.raw(
        """
        SELECT user_id
        FROM answers_knownuser
        WHERE
          NOT user_id IN (
            SELECT user_id
            FROM answers_knownuser
            INNER JOIN answers_askedalready
            ON answers_knownuser.id = answers_askedalready.user
            WHERE answers_askedalready.question = '%s'
          )
          AND NOT user_id = '%s'
        """ % (question.id, question.asker.user_id)
    )
    if users.count() == 0:
        return HttpResponse()
    user = users[randint(0, len(users))]
    AskedAlready(
        user=user,
        queston=question
    ).save()
        
    return HttpResponse(user.user_id)

def new_user(request):
    if request.method != 'POST':
        raise Http404('Use POST')
    if not 'question_id' in request.POST:
        raise Http404('Missing user_id')

    KnownUser(
        user_id=request.POST['user_id']
    ).save()
    return HttpResponse()

def new_question(request):
    if request.method != 'POST':
        raise Http404('Use POST')
    if not 'question_id' in request.POST:
        raise Http404('Missing question_id')

    question_id=request.POST['question_id']

    # TODO call the broker to get asker_id
    asker_id=requests.get("%s/user/by_question" % (settings.MAIN_URL,),
                          data={'question_id'=question_id}).text

    users=KnownUser.objects.filter(user_id=asker_id)
    if users.count() == 0:
        user=KnownUser(user_id=asker_id)
        user.save()
    else:
        user=users[0]

    KnownQuestion(
        asker=user,
        question_id=question_id
    ).save()
    return HttpResponse()

    
    
        
