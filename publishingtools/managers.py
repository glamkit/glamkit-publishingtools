from django.conf import settings
from django.db.models import Manager
from django.conf import settings

class PublishStatusableManager(Manager):
    """
    A manager for the production site; only published portraits are returned.
    """
    
    def get_query_set(self):
        if settings.PUBLISHINGTOOLS_OVERRIDE_PUBLISH_STATUS:
            return super(PublishStatusableManager, self).get_query_set() 
        return super(PublishStatusableManager, self).get_query_set().filter(status=settings.PUBLISHINGTOOLS_STATUS_CHOICE.PUBLISHED.value)
