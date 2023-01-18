from django.contrib import admin
from .models import perusahaan

# Register your models here.
class dataPerusahaan(admin.ModelAdmin):
    list_display = ['nama', 'email', 'web', 'no_tlp', 'alamat', 'jenis_perusahaan', 'created_by', 'created_at', 'updated_at' ]
admin.site.register(perusahaan, dataPerusahaan)