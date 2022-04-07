from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout



def home(req):
  if req.user.is_authenticated:
    return redirect('search_book')

  if req.method == "POST":
    username = "nobetci"
    password = req.POST.get("passwd")
    

    user = authenticate(req, username=username, password=password)

    if user is not None:
      login(req, user)

    return redirect('search_book')

  return render(req, "login.html")

def logout_view(req):
  if req.method == "POST":
    logout(req)
    return redirect("login")

  return redirect("search_book")