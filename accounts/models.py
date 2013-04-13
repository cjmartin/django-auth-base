from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class UserProfile(models.Model):
    # This field is required.
    user = models.OneToOneField(User)

    # Flickr
    flickr_nsid = models.CharField(max_length=255, null=True, blank=True)
    flickr_username = models.CharField(max_length=255, null=True, blank=True)
    flickr_fullname = models.CharField(max_length=255, null=True, blank=True)
    flickr_oauth_token = models.CharField(max_length=255, null=True, blank=True)
    flickr_oauth_token_secret = models.CharField(max_length=255, null=True, blank=True)
    
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.user.username
        
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        
post_save.connect(create_user_profile, sender=User)
