from __future__ import unicode_literals

# Create your models here.
from django.db import models


class Disease(models.Model):
    name = models.CharField(max_length=200, blank=False, primary_key=True)
    desc = models.CharField(max_length=500)

    def __str__(self):
        return str(self.name)


class ARule(models.Model):
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=500)
    support = models.FloatField(blank=False)
    confidence = models.FloatField(blank=False)
    found_date = models.DateTimeField(auto_now_add=True)
    current_diseases = models.ManyToManyField(Disease, related_name='current_diseases')
    expected_diseases = models.ManyToManyField(Disease, related_name='expected_diseases')

    def __str__(self):
        return ', '.join([disease.name for disease in self.current_diseases.all()]) + '->' + ', '.join(
            [disease.name for disease in self.expected_diseases.all()])

