from django.conf import settings

class dotdict(dict):
    def __getattr__(self, attr):
        return self.get(attr, None)
    __setattr__= dict.__setitem__
    __delattr__= dict.__delitem__

class dotdict_from_dicttuple(dict):
    def __getattr__(self, attr):
        setting_tuple = self.get(attr, None)
        try:
            return dotdict({
                'value': self.get(attr, None)[0],
                'name': self.get(attr, None)[1],
                'publishable': self.get(attr, None)[2],
            })
        except KeyError:
            return None
        except TypeError:
            return None
    __setattr__= dict.__setitem__
    __delattr__= dict.__delitem__

# TO DO: allow for folks who want specify STATUS_CHOICES as a dictionary of tuples
# TO DO: allow for folks who want specify STATUS_CHOICES as a tuple of tuples

DEFAULT_STATUS_CHOICES = {
    'DRAFT': (0, 'Draft', False),
    'DUMMY': (1, 'Dummy', False),
    'PUBLISHED': (2, 'Published', True),
    'REMOVED': (3, 'Removed', False),
}

if not hasattr(settings, 'PUBLISHINGTOOLS_OVERRIDE_PUBLISH_STATUS'):
    settings.PUBLISHINGTOOLS_OVERRIDE_PUBLISH_STATUS = True
    
if not hasattr(settings, 'PUBLISHINGTOOLS_STATUS_CHOICE'):
    settings.PUBLISHINGTOOLS_STATUS_CHOICE = dotdict_from_dicttuple(DEFAULT_STATUS_CHOICES)
    
settings.PUBLISHINGTOOLS_STATUS_CHOICES = [x[0:2] for x in settings.PUBLISHINGTOOLS_STATUS_CHOICE.itervalues()]