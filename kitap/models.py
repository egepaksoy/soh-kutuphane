import jsonfield
from django.db import models


class Book(models.Model):
  tags = [
    ("islami","İslami"),
    ("felsefe","Felsefe"),
    ("tarih","Tarih"),
    ("biyografi","Biyografi"),
    ("deneme","Deneme"),
    ("edebiyat", "Edebiyat"),
    ("yabancı dil", "Yabancı Dil"),
    ("fen bilimleri", "Fen bilimleri"),
    ("roman", "Roman"),
    ("din", "Din"),
  ]
  book_name = models.CharField(verbose_name="Kitabın Adı (Sorumlu kisi doldurmalı)", max_length=100, blank=False)
  book_writer = models.CharField(verbose_name="Kitabın Yazarı (Sorumlu kisi doldurmalı)", max_length=100, blank=False)
  book_date = models.DateField(verbose_name="Kitabın Yayınlanma Tarihi (Sorumlu kisi doldurmalı)", blank=True, null=True)
  book_tag = models.CharField(verbose_name="Kitabın Kategorisi (Sorumlu kişi doldurmalı", max_length=20, choices=tags, null=True, blank=True)
  alan_og = models.CharField(verbose_name="Kitabı Alan Ogrenci (Program Kendi dolduracak)", max_length=150, blank=True, null=True)
  alis_tar = models.DateField(verbose_name="Kitabın Verilme Tarihi (Program Kendi dolduracak)", blank=True, null=True)
  teslim_tar = models.DateField(verbose_name="Kitabın Teslim Tarihi (Program Kendi dolduracak)", blank=True, null=True)
  alan_ogrenciler_json = jsonfield.JSONField(verbose_name="Kitabı daha önce ödünç almış öğrenciler (Program Kendi dolduracak)", null=True, blank=True)
  # [{"adı": "Ege Paksoy", "Alıs tarihi": bir tarih(-), "Teslim Tarihi": tarih}]

  def __str__(self):
      return self.book_name

class Rent(models.Model):
  idler = jsonfield.JSONField(verbose_name="Kitapların IDleri (Program Kendi dolduracak)", null=True, blank=True)

  def __str__(self):
      return "Emanet alınan kitaplar"