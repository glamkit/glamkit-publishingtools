from django.db import models
from django.conf import settings

class PublishStatusableMixInBase(models.Model):

    class Meta:
        abstract = True

    def is_live(self):
        return settings.PUBLISHINGTOOLS_OVERRIDE_PUBLISH_STATUS or self.status == settings.PUBLISHINGTOOLS_STATUS_CHOICE.PUBLISHED.value

    def is_really_live(self):
        return self.status == settings.PUBLISHINGTOOLS_STATUS_CHOICE.PUBLISHED.value

class PublishStatusableMixIn(PublishStatusableMixInBase):
    status = models.IntegerField(default=settings.PUBLISHINGTOOLS_STATUS_CHOICE.DRAFT.value, db_index=True, choices=settings.PUBLISHINGTOOLS_STATUS_CHOICES )
    class Meta:
        abstract = True

class PublishedByDefaultStatusableMixIn(PublishStatusableMixInBase):
    status = models.IntegerField(default=settings.PUBLISHINGTOOLS_STATUS_CHOICE.PUBLISHED.value, db_index=True, choices=settings.PUBLISHINGTOOLS_STATUS_CHOICES )
    class Meta:
        abstract = True

