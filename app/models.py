from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class Game(models.Model):
    code = models.CharField(max_length=250)
    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='creator')
    opponent = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='opponent', null=True)
    creator_role = models.CharField(max_length=250, blank=True)
    opponent_role = models.CharField(max_length=250, blank=True)
    winner = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='winner', null=True)
    is_over = models.IntegerField(default=0)
    has_started = models.IntegerField(default=0)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.IntegerField(null=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    ip = models.CharField(null=True, max_length=255)
    email_confirmed = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def name(self):
        return self.user.first_name + ' ' + self.user.last_name

    @receiver(post_save, sender=User)
    def update_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()
