# Generated by Django 4.1.5 on 2023-01-16 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='perusahaan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('web', models.CharField(blank=True, max_length=100, null=True)),
                ('no_tlp', models.CharField(blank=True, max_length=20, null=True)),
                ('alamat', models.TextField()),
                ('jenis_perusahaan', models.CharField(choices=[('PT', 'Persero Terbatas (PT)'), ('CV', 'Persekutuan Komanditer (CV)'), ('FM', 'Firma'), ('KP', 'Koperasi')], max_length=2)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
