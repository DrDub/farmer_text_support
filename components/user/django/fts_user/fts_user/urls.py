from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
   url(r'^user/new$', 'fts_user.users.views.user_new', name='user_new'),
     # POST phone_number
   url(r'^user/(?P<uid>[0-9]+)$', 'fts_user.users.views.user_view', name='user_view'),
   url(r'^user/search/by_contact$', 'fts_main.views.wrap', {'search_by': 'contact'}, name='user_search'),
   url(r'^user/search/by_question$', 'fts_main.views.wrap', {'search_by': 'question'}, name='user_search'),
   url(r'^user/(?P<uid>[0-9]+)/question/new$', 'fts_user.users.views.user_question_new',
       name='user_question_new'),
     # POST question_id
   url(r'^user/(?P<uid>[0-9]+)/answer/new$', 'fts_user.users.views.user_answer_new',
       name='user_answer_new'),
     # POST answer_id
   url(r'^user/(?P<uid>[0-9]+)/answer/(?P<aid>[0-9]+)/status$', 'fts_user.users.views.user_answer_status',
       name='user_answer_status'),
     # POST accepted_yes_no or GET 
)
