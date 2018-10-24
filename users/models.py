from django.contrib.auth.models import AbstractUser

# Per official Django docs, following suggestion to make a custom user type in case of future needs
# For more details, see: https://docs.djangoproject.com/en/2.0/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project
class User(AbstractUser):
    def __str__(self):
        return self.username