from datetime import datetime, timedelta
from django.conf import settings

from publishingtools.tests.test_app.models import PublishStatusableObject

from testtools import TestToolsCase

class PublishingTest(TestToolsCase):

    test_app = 'publishingtools.tests.test_app'
    localise_app_loading = False
    
#     settings_override = {'PUBLISHINGTOOLS_OVERRIDE_PUBLISH_STATUS': False}

    def setUp(self):
        status = settings.PUBLISHINGTOOLS_STATUS_CHOICE
    
        self.draft_object = PublishStatusableObject.objects.create(
            status = status.DRAFT.value,
            name = "A first draft",
        )

        self.dummy_object = PublishStatusableObject.objects.create(
            status = status.DUMMY.value,
            name = "A test that should never get published",
        )

        self.published_object = PublishStatusableObject.objects.create(
            status = status.PUBLISHED.value,
            name="I'm ready for public exposure"
        )

        self.removed_object = PublishStatusableObject.objects.create(
            status = status.REMOVED.value,
            name="I contained something bad and had to be removed"
        )
                    
    def test_the_crazy_settings_format(self):
        """
        Does the crazy status settings format work?
        """
        status = settings.PUBLISHINGTOOLS_STATUS_CHOICE
        self.assertEquals(status.DRAFT.name, 'Draft')    
        self.assertTrue(status.PUBLISHED.publishable)    
        self.assertEquals(status.REMOVED.publishable, False)    
        self.assertEquals(status.DUMMY, {'value': 1, 'name': 'Dummy', 'publishable': False})
        
    def test_staging(self):
        """
        if it's a staging server, do all objects get returned?
        """
        self.settings.PUBLISHINGTOOLS_OVERRIDE_PUBLISH_STATUS = True
        self.assertEquals(PublishStatusableObject.objects.count(), 4)
        all_objects = PublishStatusableObject.objects.all().values_list('name', flat=True)
        self.assertEqual(list(all_objects), [
            u"A first draft",
            u"A test that should never get published",
            u"I'm ready for public exposure",
            u"I contained something bad and had to be removed"
        ])
        
        self.assertTrue(self.draft_object.is_live)


    def test_production(self):
        """
        if it's a production server, do only published objects get returned?
        """
        self.settings.PUBLISHINGTOOLS_OVERRIDE_PUBLISH_STATUS = False
        all_objects = PublishStatusableObject.objects.all().values_list('name', flat=True)
        self.assertEquals(PublishStatusableObject.objects.count(), 1)
        
