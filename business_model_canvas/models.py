from django.db import models
from save_deep import save_deep

class WithDatesAndVersion(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    version = models.IntegerField(default=1)

    class Meta:
        abstract = True

    def create_new_version(self):
        new_version = self.__class__()
        for field in self._meta.fields:
            name = field.name
            setattr(new_version, name, getattr(self, name))
        new_version.pk = None
        new_version.created_at = None
        new_version.updated_at = None
        
        if(hasattr(new_version, 'previous')):
            new_version.previous = self

        version = self.version
        if not version:
            version = 0
        new_version.version = version + 1
        return save_deep(new_version)


class BusinessModelCanvas(WithDatesAndVersion, models.Model):
    previous = models.ForeignKey('BusinessModelCanvas', null=True, blank=True, on_delete=models.SET_NULL)

    name = models.CharField(max_length=256, null=True, blank=True)

    one_sentence = models.TextField(default='', blank=True)

    key_partners = models.TextField(default='', blank=True)
    key_activies = models.TextField(default='', blank=True)
    key_resources = models.TextField(default='', blank=True)
    value_propositions = models.TextField(default='', blank=True)
    customer_relationships = models.TextField(default='', blank=True)
    channels = models.TextField(default='', blank=True)
    customer_segments = models.TextField(default='', blank=True)
    cost_structure = models.TextField(default='', blank=True)
    revenue_streams = models.TextField(default='', blank=True)

    

    @staticmethod
    def example():
        return BusinessModelCanvas(
            name='the name',
            one_sentence='the one_sentence',
            key_partners='the key_partners',
            key_activies='the key_activies',
            key_resources='the key_resources',
            value_propositions='the value_propositions',
            customer_relationships='the customer_relationships',
            channels='the channels',
            customer_segments='the customer_segments',
            cost_structure='the cost_structure',
            revenue_streams='the revenue_streams'
        )

    
