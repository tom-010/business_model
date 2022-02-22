from django.db import models
from helper.with_dates_and_version import WithDates

class Project(WithDates, models.Model):
    name = models.CharField(max_length=256)


    @property
    def business_model_canvases(self):
        pass

    @property
    def stories(self):
        pass


class CustomerSegment(WithDates, models.Model):
    name = models.CharField(max_length=256)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True)