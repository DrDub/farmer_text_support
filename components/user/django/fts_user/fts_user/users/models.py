from django.db import models

class FTS_User(models.Model):
    phone_number = models.CharField(max_length=50, db_index=True)

class Answer(models.Model):
    user = models.ForeignKey(FTS_User)
    answer_id = models.IntegerField()

class Question(models.Model):
    user = models.ForeignKey(FTS_User)
    question_id = models.IntegerField()

class Status(models.Model):
    user = models.ForeignKey(FTS_User)
    answer = models.ForeignKey(Answer)
    status = models.CharField(max_length=10)
