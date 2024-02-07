from django.db import models 

class Proxy(models.Model):
    ip_address = models.CharField(max_length=100)
    port = models.IntegerField(default=0)
    country = models.CharField(max_length=100)
    protocol = models.CharField(max_length=100) 
    anonymity = models.CharField(max_length=100)
    speed = models.FloatField(default=0)
    uptime = models.FloatField(default=0)
    last_check = models.CharField(max_length=100)
    response = models.FloatField(default=0)
    latency = models.FloatField(default=0)
    org_and_asn = models.CharField(max_length=100)

class CountriesOnline(models.Model):
    count = models.IntegerField(default=0)
    last_update = models.CharField(max_length=100)