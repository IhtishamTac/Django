from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class JenisKelamin(models.TextChoices):
        LAKILAKI = 'L', _('Laki-Laki')
        PEREMPUAN = 'P', _('Perempuan')


class siswa(models.Model):
    nama = models.CharField(max_length=50)
    jenis_kelamin = models.CharField(
            max_length=1,
            choices=JenisKelamin.choices,
        )
    sekolah = models.OneToOneField("sekolah.sekolah", on_delete=models.CASCADE, blank=True, null=True)

    no_tlp = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    alamat = models.TextField(default='Jawa Barat, Indonesia')
    tempat_lahir = models.CharField(max_length=100)
    tanggal_lahir = models.DateField()
    nisn = models.CharField(max_length=20)

    #default
    #created_by
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
          return self.nama

    


