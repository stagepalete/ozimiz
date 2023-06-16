from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(self, username,  fname, lname, phone_number, gender, birth_date, telegram, email, password=None):
        '''Creates default user'''
        if not username:
            raise ValueError('Username is required')
        email = self.normalize_email(email)
        username = AbstractBaseUser.normalize_username(username)
        user = self.model(username = username, fname = fname, lname = lname, phone_number = phone_number, gender = gender, birth_date = birth_date, telegram = telegram, email = email)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username,  fname, lname, phone_number, gender, birth_date, telegram, email, password):
        '''Creates superuser'''
        user = self.create_user(username,  fname, lname, phone_number, gender, birth_date, telegram, email, password)
        user.is_superuser = True
        user.is_staff = True

        user.save(using = self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True, verbose_name='username')
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    ava = models.CharField(max_length=255, null=False, blank=True)
    phone_number = models.CharField(max_length=11, unique=True)

    MALE = "M"
    FEMALE = "F"
    GENDER_CHOICES = (
        (MALE, "Male"),
        (FEMALE, "Female")
    )
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default="M")

    birth_date = models.DateField()
    telegram = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['fname', 'lname', 'phone_number', 'gender', 'birth_date', 'telegram', 'email']
    
    def __str__(self):
        return self.username
    
    def get_full_name(self):
        return f'{self.fname} {self.lname}'

    def get_short_name(self):
        return self.fname

    def get_email(self):
        return self.email
     