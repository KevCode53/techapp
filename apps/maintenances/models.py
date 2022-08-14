# Imports for Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Imports Models
from apps.core.models import BaseModel
from apps.users.models import User, Employee
from apps.equipments.models import Equipement
from apps.ubications.models import Ubication

# Create your models here.

class Compromise(BaseModel):
  """Model definition for Compromise."""

  # TODO: Define fields here
  user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('Usuario'))
  year = models.SmallIntegerField(_('Año'))
  estimated_computers = models.PositiveSmallIntegerField(_('Computadoras Estimadas'), default=0)
  total_computers = models.PositiveSmallIntegerField(_('Computadoras Totales'), default=0)
  ubications = models.ManyToManyField(Ubication, verbose_name=_('Fiscalias'))

  class Meta:
    """Meta definition for Compromise."""

    unique_together = ('user', 'year')
    verbose_name = 'Compromiso'
    verbose_name_plural = 'Compromisos'

  def __str__(self):
    """Unicode representation of Compromise."""
    pass

  def save(self):
    """Save method for Compromise."""
    pass

  def get_absolute_url(self):
    """Return absolute url for Compromise."""
    return ('')

  # TODO: Define custom methods here


class Maintenance(BaseModel):
  """Model definition for Maintenance."""

  # TODO: Define fields here
  user = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name=_('Usuario Responsable'))
  technical = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('Técnico'))
  cpu = models.ForeignKey(Equipement, on_delete=models.CASCADE, verbose_name=_('CPU'), related_name=_('cpu'))
  printer = models.ForeignKey(Equipement, on_delete=models.CASCADE, verbose_name=_('Impresora'), related_name=_('printer'))
  monitor = models.ForeignKey(Equipement, on_delete=models.CASCADE, verbose_name=_('Monitor'), related_name=_('monitor'))
  keyboard = models.ForeignKey(Equipement, on_delete=models.CASCADE, verbose_name=_('Teclado'), related_name=_('keyboard'))
  mouse = models.ForeignKey(Equipement, on_delete=models.CASCADE, verbose_name=_('Mouse'), related_name=_('mouse'))
  scanner = models.ForeignKey(Equipement, on_delete=models.CASCADE, verbose_name=_('Escanér'), related_name=_('scanner'))
  speakers = models.ForeignKey(Equipement, on_delete=models.CASCADE, verbose_name=_('Bocinas'), related_name=_('speakers'))
  figer_printer = models.ForeignKey(Equipement, on_delete=models.CASCADE, verbose_name=_('Lector de Huellas'), related_name=_('finger_printer'))
  ups = models.ForeignKey(Equipement, on_delete=models.CASCADE, verbose_name=_('Bateria UPS'), related_name=_('ups'))
  phone_ip = models.ForeignKey(Equipement, on_delete=models.CASCADE, verbose_name=_('Telefono IP'), related_name=_('phone_ip'))
  webcam = models.ForeignKey(Equipement, on_delete=models.CASCADE, verbose_name=_('Camára Web'), related_name=_('webcam'))
  hard_disk = models.ForeignKey(Equipement, on_delete=models.CASCADE, verbose_name=_('Disco Duro'), related_name=_('hard_disk'))


  class Meta:
    """Meta definition for Maintenance."""

    verbose_name = 'Mantenimiento'
    verbose_name_plural = 'Mantenimientos'

  def __str__(self):
    """Unicode representation of Maintenance."""
    return '%s' % (self.user)

  # TODO: Define custom methods here
