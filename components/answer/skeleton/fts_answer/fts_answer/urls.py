from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
   url(r'^expert/targets/(?P<qid>[0-9]+)$', 'fts_answer.views.stub', 
       name='expert_targets'),
   url(r'^expert/new_question$', 'fts_answer.views.stub', 
       name='expert_new_question'),
      # POST question_id
   url(r'^expert/new_answer$', 'fts_answer.views.stub', 
       name='expert_new_answer'),
      # POST user_id, question_id
   url(r'^expert/answer_status$', 'fts_answer.views.stub', 
       name='expert_answer_status'),
      # POST user_id, question_id, accepted_yes_no
)
