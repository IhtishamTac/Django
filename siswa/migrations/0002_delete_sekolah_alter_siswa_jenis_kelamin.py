# Generated by Django 4.1.5 on 2023-01-16 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siswa', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='sekolah',
        ),
        migrations.AlterField(
            model_name='siswa',
            name='jenis_kelamin',
            field=models.CharField(choices=[('L', 'Laki-Laki'), ('P', 'Perempuan')], max_length=1),
        ),
    ]
