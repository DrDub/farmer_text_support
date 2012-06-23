from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
   url(r'^expert/targets/(?P<qid>[0-9]+)$', 'fts_answer.views.stub',
       name='expert_targets'),
   url(r'^expert/asked/(?P<uid>[0-9]+)$', 'fts_answer.views.stub',
       name='expert_asked'),
      # POST question_text
   url(r'^expert/answered/(?P<qid>[0-9]+)$', 'fts_answer.views.stub',
       name='expert_answered'),
      # POST user_id
   url(r'^expert/status/(?P<aid>[0-9]+)$', 'fts_answer.views.stub',
       name='expert_status'),
      # POST user_id, accepted_yes_no
)
