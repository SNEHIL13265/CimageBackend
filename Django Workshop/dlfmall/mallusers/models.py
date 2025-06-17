from django.db import models

class userDetails(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(primary_key=True)
    mobile = models.IntegerField(unique=True)
    password = models.CharField(max_length=20)
    address = models.CharField(max_length=100)

membershipName = (
    ("silver", "silver"),
    ("Gold", "Gold",),
    ("Platinum", "Platinum")
)    

class membershipDetails(models.Model):
    membershipCategory = models.CharField(max_length=20, choices=membershipName)
    membershipId = models.AutoField(primary_key=True)
    email = models.ForeignKey(userDetails, on_delete= models.CASCADE)
    Validity = models.DateField()

class eventDetails(models.Model):
    eventid =models.AutoField(primary_key=True)
    eventName = models.CharField(max_length=50,unique=True)
    eventdescription= models.CharField(max_length=100)
    eventdate = models.DateField()
    eventvenue =  models.CharField(max_length=50)

class registrationDelails(models.Model):
    registrationId = models.AutoField(primary_key=True)
    eventId =models.ForeignKey(eventDetails,on_delete=models.CASCADE)
    email =models.ForeignKey(userDetails,on_delete=models.CASCADE)
    






9