from django.db import models
import datetime

# Create your models here.
class Report(models.Model):
    location = models.CharField(max_length=96)
    description = models.CharField(max_length=200)
    date = models.DateField(("Date"))
    time =models.TimeField(auto_now=True, auto_now_add=False)
    Incident_location = models.CharField(max_length=216)
    Intial_Serverity = models.CharField(max_length=500)
    suspect_cause = models.CharField(max_length=116)
    immediaet_action = models.CharField(max_length=116)
    sub_incident_type = models.CharField(max_length=116)