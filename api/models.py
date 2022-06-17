from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):

    def __repr__(self):
        return f"<User username={self.username} pk={self.pk}>"

    def __str__(self):
        return self.username
