from django.db import models
from django.contrib.auth.models import Group, User
from django.db.models.signals import post_save
# Create your models here.

class Olympiad(models.Model):
    title = models.CharField(max_length=1000)
    start = models.DateTimeField(blank=True, null=True)
    stop = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

class Contest(models.Model):
    title = models.CharField(max_length=1000)
    olympiad = models.ForeignKey(Olympiad)
    start = models.DateTimeField()
    stop = models.DateTimeField()
    admin_group = models.ForeignKey(Group, blank=True, null=True, related_name='admin_contests')
    participants_group = models.ForeignKey(Group, blank=True, null=True, related_name='contests')

    def __str__(self):
        return '{}: {}'.format(self.olympiad, self.title)

def create_group(sender, instance, *args, **kwargs):
        if kwargs['created']:
            group = Group(name=instance.title)
            group.save()
            instance.participants_group = group

            admin_group = Group(name='{}_admin'.format(instance.title))
            admin_group.save()

            instance.participants_group = group
            instance.admin_group = admin_group
            instance.save()

post_save.connect(create_group, sender=Contest)