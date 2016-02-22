from django.conf.urls import patterns, include, url

import requests

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
   url(r'^question/new$', 'fts_question.views.stub',
       name='question_new'),
     # POST question_text
   url(r'^question/(?P<qid>[0-9]+)/answer$', 'fts_question_answer.views.stub',
       name='question_answer'),
   url(r'^answer/(?P<aid>[0-9]+)/sound$', 'fts_question_answer.views.stub',
       name='answer_sound'),
   url(r'^answer/(?P<aid>[0-9]+)/question$', 'fts_question_answer.views.stub',
       name='answer_question'),
   url(r'^answer/(?P<qid>[0-9]+)/new$', 'fts_question_answer.views.stub',
       name='answer_new'),
     # POST sound_file                       
   url(r'^answer/(?P<aid>[0-9]+)/status$', 'fts_question_answer.views.stub',
       name='answer_status'),
     # POST accepted_yes_no
)

import settings

if requests.post(settings.FTS_MAIN_URL + '/register/question_answer', data="http://localhost:8001/").text != "OK":
    # TODO fail
    die()

