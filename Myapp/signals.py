from django.db.models.signals import post_save , pre_save
from django.dispatch import receiver
from .models import *

@receiver(post_save, sender=User)
def post_save_receiver(created , sender, instance, **kwargs):
    print(created)
    if created:
        UserProfile.objects.create(user=instance)    
    else:
        try:
            Profile = UserProfile.objects.get(user=instance)
            Profile.save()
        except:
            UserProfile.objects.create(user=instance)
            print('User Profile is been created')

        print('user is updated')
@receiver(pre_save , sender= User)
def pre_save_signal(sender , instance , **kwargs):
    print(instance.username, 'This user is been saved')

# def post_save_create_profile_receiver():
#     post_save.connect(post_save_create_profile_receiver , sender= User)
