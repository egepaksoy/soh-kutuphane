# Generated by Django 4.0.3 on 2022-03-13 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=100, verbose_name='Kitabın Adı')),
                ('book_writer', models.CharField(max_length=100, verbose_name='Kitabın Yazarı')),
                ('book_date', models.DateField(blank=True, verbose_name='Kitabın Yayınlanma Tarihi')),
                ('alan_og', models.CharField(blank=True, max_length=150, verbose_name='Kitabı Alan Ogrenci')),
                ('alis_tar', models.DateField(blank=True, verbose_name='Kitabın Verilme Tarihi')),
                ('teslim_tar', models.DateField(blank=True, verbose_name='Kitabın Teslim Tarihi')),
                ('alan_ogrenciler_json', models.JSONField(verbose_name='Kitabı Alan Öğrenciler jsonf')),
            ],
        ),
    ]
