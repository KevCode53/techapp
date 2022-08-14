# Imports Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Imports Models
from apps.core.models import BaseModel
from apps.users.models import Employee

# Import Utils
from utils.choices import OWNER_CHOICES, TYPE_EQUIPMENT_CHOICES

# Create your models here.

class Equipement(BaseModel):
  """Model definition for Equipement."""

  # TODO: Define fields here
  owner = models.CharField(_('Propietario'), max_length=50, choices=OWNER_CHOICES, default='MP')
  year = models.CharField(_('Año'), max_length=4)
  code = models.CharField(_('Codigo'), max_length=8)
  correlative = models.CharField(_('Correlativo'), max_length=6)
  user = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name=_('Usuario Responsable'))

  class Meta:
    """Meta definition for Equipement."""

    verbose_name = _('Equipo')
    verbose_name_plural = _('Equipos')

  def __str__(self):
    """Unicode representation of Equipment."""
    return '%s %s' % (self.description, self.get_inventary())

  def save(self, *args, **kwargs):
    """Save method for Equipement."""
    self.description = self.description.upper()
    super(Equipment, self).save(*args, **kwargs)

  # TODO: Define custom methods here

  def get_inventary(self):
    """Return inventary of equipment."""
    return '%s-%s-%s-%s' % (self.owner, self.year, self.code, self.correlative)
