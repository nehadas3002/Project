from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.http.response import JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from .models import User, NewBook, Read, Reading, Rating, Comment


# Create your views here.

def index(request):
    all_books = NewBook.objects.all()
    return render(request, "books/index.html", {
        "all_books": all_books, 
        "home": True
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "books/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "books/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "books/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "books/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "books/register.html")

def newbook(request):
    if request.method == "POST":
        title = request.POST["title"]
        author = request.POST["author"]
        cover = request.POST["cover"]
        synopsis = request.POST["synopsis"]
        user = request.user
        ins = NewBook(title=title, author=author, cover=cover, user=user, synopsis=synopsis)
        ins.save()

        return HttpResponseRedirect(reverse("index"))

def search(request):
    if request.method == "POST":
        search = request.POST["search"]
        
        titles = []
        """This array holds all the titles"""

        for book in NewBook.objects.all():
            titles.append(book.title)

        results = []
        
        for title in titles:
            if search.upper() in title.upper():
                results.append(title)

        objects = []
        """This array holds all the objects from the titles"""

        for result in results:
            objects.append(NewBook.objects.get(title=result))


        return render(request, "books/search.html", {
            "search": search, 
            "results": results, 
            "objects": objects, 
            "home": False
        })

@login_required(login_url="login")
def booklist(request, bookid):
    selected = NewBook.objects.get(pk=bookid)

    user = User.objects.get(username = request.user)
    # book = NewBook.objects.get(id=bookid)
    
    message = ""
    success = False
    exists = Rating.objects.filter(user = user, book = selected).exists()

    if request.method == "POST":
        if "read" in request.POST: 
            newread = Read(user=user, book=selected)
            newread.save()
            return HttpResponseRedirect(reverse("booklist", kwargs={"bookid": bookid}))
            

        elif "reading" in request.POST:
            newreading = Reading(user=user, book=selected)
            newreading.save()
            return HttpResponseRedirect(reverse("booklist", kwargs={"bookid": bookid}))

        elif "un-read" in request.POST:
            object = Read.objects.get(user=user, book=selected)
            object.delete()
            return HttpResponseRedirect(reverse("booklist", kwargs={"bookid": bookid}))

        elif "un-reading" in request.POST:
            object = Reading.objects.get(user=user, book=selected)
            object.delete()
            return HttpResponseRedirect(reverse("booklist", kwargs={"bookid": bookid}))

        elif "first" in request.POST:
            if exists:
                f = Rating.objects.get(user = user, book = selected)
                f.delete()

            rate = Rating(user=user, book=selected, rating=1)
            rate.save()
            message = "You rated this book 1 star"
            success = True
            return HttpResponseRedirect(reverse("booklist", kwargs={"bookid": bookid}))

        elif "second" in request.POST: 
            if exists:
                f = Rating.objects.get(user = user, book = selected)
                f.delete()

            rate = Rating(user=user, book=selected, rating=2)
            rate.save()
            message = "You rated this book 2 star"
            success = True
            return HttpResponseRedirect(reverse("booklist", kwargs={"bookid": bookid}))

        elif "third" in request.POST: 
            if exists:
                f = Rating.objects.get(user = user, book = selected)
                f.delete()

            rate = Rating(user=user, book=selected, rating=3)
            rate.save()
            message = "You rated this book 3 star"
            success = True
            return HttpResponseRedirect(reverse("booklist", kwargs={"bookid": bookid}))

        elif "fourth" in request.POST:
            if exists:
                f = Rating.objects.get(user = user, book = selected)
                f.delete()

            rate = Rating(user=user, book=selected, rating=4)
            rate.save()
            message = "You rated this book 4 star"
            success = True
            return HttpResponseRedirect(reverse("booklist", kwargs={"bookid": bookid}))

        elif "fifth" in request.POST: 
            if exists:
                f = Rating.objects.get(user = user, book = selected)
                f.delete()

            rate = Rating(user=user, book=selected, rating=5)
            rate.save()
            message = "You rated this book 5 star"
            success = True
            return HttpResponseRedirect(reverse("booklist", kwargs={"bookid": bookid}))

    is_read = Read.objects.filter(book = selected, user = user).exists()
    is_reading = Reading.objects.filter(book = selected, user = user).exists()
    number_of_ratings = Rating.objects.filter(book = selected).count()

    ones = Rating.objects.filter(book = selected, rating = 1).count()
    twos = Rating.objects.filter(book = selected, rating = 2).count()
    threes = Rating.objects.filter(book = selected, rating = 3).count()
    fours = Rating.objects.filter(book = selected, rating = 4).count()
    fives = Rating.objects.filter(book = selected, rating = 5).count()

    rate2 = Rating.objects.get(user = user, book = selected) if exists else 0
    personal_rate = rate2.rating if exists else 0 

    message2 = f"You rate this book {personal_rate} stars"


    return render(request, "books/booklist.html", {
        "selected_book": selected, 
        "is_read": is_read,
        "is_reading": is_reading, 
        "message": message, 
        "number_of_ratings": number_of_ratings,
        "success": success, 
        "ones": ones, 
        "twos": twos, 
        "threes": threes, 
        "fours": fours, 
        "fives": fives, 
        "exists": exists, 
        "message2": message2,
        "personal_rate": personal_rate, 
        "home": False

    })


@login_required(login_url="login")
def mybooks(request):
    user = User.objects.get(username = request.user)

    readbooks = Read.objects.filter(user=user)
    readingbooks = Reading.objects.filter(user=user)
    count = readbooks.count()

    return render(request, "books/mybooks.html", {
        "readbooks": readbooks,
        "readingbooks": readingbooks, 
        "home": False, 
        "count": count, 
        "count2": readingbooks.count()
    })

@login_required(login_url="login")
def bookchats(request): 
    all_books = NewBook.objects.all()
    return render(request, "books/bookchats.html", {
        "all_books": all_books, 
        "home": False
    })

@login_required(login_url="login")
def chat(request, bookid):
    book = NewBook.objects.get(id=bookid)

    if request.method == "POST":
        comment = request.POST["comment"]
        message = Comment(user = request.user, book = book, comment = comment)
        message.save()
        return HttpResponseRedirect(reverse("chat", kwargs={"bookid": bookid}))


    comments = Comment.objects.filter(book = book)

    return render(request, "books/chat.html", {
        "title": book.title, 
        "book": book, 
        "comments": comments, 
        "test": Comment.objects.first(),
        "home": False
    })








