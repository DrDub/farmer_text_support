from django.db import models


class Component(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    url = models.CharField(max_length=1024)

class OutstandingQuestion(models.Model):
    question_id = models.IntegerField(db_index=True)
    since = models.DateField()
