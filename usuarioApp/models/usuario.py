from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a user with the given username and password.
        """
        if not email:
            raise ValueError('Los usuarios deben tener un email')
        user = self.model(username=email)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given username and password.
        """
        user = self.create_user(
            username=email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    #id = models.BigAutoField(primary_key=True)
    nombres = models.CharField('Nombres', max_length=50, null=False, default="Sin nombres")
    apellidos = models.CharField('Apellidos', max_length=50, null=False, default="Sin apellidos")
    ciudad = models.CharField('Ciudad', max_length=50, null=False, default="Sin ciudad")
    password = models.CharField('Password', max_length = 256, null=False, default="Sin password")
    departamento = models.CharField('Departamento', max_length=50, null=False, default="Sin departamento")
    direccion = models.CharField('Direccion', max_length=50, null=False, default="Sin direccion")
    email = models.EmailField('Email', max_length =100, unique=True, null=False, default="Sin email")
    telefono = models.CharField('Telefono', max_length=50, null=True, default="Sin telefono")
    es_admin = models.BooleanField('EsAdmin', default=False)
    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)

    objects = UserManager()
    USERNAME_FIELD = 'email'