from django.db import models
from helper.with_dates_and_version import WithDatesAndVersion

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
