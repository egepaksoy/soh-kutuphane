import datetime
import json
from django.shortcuts import render, HttpResponse, redirect
from .models import *


# Ana sayfada kitap arama kodu
def search_book(req):
  if req.user.is_authenticated:
    tags = ["islami", "felsefe", "tarih", "biyografi", "edebiyat", "din", "yabancı dil", "fen bilimleri", "deneme", "roman"]
    book_rent = Rent.objects.all().first()
    all_books = Book.objects.all()
    today = datetime.date.today()
    if req.method == "GET":
      latebooks = []
      latebook = False
      if book_rent.idler != None:
        for book in book_rent.idler:
          gecen_zaman = (today-all_books.filter(id=book).first().alis_tar).days
          if gecen_zaman > 15:
            latebooks.append([all_books.filter(id=book).first(), (today-all_books.filter(id=book).first().alis_tar).days])

      if len(latebooks) != 0:
        latebook = True


      return render(req, "search_page.html", context={"latebook": latebook, "latebooks": latebooks, "tags": tags})



    else: 
      latebooks = []
      latebook = False
      if book_rent.idler != None:
        for book in book_rent.idler:
          gecen_zaman = (today-all_books.filter(id=book).first().alis_tar).days
          if gecen_zaman > 15:
            latebooks.append([all_books.filter(id=book).first(), (today-all_books.filter(id=book).first().alis_tar).days])

      if len(latebooks) != 0:
        latebook = True


      book_name = req.POST.get("book_credation")
      books = []
      for book in all_books:
        if  book_name.upper() in book.book_name.upper() or  book_name.upper() in book.book_writer.upper():
          books.append(book)

      return render(req, "search_page.html", context={"books": books, "latebook": latebook, "latebooks": latebooks, "tags": tags})
  
  return redirect("login")

# Kitabin sayfasini gosteren kod
def book_info(req, id):
  if req.user.is_authenticated:
    book = Book.objects.get(id=id)
    alis_tarihi = book.alis_tar
    today = datetime.date.today()

    alanog = []

    numOfDays = 0
    if book.alan_og:
      numOfDays = (today-alis_tarihi).days

    if book.alan_ogrenciler_json != None:
      alanog = book.alan_ogrenciler_json
      alanog.reverse()

    danger = False
    if numOfDays >= 15:
      danger = True

    return render(req, "book_info.html", context={"book": book, "danger": danger, "numDays": numOfDays, "alan_ogrenciler_json": alanog})

  return redirect("login")

# Emanet alinan kitap teslim edilirken yapilanlar
def book_teslim(req, id):
  if req.user.is_authenticated:
    if req.method == "POST":
      book = Book.objects.get(id=id)
      book_update = Book.objects.filter(id=id)
      book_rent = Rent.objects.all().first()
      today = datetime.date.today()

      gecen_gun = (today-book.alis_tar).days

      book_update.update(teslim_tar=today)

      json_data = {
        "alan_og": book.alan_og,
        "alis_tar": book.alis_tar,
        "teslim_tar": today,
        "gecen_gun": gecen_gun,
      }

      b = book.alan_ogrenciler_json

      if b == None:
        b = [json_data]
      else:
        b.append(json_data)

      idler = book_rent.idler
      if idler != None:
        if id in idler:
          idler.remove(id)

      book_rent.idler = idler
      book_rent.save()

      book_update.update(alan_ogrenciler_json=b)

      book_update.update(alan_og=None, alis_tar=None, teslim_tar=None)


      # TODO: search sayfasına kitap teslim kabul edilmiştir diye mesaj göndercek


    return redirect("book_info", id=id)

  return redirect("login")

# Kitaplar emanet alinirken yapilan islemler
def book_emanet(req, id):
  if req.user.is_authenticated:
    if req.method == "POST":
      book_update = Book.objects.filter(id=id)
      book_rent = Rent.objects.all().first()
      today = datetime.date.today()

      ogrenci_ismi = req.POST.get("ogrenci_ad")

      book_update.update(alis_tar=today, alan_og=ogrenci_ismi)

      idler = book_rent.idler
      if book_rent.idler == None:
        idler = [id]
      else:
        idler.append(id)

      book_rent.idler = idler

      book_rent.save()
    
      return redirect("search_book")

    return redirect("book_info", id=id)

  return redirect("login")


def book_category(req, tag):
  if req.user.is_authenticated:
    books = Book.objects.filter(book_tag=tag)

    return render(req, "book_tag.html", context={"books": books, "tag": tag})