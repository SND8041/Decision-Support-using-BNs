from django.contrib.auth.models import User
from django.db import models

# Create A User Profile Model
class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username