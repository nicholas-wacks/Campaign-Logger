from django.db import models
from users.models import User

class Campaign(models.Model):
    Name = models.TextField(default='')
    Users = models.ManyToManyField(User)

    def __str__(self):
        return self.Name

    class Meta:
        ordering = ('id',)