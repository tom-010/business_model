from pyexpat import model
from django.db import models
import matplotlib.pyplot as plt

class WithDates(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class BusinessModelCanvas(WithDates, models.Model):

    name = models.CharField(max_length=256, null=True, blank=True)

    key_partners = models.TextField(default='', blank=True)
    key_activies = models.TextField(default='', blank=True)
    key_resources = models.TextField(default='', blank=True)
    value_propositions = models.TextField(default='', blank=True)
    customer_relationships = models.TextField(default='', blank=True)
    channels = models.TextField(default='', blank=True)
    customer_segments = models.TextField(default='', blank=True)
    cost_structure = models.TextField(default='', blank=True)
    revenue_streams = models.TextField(default='', blank=True)

    previous = models.ForeignKey('BusinessModelCanvas', null=True, blank=True, on_delete=models.SET_NULL)