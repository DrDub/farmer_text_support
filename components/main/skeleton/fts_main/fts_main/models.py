from django.db import models


class Component(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    url = models.CharField(max_length=1024)
