from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class Post(models.Model):

    # auto_now_add sets value of timestamp_posted to be time of creation
    timestamp_posted = models.DateTimeField(auto_now_add=True)

    # auto_now sets value of timestamp_edited to be the time of edit
    # (anytime post.save() is called)
    timestamp_edited = models.DateTimeField(auto_now=True)

    # published content
    posted_text = models.TextField()

    # snapshot of most recent edit of a post (not necessarily published)
    edited_text = models.TextField()

    # assumption: one author per post (else switch to ManyToManyRelationship)
    author = models.ForeignKey('auth.User',
                               related_name='posts',
                               on_delete=models.CASCADE)

    private = models.BooleanField(default=False)

    def __str__(self):
        return "Post by {} on {}".format(self.author, self.timestamp_posted)
