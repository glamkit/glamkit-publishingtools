from django.db import models
from publishingtools.models import PublishStatusable
from publishingtools.managers import PublishStatusableManager

class PublishStatusableObject(PublishStatusable):
    objects = PublishStatusableManager()
    
    name = models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.name