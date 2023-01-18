from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

# Create your models here.

class JenisPerusahaan(models.TextChoices):
        PT = 'PT', _('Persero Terbatas (PT)')
        CV = 'CV', _('Persekutuan Komanditer (CV)')
        FIRMA = 'FMA', _('Firma')
        KOPERASI = 'KPR', _('Koperasi')
        YAYASAN = 'YYS', _('Yayasan')

class perusahaan(models.Model):
    nama = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True, null=True)
    web = models.CharField(max_length=100, blank=True, null=True)
    no_tlp = models.CharField(max_length=20, blank=True, null=True)
    alamat = models.TextField()
    jenis_perusahaan = models.CharField(
        max_length=3,
        choices=JenisPerusahaan.choices,
    )

    #default
    created_by = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, related_name="perusahaan_created_by", default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
          return self.nama