from celery.task import task
from celery.task.sets import subtask

from .models import OutstandingQuestion
from .views import _component_url

import requests
import settings

@task(name='fts.broadcast_question', ignore_result=True)
def broadcast_question():
    """Find any outstanding questions and ask for answers"""

    outstanding = OutstandingQuestion.objects.all()
    if outstanding.count() == 0:
        return # great

    # pick one at random
    outstanding = outstanding[randint(0, len(outstanding))]
    question_id = outstanding.question_id

    # see if we have an answer in the question repository
    answer_ids = requests.get("%s/question/%s/answer" % (_component_url('question'), question_id)).text.splitlines()

    # we have to see if these answers have been accepted by the user
    for answer_id in answer_ids:
        accepted = requests.get("%s/user/%s/answer/%s/status" % (_component_url('user'), answer_id)).text
        if accepted == "PENDING":
            # an answer is available and the user haven't said anything about it
            # TODO needs to keep track of pending answers to retry calling the user or purging them
            return
        if accepted == "UNKNOWN_ID":
            # new answer, relay it to the user
            
            user_id = requests.get(_component_url('user') + "/user/search/by_question",
                                   data={'question_id': question_id}).text

            requests.post("%s/user/%s/answer/%s/status" % (_component_url('user'), user_id, answer_id),
                          data={'accepted_yes_no':'PENDING'})
            
            # contact the user with the new answer
            sound_file = requests.get("%s/answer/%s/sound" % (_component_url('question'), answer_id)).text

            requests.post("%s/phone/call" % (settings.SITE_URL),
                                    data={'user_id':user_id,
                                          'message_type': 'relay_answer',
                                          'message_data': '{"sound_file":"'+sound_file+'"}'))
            return
            
        if bool(accepted) and not accepted == "0":
            # this question is no longer outstanding
            outstanding.delete()
            return

        # bad answers, continue

    # ask the answer scout for a user_id
    user_id = requests.post(_component_url('answer') + "/expert/who",
                  data={'question_id': question_id})
    if len(user_id) > 0:
        requests.post(_component_url('sms') + "/sms/send",
                      data={'user_id':user_id,
                            'message_type':'ask',
                            'message_data':'{"question_id": "' + question_id + '"}'})
