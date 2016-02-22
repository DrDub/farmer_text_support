from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
   url(r'^$', 'fts_main.views.home', name='home'),

   # main
   url(r'^register/(?P<component>[^/]+)$', 'fts_main.views.register', name='component_register'),
     # POST url

   # question
   url(r'^question/new$', 'fts_main.views.question_new', {'component':'question_answer'},
       name='question_new'),
     # POST question_text
   url(r'^question/(?P<qid>[0-9]+)/answer$', 'fts_main.views.wrap', {'component':'question_answer'},
       name='question_answer'),
   url(r'^answer/(?P<aid>[0-9]+)/sound$', 'fts_main.views.wrap', {'component':'question_answer'},
       name='answer_sound'),
   url(r'^answer/(?P<aid>[0-9]+)/question$', 'fts_main.views.wrap', {'component':'question_answer'},
       name='answer_question'),
   url(r'^answer/(?P<qid>[0-9]+)/new$', 'fts_main.views.wrap', {'component':'question_answer'},
       name='answer_new'),
     # POST sound_file
   url(r'^answer/(?P<aid>[0-9]+)/status$', 'fts_main.views.answer_status', {'component':'question_answer'},
       name='answer_status'),
     # POST accepted_yes_no

   # user repo
   url(r'^user/new$', 'fts_main.views.wrap', {'component':'user'}, name='user_new'),
     # POST phone_number
   url(r'^user/(?P<id>[0-9]+)$', 'fts_main.views.wrap', {'component':'user'}, name='user_view'),
   url(r'^user/search/by_contact$', 'fts_main.views.wrap', {'component':'user'}, name='user_search_contact'),
   url(r'^user/search/by_question$', 'fts_main.views.wrap', {'component':'user'}, name='user_search_question'),
   url(r'^user/(?P<uid>[0-9]+)/question/new$', 'fts_main.views.wrap', {'component':'user'},
       name='user_question_new'),
     # POST question_id
   url(r'^user/(?P<uid>[0-9]+)/answer/new$', 'fts_main.views.wrap', {'component':'user'},
       name='user_answer_new'),
     # POST answer_id
   url(r'^user/(?P<qid>[0-9]+)/answer/(?P<qid>[0-9]+)/status$', 'fts_main.views.wrap', {'component':'user'},
       name='user_answer_status'),
     # POST accepted_yes_no
   
   # comm - sms
   url(r'^comm/sms/send$', 'fts_main.views.wrap', {'component':'comm'}, name='sms_send'),
     # POST user_id, message_type, message_data
   
   # comm - phone
   url(r'^comm/phone/call$', 'fts_main.views.wrap', {'component':'comm'}, name='phone_call'),
     # POST user_id, message_type, message_data
   
   # expert
   url(r'^expert/targets/(?P<qid>[0-9]+)$', 'fts_main.views.wrap', {'component':'expert'},
       name='expert_targets'),
   url(r'^expert/new_question$', 'fts_main.views.wrap', {'component':'expert'},
       name='expert_new_question'),
      # POST question_id
   url(r'^expert/new_answer$', 'fts_main.views.wrap', {'component':'expert'},
       name='expert_new_answer'),
      # POST user_id, question_id
   url(r'^expert/answer_status$', 'fts_main.views.wrap', {'component':'expert'},
       name='expert_answer_status'),
      # POST user_id, question_id, accepted_yes_no
   )
