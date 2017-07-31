
#from __future__ import unicode_literals
#my Token
# mFcoR2upMjsJWZYxwiZum4HVoTwvZSeuMyMiUFU0RjPMou9q
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
#from django.utils import timezone

class Token(models.Model) :
    """docstring fs Token."""
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    token=models.CharField(max_length=48)
    def __str__(self):
        #return self.user
        return "{}_token".format(self.user)



# Create your models here.
class Expense(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User)

    def __str__(self):
        #return self.text
        return "{}-{}".format(self.date, self.amount)



class Income(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User)

    def __str__(self):
        #return self.text
        return "{}-{}".format(self.date, self.amount)
