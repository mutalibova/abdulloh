from django.shortcuts import render, redirect
from .models import WorkmateUser, Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def register(request):
    if request.method == "POST":
        name = request.POST.get("name")
        code = request.POST.get("code")

        if WorkmateUser.objects.filter(name=name).exists():
            return render(request, "register.html", {"error": "Bu ism mavjud"})

        WorkmateUser.objects.create(name=name, code=code)
        return redirect("login")

    return render(request, "register.html")

def login(request):
    if request.method == "POST":
        name = request.POST.get("name")
        code = request.POST.get("code")
        user = WorkmateUser.objects.filter(name=name, code=code).first()
        if user:
            request.session["user_id"] = user.id
            request.session["name"] = user.name
            return redirect("home")
        else:
            return render(request, "login.html", {"error": "Xato ma'lumot"})
    return render(request, "login.html")

def home(request):
    if "user_id" not in request.session:
        return redirect("register") 
    narsalar = Post.objects.all()
    return render(request, 'home.html', {"narsalar":narsalar})

def bos(request):
    narsalar = Post.objects.all()
    return render(request, 'bos.html')

def about(request):
    about = Post.objects.all()
    return render(request, 'about.html')

def acaunt(request):
    if "user_id" not in request.session:
        return redirect("login")
    user_id = request.session["user_id"]
    user = WorkmateUser.objects.get(id=user_id)
    ishlar = Post.objects.count()
    profi = Post.objects.filter(text2__isnull=False).count()
    haqida = Post.objects.filter(text3__isnull=False).count()
    return render(request, 'acaunt.html', {
        "user": user,
        "ishlar": ishlar,
        "profi": profi,
        "haqida": haqida
    })

def haqida(request):
    haqida = Post.objects.all()
    return render(request, 'haqida.html')

def index(request):
    index = Post.objects.all()
    return render(request, 'index.html')

def job(request):
    job = Post.objects.all()
    return render(request, 'job.html')

def frontend(request):
    frontend = Post.objects.all()
    return render(request, 'frontend.html')

def see(request):
    see = Post.objects.all()
    return render(request, 'see.html')

def til(request):
    til = Post.objects.all()
    return render(request, 'til.html')

def logout(request):
    request.session.flush()
    return redirect("login")