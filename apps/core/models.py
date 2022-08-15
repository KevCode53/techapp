# Imports Django
from django.db import models

# Imports Third Party
from simple_history.models import HistoricalRecords

# Create your models here.

class BaseModel(models.Model):
  """Model definition for BaseModel."""

  # TODO: Define fields here
  id = models.AutoField(primary_key=True)
  state = models.BooleanField('Estado', default=True)
  created_date = models.DateField('Fecha de Creación', auto_now=False, auto_now_add=True)
  modified_date = models.DateField('Fecha de Modificación', auto_now=True, auto_now_add=False)
  deleted_date = models.DateField('Fecha de Eliminacion', auto_now=True, auto_now_add=False)

  class Meta:
    """Meta definition for BaseModel."""

    abstract = True
    verbose_name = 'BaseModel'
    verbose_name_plural = 'BaseModels'

  def __str__(self):
    """Unicode representation of BaseModel."""

  # TODO: Define custom methods here

class Department(BaseModel):
  """Model definition for Department."""

  # TODO: Define fields here
  id = models.CharField('Código', primary_key=True, max_length=2, unique=True)
  name = models.CharField('Nombre', max_length=150, unique=True)
  historical = HistoricalRecords()

  @property
  def _history_user(self):
    return self.change_by

  @_history_user.setter
  def _history_user(self, value):
    self.change_by = value

  class Meta:
    """Meta definition for Department."""

    # unique_together = (('code', 'name'),)
    verbose_name = 'Department'
    verbose_name_plural = 'Departments'

  def __str__(self):
    """Unicode representation of Department."""
    return '%s %s' % (self.id, self.name)

  def save(self, *args, **kwargs):
    """Save method for Equipement."""
    self.name = self.name.upper()
    super(Department, self).save(*args, **kwargs)

  # TODO: Define custom methods here
