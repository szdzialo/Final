from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Question(models.Model):
        title = models.CharField(max_length=500)
        description = models.TextField(null=True, blank=True)
        created_at = models.DateTimeField(auto_now_add=True)
        user = models.ForeignKey(User)
        
        def __unicode__(self):
                return self.title