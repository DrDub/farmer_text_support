from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
   url(r'^sms/send$', 'fts_sms.views.stub', name='sms_send'),
     # POST user_id, message_type, message_data
)
