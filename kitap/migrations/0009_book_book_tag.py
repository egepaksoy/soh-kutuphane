# Generated by Django 4.0.3 on 2022-04-08 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kitap', '0008_rent'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_tag',
            field=models.CharField(blank=True, choices=[('0', 'Bilinmiyor'), ('1', 'Felsefe'), ('2', 'Tarih'), ('3', 'Biyografi'), ('4', 'Hikaye'), ('5', 'İslami')], max_length=20, null=True, verbose_name='Books Tag'),
        ),
    ]
