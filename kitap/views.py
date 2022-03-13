import datetime
import json
from django.shortcuts import render, HttpResponse, redirect
from .models import *


def search_book(req):
  if req.method == "GET":
    return render(req, "search_page.html")
  else: 
    book_name = req.POST.get("book_credation")
    all_books = Book.objects.all()
    books = []
    for book in all_books:
      if  book_name.upper() in book.book_name.upper() or  book_name.upper() in book.book_writer.upper():
        books.append(book)

    return render(req, "search_page.html", context={"books": books})

def book_info(req, id):
  if req.method == "POST":
    book = Book.objects.get(id=id)
    return render(req, "book_info.html", context={"book": book})

  else:
    return redirect("search_book")

def book_teslim(req, id):
  if req.method == "POST":
    book = Book.objects.get(id=id)
    book_update = Book.objects.filter(id=id)
    today = datetime.date.today()

    book_update.update(teslim_tar=today)

    json_data = {
      "alan_og": book.alan_og,
      "alis_tar": book.alis_tar,
      "teslim_tar": today
    }

    b = book.alan_ogrenciler_json

    if book != "null":
      b.append(json_data)
    else:
      b = json_data

    book_update.update(alan_ogrenciler_json=b)

    book_update.update(alan_og=None, alis_tar=None, teslim_tar=None)

    # TODO: search sayfasına kitap teslim kabul edilmiştir diye mesaj göndercek


  return redirect("search_book")

def book_emanet(req, id):
  if req.method == "POST":
    book_update = Book.objects.filter(id=id)
    today = datetime.date.today()

    ogrenci_ismi = req.POST.get("ogrenci_ad")

    book_update.update(alis_tar=today, alan_og=ogrenci_ismi)
  
    return redirect("search_book")

  return render(req, "emanet.html")