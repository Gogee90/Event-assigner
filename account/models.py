from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    pass

    verbose_name = 'User'
    verbose_name_plural = 'Users'

    def __str__(self):
        return f'{self.username} {self.email}'

    @property
    def events(self):
        return self.event_set.all()
