from django.db import models

# Create your models here.
class Mobility(models.Model):
    date = models.TextField(blank=True, primary_key=True)
    mobility_recreation = models.FloatField(blank=True, null=True)
    mobility_grocery = models.FloatField(blank=True, null=True)
    mobility_parks = models.FloatField(blank=True, null=True)
    mobility_transit = models.FloatField(blank=True, null=True)
    mobility_work = models.FloatField(blank=True, null=True)
    mobility_residential = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mobility'