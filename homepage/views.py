from django.shortcuts import render, HttpResponse


def home(req):
  return render(req, "homepage.html")