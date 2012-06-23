from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
   url(r'^phone/call$', 'fts_phone.views.stub', name='phone_call'),
     # POST user_id, message_type, message_data
                       
)
