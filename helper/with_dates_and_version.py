from django.db import models
from save_deep import save_deep

class WithDates(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-updated_at']


class WithDatesAndVersion(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    version = models.IntegerField(default=1)

    class Meta:
        abstract = True
        ordering = ['-updated_at']

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
