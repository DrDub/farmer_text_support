from django.db import models

class KnownUser(models.Model):
    user_id = models.IntegerField(db_index=True)

class KnownQuestion(models.Model):
    asker = models.ForeignKey(KnownUser)
    question_id = models.IntegerField(db_index=True)

class AskedAlready(models.Model):
    user = models.ForeignKey(KnownUser)
    question = models.ForeignKey(KnownQuestion)
