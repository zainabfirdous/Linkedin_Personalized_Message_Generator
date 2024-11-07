from django.db import models

class targetProfileDetails(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=300)
    profile_url = models.URLField(max_length=400)
    posts = models.JSONField(default=list)

    class Meta:
        db_table = 'targetProfileDetails'