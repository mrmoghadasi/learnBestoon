
#from __future__ import unicode_literals
#my Token
# mFcoR2upMjsJWZYxwiZum4HVoTwvZSeuMyMiUFU0RjPMou9q
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
#from django.utils import timezone

# Create your models here.
class Expense(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User)

    def __str__(self):
        #return self.text
        return "{}-{}".format(self.date, self.amount)

'''
    def __unicode__(self):
        return "{}-{}".format(self.date, self.amount)
        return self.text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        '''

class Income(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User)

    '''
    def __unicode__(self) :
        return "{}-{}".format(self.date, self.amount)
        return self.text'''
    def __str__(self):
        #return self.text
        return "{}-{}".format(self.date, self.amount)
