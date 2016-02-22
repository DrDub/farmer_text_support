from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
   url(r'^expert/who$', 'fts_answer.views.stub', 
       name='expert_who'),
      # POST question_id
   url(r'^expert/new_user$', 'fts_answer.views.stub', 
       name='expert_new_user'),
      # POST user_id
   url(r'^expert/new_question$', 'fts_answer.views.stub', 
       name='expert_new_question'),
      # POST question_id
   url(r'^expert/new_answer$', 'fts_answer.views.stub', 
       name='expert_new_answer'),
      # POST user_id, question_id
   url(r'^expert/new_answer_status$', 'fts_answer.views.stub', 
       name='expert_answer_status'),
      # POST user_id, question_id, answer_id, accepted_yes_no
)
