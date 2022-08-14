# Import Django
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _

# Import Models
from apps.core.models import BaseModel

# Import Utils
from .manager import UserManager

# Import Third Apps
from simple_history.models import HistoricalRecords

# Create your models here.

class EmployeeBase(BaseModel):
  """Model definition for EmployeeBase."""

  # TODO: Define fields here
  nip = models.CharField('NIP', max_length=8, unique=True)
  name = models.CharField('Name', max_length=50)
  phone = models.CharField('Phone', max_length=9, blank=True, null=True)

  class Meta:
    """Meta definition for EmployeeBase."""

    abstract = True
    verbose_name = 'EmployeeBase'
    verbose_name_plural = 'EmployeeBases'

class Employee(EmployeeBase):
  """Model definition for Employee."""

  # TODO: Define fields here

  class Meta:
    """Meta definition for Employee."""

    verbose_name = _('Empleado')
    verbose_name_plural = _('Empleados')

  def __str__(self):
    """Unicode representation of Employee."""
    return '%s - %s' % (self.nip, self.name)

  def save(self, *args, **kwargs):
    """Save method for Equipement."""
    self.name = self.name.upper()
    super(Employee, self).save(*args, **kwargs)

  # TODO: Define custom methods here


class User(AbstractBaseUser, PermissionsMixin, EmployeeBase):
  username = models.CharField(max_length=150, validators=[UnicodeUsernameValidator], unique=True)
  email = models.EmailField('Correo Electronico', max_length=150, unique=True)
  name = models.CharField(max_length=150, blank=True, null=True)
  last_name = models.CharField(max_length=150, blank=True, null=True)
  image = models.ImageField(upload_to='profile/images', blank=True, null=True)

  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=False)
  historical = HistoricalRecords()

  objects = UserManager()

  class Meta:
    verbose_name = 'Usuario'
    verbose_name_plural = 'Usuarios'

  USERNAME_FIELD = 'username'
  REQUIRED_FIELDS = ['email', 'name', 'last_name', 'nip']

  def natural_key(self):
    return self.username

  def __str__(self):
    return f'{self.name} {self.last_name}'