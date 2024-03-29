# Generated by Django 4.0.3 on 2022-03-13 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kitap', '0004_alter_book_alan_ogrenciler_json'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='alan_og',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Kitabı Alan Ogrenci'),
        ),
        migrations.AlterField(
            model_name='book',
            name='alis_tar',
            field=models.DateField(blank=True, null=True, verbose_name='Kitabın Verilme Tarihi'),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_date',
            field=models.DateField(blank=True, null=True, verbose_name='Kitabın Yayınlanma Tarihi'),
        ),
        migrations.AlterField(
            model_name='book',
            name='teslim_tar',
            field=models.DateField(blank=True, null=True, verbose_name='Kitabın Teslim Tarihi'),
        ),
    ]
