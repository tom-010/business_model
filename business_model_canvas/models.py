from django.db import models

class WithDates(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class BusinessModelCanvas(WithDates, models.Model):

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

    version = models.IntegerField(default=1)

    previous = models.ForeignKey('BusinessModelCanvas', null=True, blank=True, on_delete=models.SET_NULL)

    def create_new_version(self):
        return BusinessModelCanvas.objects.create(
            name=self.name,
            one_sentence=self.one_sentence,
            key_partners=self.key_partners,
            key_activies=self.key_activies,
            key_resources=self.key_resources,
            value_propositions=self.value_propositions,
            customer_relationships=self.customer_relationships,
            channels=self.channels,
            customer_segments=self.customer_segments,
            cost_structure=self.cost_structure,
            revenue_streams=self.revenue_streams,
            version=self.version+1,
            previous=self,
        )
