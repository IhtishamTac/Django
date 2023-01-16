from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.

class JenisSekolah(models.TextChoices):
        SMK = 'SMK', _('Sekolah Menengan Kejuruan')
        SMA = 'SMA', _('Sekolah Menengan Atas')
        UNIVERSITAS = 'UNIV', _('Universitas')


class sekolah(models.Model):
    nama = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True, null=True)
    web = models.CharField(max_length=100, blank=True, null=True)
    no_tlp = models.CharField(max_length=20, blank=True, null=True)
    alamat = models.TextField()
    jenis_sekolah = models.CharField(
        max_length=4,
        choices=JenisSekolah.choices,
    )

    #default
    #created_by
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
          return self.nama