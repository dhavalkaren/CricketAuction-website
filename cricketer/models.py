from django.db import models

# Create your models here.
class cricketer(models.Model):
    BOWLER = 'BOWLER'
    BATSMAN='BATSMAN'
    ALL_ROUNDER='ALL_ROUNDER'
    cricketer_type=((BOWLER,'BOWLER'),(BATSMAN,'BATSMAN'),(ALL_ROUNDER,'ALL_ROUNDER'))
    type = models.CharField(choices=cricketer_type,default=BATSMAN,max_length=100)
    
    cricketer_name = models.CharField(max_length=100)
    matches = models.IntegerField(default=0)
    runs = models.IntegerField(default=0)
    highest = models.IntegerField(default=0)
    average = models.FloatField(default=0.0)
    strike_rate = models.FloatField(default=0.0)
    hundreds = models.IntegerField(default=0)
    fifeties = models.IntegerField(default=0)
    wickets = models.IntegerField(default=0)
    economy = models.FloatField(default=0.0)
    bid = models.IntegerField(default=5000000)
    image = models.ImageField(default='cricketer.jpg',upload_to='cricketer_pic')
    def __str__(self):
        return self.cricketer_name

class MI(models.Model):
    cricketer_name = models.CharField(max_length=100)
    bid = models.IntegerField(default=0)
    image = models.ImageField(default='cricketer.jpg',upload_to='cricketer_pic')
    def __str__(self):
        return self.cricketer_name

class RCB(models.Model):
    cricketer_name = models.CharField(max_length=100)
    bid = models.IntegerField(default=0)
    image = models.ImageField(default='cricketer.jpg',upload_to='cricketer_pic')
    def __str__(self):
        return self.cricketer_name

class CSK(models.Model):
    cricketer_name = models.CharField(max_length=100)
    bid = models.IntegerField(default=0)
    image = models.ImageField(default='cricketer.jpg',upload_to='cricketer_pic')
    def __str__(self):
        return self.cricketer_name

class KKR(models.Model):
    cricketer_name = models.CharField(max_length=100)
    bid = models.IntegerField(default=0)
    image = models.ImageField(default='cricketer.jpg',upload_to='cricketer_pic')
    def __str__(self):
        return self.cricketer_name

class KXIP(models.Model):
    cricketer_name = models.CharField(max_length=100)
    bid = models.IntegerField(default=0)
    image = models.ImageField(default='cricketer.jpg',upload_to='cricketer_pic')
    def __str__(self):
        return self.cricketer_name

class DC(models.Model):
    cricketer_name = models.CharField(max_length=100)
    bid = models.IntegerField(default=0)
    image = models.ImageField(default='cricketer.jpg',upload_to='cricketer_pic')
    def __str__(self):
        return self.cricketer_name

class RR(models.Model):
    cricketer_name = models.CharField(max_length=100)
    bid = models.IntegerField(default=0)
    image = models.ImageField(default='cricketer.jpg',upload_to='cricketer_pic')
    def __str__(self):
        return self.cricketer_name

class SRH(models.Model):
    cricketer_name = models.CharField(max_length=100)
    bid = models.IntegerField(default=0)
    image = models.ImageField(default='cricketer.jpg',upload_to='cricketer_pic')
    def __str__(self):
        return self.cricketer_name