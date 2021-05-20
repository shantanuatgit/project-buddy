from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#class DeveloperProfile(models.Model):

class AllProfile(models.Model):
        name=models.CharField(max_length=200)
        email=models.CharField(max_length=225)
        user=models.ForeignKey(User,on_delete=models.CASCADE)
        profile_pic=models.ImageField(upload_to='profileImage/')
        react=models.CharField(max_length=50,blank=True)
        angular=models.CharField(max_length=50,blank=True)
        vuejs=models.CharField(max_length=50,blank=True)
        bootstrap=models.CharField(max_length=50,blank=True)
        css=models.CharField(max_length=50,blank=True)
        django=models.CharField(max_length=50,blank=True)
        javascript=models.CharField(max_length=50,blank=True)
        php=models.CharField(max_length=50,blank=True)
        nodejs=models.CharField(max_length=50,blank=True)
        flask=models.CharField(max_length=50,blank=True)


        website_url=models.CharField(max_length=200, blank=True)
        Git_Hub_Url=models.CharField(max_length=200, blank=True)
        LinkedIn_Url=models.CharField(max_length=200,blank=True)
        facebook_url=models.CharField(max_length=200, blank=True)
        instagram_url=models.CharField(max_length=200, blank=True)


class Skill(models.Model):
    profile=models.ForeignKey(AllProfile, on_delete=models.CASCADE)
    skills=models.CharField(max_length=225)

class Test(models.Model):
    field=models.CharField(max_length=20)

class Member( models.Model ):

    model_categories = models.CharField(
            max_length = 255,
            null = True,
            blank = True )


class Invitation(models.Model):
    invitee=models.ForeignKey(User, on_delete=models.CASCADE)
    inviter=models.ForeignKey(AllProfile, on_delete=models.CASCADE, null=True)


class Response(models.Model):
    sender=models.ForeignKey(User, on_delete=models.CASCADE)
    accepter=models.ForeignKey(AllProfile, on_delete=models.CASCADE)
