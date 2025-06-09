from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Custom user manager
class UserManager(BaseUserManager):
    def create_user(self,first_name, last_name,surname, email, raw_password, role=0):
       if not email:
          raise ValueError("The Email Field must be set")
       user=self.model(
            first_name=first_name,
            last_name=last_name,
            surname=surname,
            email=self.normalize_email(email),
            role=role
        )
       user.set_password(raw_password)  # This handles hashing
       user.save(using=self._db)
       return user
    def create_superuser(self,first_name,last_name,surname,email,raw_password,role=1):
        if not email:
            raise ValueError("The Email must be set")
        user=self.create_user(
            first_name=first_name,
            last_name=last_name,
            surname=surname,
            email=self.normalize_email(email),
            raw_password=raw_password,
            role=role
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
   

# Custom user model
class Users(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = (
        (0, 'Student'),
        (1, 'Faculty'),
    )
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    surname = models.CharField(max_length=50, blank=True)
    email = models.EmailField(unique=True)
    role = models.IntegerField(choices=ROLE_CHOICES,default=0)  # 0 for user, 1 for admin
    date_created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name','surname']
    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.surname} ({self.email})"

   
