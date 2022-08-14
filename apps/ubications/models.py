# From Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Import Models
from apps.core.models import BaseModel, Department

# Imports Third Party
from simple_history.models import HistoricalRecords

# Create your models here.

class Ubication(BaseModel):
  """Model definition for Ubication."""

  # TODO: Define fields here
  code = models.CharField('Código', max_length=6)
  name = models.CharField(_('Nombre'), max_length=100)
  address = models.CharField(_('Address'), max_length=100, blank=True, null=True)
  phone = models.CharField(_('phone'), max_length=100, blank=True, null=True)
  department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name=_('Departamento'))
  estimated_computers = models.PositiveSmallIntegerField(_('Estimated Computers'), default=0)
  historical = HistoricalRecords()

  @property
  def _history_user(self):
    return self.change_by

  @_history_user.setter
  def _history_user(self, value):
    self.change_by = value

  class Meta:
    """Meta definition for Ubication."""

    verbose_name = 'Fiscalía'
    verbose_name_plural = 'Fiscalías'

  def __str__(self):
    """Unicode representation of Ubication."""
    return '%s' % (self.name)

  def save(self, *args, **kwargs):
    """Save method for Equipement."""
    self.name = self.name.upper()
    super(Ubication, self).save(*args, **kwargs)

  # TODO: Define custom methods here
