from django.db import models
from django.contrib.auth.models import BaseUserManager
from core.user.models import MyUser

class TeacherManager(BaseUserManager):
    def create_user(self, username, email, password=None, **kwargs):
        if not username:
            raise ValueError('Teachers must have a username!')
        if not email:
            raise ValueError('Teachers must have an email!')
        if not password:
            raise ValueError('Teachers must have a password!')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            **kwargs,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

class Teacher(MyUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    bio = models.TextField(null=True, blank=True)

    objects = TeacherManager()

    def __str__(self):
        return f'{self.username}'

class BankInfo(models.Model):
    card_number = models.IntegerField()
    expiration_date = models.CharField(max_length=5)
    cvv_code = models.IntegerField()
    user = models.OneToOneField(Teacher, on_delete=models.CASCADE)
