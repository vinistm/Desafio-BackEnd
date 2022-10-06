from django.db import models
from django.forms import CharField


class COMPANY(models.Model):
    title = CharField(max_length=120)
    fileds = models.FileField(upload_to ='upload/')