import email
from unittest.util import _MAX_LENGTH
from django.db import models

# makemigrations - create changes and store in a file 
# migrate - apply the pending changes created by makemigrations

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122,null=True)
    email = models.CharField(max_length=122,null=True)
    phone = models.CharField(max_length=12,null=True)
    desc = models.TextField(null=True)
    date = models.DateField(null=True)
    
    def __str__(self):
        return self.name
    
    
class EventAdvisor(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    destination = models.CharField(max_length=122)
    CUISINE_CHOICES = [
        ('IND', 'Indian'),
        ('CHN', 'Chinese'),
        ('ARB', 'Arabian'),
    ]
    PACKAGE_CHOICES = [
        ('BP', 'Basic Package :  ₹500 per 100 members.'),
        ('SP', 'Standard Package : ₹5,000 per 100 members.'),
        ('AP', 'Advanced Package : ₹10,000 per 100 members.'),
        ('PP', 'Premium Package : ₹1,000 to ₹50,000 per 100 members.'),
        ('EP', 'Enterprise Package : ₹5,000 to ₹200,000 or more per 100 members.'),
        ('LP', 'Lite Package : Typically free or up to ₹200 per 100 members.'),
        ('PPP', 'Pro Package : Priced at approximately ₹50 to ₹3,000 per 100 members.'),
        ('UP', 'Ultimate Package : Around ₹300 to ₹1,000 per 100 members.'),
        ('VP', 'VIP Package : ₹1,000 to ₹50,000 or more per 100 members.'),
    ]
    cuisine = models.CharField(max_length=10, choices=CUISINE_CHOICES, default='option1')
    package = models.CharField(max_length=10, choices=CUISINE_CHOICES, default='option1')
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    desc = models.TextField(max_length=500,null=True)
    guest = models.CharField(max_length=500,null=True)


    def __str__(self):
        return self.name

    
class CollegeEvent(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    destination = models.CharField(max_length=122)
    CUISINE_CHOICES = [
        ('IND', 'Indian'),
        ('CHN', 'Chinese'),
        ('ARB', 'Arabian'),
    ]
    PACKAGE_CHOICES = [
        ('BP', 'Basic Package :  ₹500 per 100 members.'),
        ('SP', 'Standard Package : ₹5,000 per 100 members.'),
        ('AP', 'Advanced Package : ₹10,000 per 100 members.'),
        ('PP', 'Premium Package : ₹1,000 to ₹50,000 per 100 members.'),
        ('EP', 'Enterprise Package : ₹5,000 to ₹200,000 or more per 100 members.'),
        ('LP', 'Lite Package : Typically free or up to ₹200 per 100 members.'),
        ('PPP', 'Pro Package : Priced at approximately ₹50 to ₹3,000 per 100 members.'),
        ('UP', 'Ultimate Package : Around ₹300 to ₹1,000 per 100 members.'),
        ('VP', 'VIP Package : ₹1,000 to ₹50,000 or more per 100 members.'),
    ]
    cuisine = models.CharField(max_length=10, choices=CUISINE_CHOICES, default='option1')
    package = models.CharField(max_length=10, choices=CUISINE_CHOICES, default='option1')
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    desc = models.TextField(max_length=500,null=True)
    guest = models.CharField(max_length=500,null=True)
    

    def __str__(self):
        return self.name

class PartiesEvent(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    destination = models.CharField(max_length=122)
    CUISINE_CHOICES = [
        ('IND', 'Indian'),
        ('CHN', 'Chinese'),
        ('ARB', 'Arabian'),
    ]
    PACKAGE_CHOICES = [
        ('BP', 'Basic Package :  ₹500 per 100 members.'),
        ('SP', 'Standard Package : ₹5,000 per 100 members.'),
        ('AP', 'Advanced Package : ₹10,000 per 100 members.'),
        ('PP', 'Premium Package : ₹1,000 to ₹50,000 per 100 members.'),
        ('EP', 'Enterprise Package : ₹5,000 to ₹200,000 or more per 100 members.'),
        ('LP', 'Lite Package : Typically free or up to ₹200 per 100 members.'),
        ('PPP', 'Pro Package : Priced at approximately ₹50 to ₹3,000 per 100 members.'),
        ('UP', 'Ultimate Package : Around ₹300 to ₹1,000 per 100 members.'),
        ('VP', 'VIP Package : ₹1,000 to ₹50,000 or more per 100 members.'),
    ]
    cuisine = models.CharField(max_length=10, choices=CUISINE_CHOICES, default='option1')
    package = models.CharField(max_length=10, choices=CUISINE_CHOICES, default='option1')
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    desc = models.TextField(max_length=500,null=True)
    guest = models.CharField(max_length=500,null=True)
    

    def __str__(self):
        return self.name

class WeddingEvent(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    destination = models.CharField(max_length=122)
    CUISINE_CHOICES = [
        ('IND', 'Indian'),
        ('CHN', 'Chinese'),
        ('ARB', 'Arabian'),
    ]
    PACKAGE_CHOICES = [
        ('BP', 'Basic Package :  ₹500 per 100 members.'),
        ('SP', 'Standard Package : ₹5,000 per 100 members.'),
        ('AP', 'Advanced Package : ₹10,000 per 100 members.'),
        ('PP', 'Premium Package : ₹1,000 to ₹50,000 per 100 members.'),
        ('EP', 'Enterprise Package : ₹5,000 to ₹200,000 or more per 100 members.'),
        ('LP', 'Lite Package : Typically free or up to ₹200 per 100 members.'),
        ('PPP', 'Pro Package : Priced at approximately ₹50 to ₹3,000 per 100 members.'),
        ('UP', 'Ultimate Package : Around ₹300 to ₹1,000 per 100 members.'),
        ('VP', 'VIP Package : ₹1,000 to ₹50,000 or more per 100 members.'),
    ]
    cuisine = models.CharField(max_length=10, choices=CUISINE_CHOICES, default='option1')
    package= models.CharField(max_length=10, choices=CUISINE_CHOICES, default='option1')
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    desc = models.TextField(max_length=500,null=True)
    guest = models.CharField(max_length=500,null=True)
    

    def __str__(self):
        return self.name

class TechnicalEvent(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    destination = models.CharField(max_length=122)
    CUISINE_CHOICES = [
        ('IND', 'Indian'),
        ('CHN', 'Chinese'),
        ('ARB', 'Arabian'),
    ]
    PACKAGE_CHOICES = [
        ('BP', 'Basic Package :  ₹500 per 100 members.'),
        ('SP', 'Standard Package : ₹5,000 per 100 members.'),
        ('AP', 'Advanced Package : ₹10,000 per 100 members.'),
        ('PP', 'Premium Package : ₹1,000 to ₹50,000 per 100 members.'),
        ('EP', 'Enterprise Package : ₹5,000 to ₹200,000 or more per 100 members.'),
        ('LP', 'Lite Package : Typically free or up to ₹200 per 100 members.'),
        ('PPP', 'Pro Package : Priced at approximately ₹50 to ₹3,000 per 100 members.'),
        ('UP', 'Ultimate Package : Around ₹300 to ₹1,000 per 100 members.'),
        ('VP', 'VIP Package : ₹1,000 to ₹50,000 or more per 100 members.'),
    ]
    cuisine = models.CharField(max_length=10, choices=CUISINE_CHOICES, default='option1')
    package = models.CharField(max_length=10, choices=CUISINE_CHOICES, default='option1')
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    desc = models.TextField(max_length=500,null=True)
    guest = models.CharField(max_length=500,null=True)
    

    def __str__(self):
        return self.name