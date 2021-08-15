from django.contrib.postgres.fields import ArrayField
from django.db import models
from users.models import User, user_type
from startups.models import Startup

# Create your models here.
class Investor(models.Model):
    user = models.OneToOneField(user_type, on_delete=models.CASCADE, primary_key=True)
    registered_business = models.BooleanField(default=False)
    interests = ArrayField(models.CharField(max_length=200), blank=True)
    verified = models.BooleanField(default=False)
    name = models.CharField(max_length=300, default="Investor")
    profile_pic = models.ImageField(upload_to=f'investors/profile_pics', null=True)
    detail = models.TextField(null=True)

    def __str__(self):
        return self.user.user.email


class Investment(models.Model):
    investor = models.ForeignKey(Investor, on_delete=models.CASCADE)
    startup = models.ForeignKey(Startup, on_delete=models.CASCADE)
    amount = models.FloatField()