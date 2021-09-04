from django.db import models
import datetime

# Create your models here.
class Job(models.Model):
    name = models.CharField(max_length=255)
    comapny = models.CharField(max_length=255)
    short_description = models.CharField(max_length=500)
    description = models.TextField(null=True, blank=True)
    vacancy = models.IntegerField(null=True, blank=True)
    last_date = models.DateField()
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    date_modified = models.DateTimeField(auto_now=True, blank=True)


    def __str__(self):
        return self.name + " at " + self.comapny

    def to_json(self):
            return {
                'id': self.id,
                'name': self.name,
                'description': self.description,
                'short_description': self.short_description,
                'vacancy': self.vacancy,
                'comapny': self.comapny,
                'last_date': self.last_date,
                'date_created': self.date_created,
                'date_modified': self.date_modified
            }
   