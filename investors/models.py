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

    def __str__(self):
        return User.get_email(self.user)


class Investment(models.Model):
    investor = models.ForeignKey(Investor, on_delete=models.CASCADE)
    startup = models.ForeignKey(Startup, on_delete=models.CASCADE)
    amount = models.FloatField()