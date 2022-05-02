from django.urls import path
from . import views 

urlpatterns = [
    path("", views.index, name="index"), 
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("newbook", views.newbook, name="newbook"), 
    path("search", views.search, name="search"), 
    path("booklist/<int:bookid>", views.booklist, name="booklist"), 
    path("mybooks", views.mybooks, name="mybooks"), 
    path("bookchats", views.bookchats, name="bookchats"), 
    path("chat/<int:bookid>", views.chat, name="chat")

]