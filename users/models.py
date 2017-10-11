from __future__ import unicode_literals

from django.db import models

# Create your models here.


class GitUsers(models.Model):
    login = models.CharField(max_length=200, blank=True, null=True)
    userid = models.IntegerField()
    avatar_url = models.URLField(max_length=200)
    gravatar_id = models.CharField(max_length=200, blank=True, null=True)
    url = models.URLField(max_length=200, blank=True, null=True)
    html_url = models.URLField(max_length=200, blank=True, null=True)
    followers_url = models.URLField(max_length=200, blank=True, null=True)
    following_url = models.URLField(max_length=200, blank=True, null=True)
    gists_url = models.URLField(max_length=200, blank=True, null=True)
    starred_url = models.URLField(max_length=200, blank=True, null=True)
    subscriptions_url = models.URLField(max_length=200, blank=True, null=True)
    organizations_url = models.URLField(max_length=200, blank=True, null=True)
    repos_url = models.URLField(max_length=200, blank=True, null=True)
    events_url = models.URLField(max_length=200, blank=True, null=True)
    received_events_url = models.URLField(max_length=200, blank=True, null=True)
    acctype = models.CharField(max_length=200, blank=True, null=True)
    site_admin = models.BooleanField()
    name = models.CharField(max_length=20, blank=True, null=True)
    company = models.CharField(max_length=30, blank=True, null=True)
    blog = models.CharField(max_length=30, blank=True, null=True)
    location = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    hireable = models.BooleanField()
    bio = models.CharField(max_length=2000, blank=True, null=True)
    public_repos = models.IntegerField()
    public_gists = models.IntegerField()
    followers = models.IntegerField()
    following = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta(object):
        unique_together = ('login',)
