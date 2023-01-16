from django.contrib import admin
from .models import sekolah

# Register your models here.
class namaSekolah(admin.ModelAdmin):
    list_display = ['nama', 'email', 'web', 'no_tlp', 'alamat', 'jenis_sekolah', 'created_at', 'updated_at' ]

admin.site.register(sekolah,namaSekolah)