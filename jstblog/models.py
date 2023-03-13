from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone=models.CharField(blank=True,max_length=11)
    city=models.CharField(blank=True,max_length=20)
    address=models.CharField(blank=True,max_length=100)
    image=models.ImageField(upload_to="Profile/",blank=True,null=True)
    dob=models.DateField(blank=True,null=True)

    def __str__(self):
        return '{}'.format(self.user)
    
    
    
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        print(instance.is_active)



@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()