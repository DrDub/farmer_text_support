from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
   url(r'^user/new$', 'fts_user.views.stub', name='user_new'),
     # POST phone_number
   url(r'^user/(?P<id>[0-9]+)$', 'fts_user.views.stub', name='user_view'),
   url(r'^user/search/by_contact$', 'fts_user.views.stub', name='user_search'),
   url(r'^user/(?P<uid>[0-9]+)/question/new$', 'fts_user.views.stub',
       name='user_question_new'),
     # POST question_id
   url(r'^user/(?P<uid>[0-9]+)/answer/new$', 'fts_user.views.stub',
       name='user_answer_new'),
     # POST answer_id
   url(r'^user/(?P<qid>[0-9]+)/answer/(?P<qid>[0-9]+)/status$', 'fts_user.views.stub',
       name='user_answer_status'),
     # POST accepted_yes_no
)
