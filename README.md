# Captstone Project: BookWorm
Bookworm is an application that allows users to rate, log/record, and chat about their reading selections. It is designed to create a space for people to discuss books they like, track their reading progress, and give their opinions on different books. This is achieved through a rating system, a chat feature, and a reading list feature. Bookworm is perfect for the average reader and the hardcore book worm. The reason why I created this project is because there is lack of quality forum/discussion spaces for books and I personally found it difficult to find people to talk about a specific book with. 

## Distinctiveness and Complexity

### Justification

This project is sufficiently distinct from other projects in this course. 

* It is not a typical social network nor an e-commerce website. 
    - Bookworm is a forum website for discussion and sharing opinions on a niche topic. 
* Rating system
    - One difference between this project and others in this course is that this web application has a 5 star rating system which allows users to rate a book on a scale of 1 to 5 and that information is displayed to all other users whereas past projects have had more simple user interactions such as 'likes'. 
* Messaging capability
    - This application also includes a chat feature in the visual form of chat boxes for each book for users to discuss books that they have already read with other fans of the book which are not part of previous projects. 
* Completely Mobile Responsive
    - This website was made to be mobily responsive using bootstrap grid and flexbox. The layout adjusts for phone screens where the information elegantly stacks on each other whereas for larger screens, the layout extends into the wider space. 
* Languages
    - This website uses django on the backend, and html, css, and javascript on the front end, all languages learned in lecture

## Files and what they contain

* books
    - static
        - ```books/main.js``` - java scripts for the website. Contains a function that fills in stars when hovering over the rating system. Contains a function that changes displays to block when drop downs are clicked. 
        - ```books/styles.css``` - Styling for web pages. 
    - Templates
        - ```books/bookchats.html``` -  html for a list of links to every single book chat that has been created.
        - ```books/booklist.html``` -  the page that displays all of the information for each book individually on each page using bootrap grid. Contains title, author, user who posted, rating, synopsis, and link to bookchat for that book. 
        - ```books/chat.html``` - shows the chat for a specific book. Formatted similar to imessage. Created using bootrap classes. 
        - ```books/index.html``` - homepage that lists all the books. Has add book option. 
        - ```books/layout.html``` -  base that is extended in every html file. Contains navigation bar. When user is logged out, the nav bar has links for all books, log in, and register. When user is logged in, the navigation bar has links to all books, my books, book chats, and logout. On the right ride, there is the search bar where there user can search via title. This nav bar is present on all the pages. 
        - ```books/login.html``` - this is the log in page when an already established user can log in and view their personalized account
        - ```books/mybooks.html``` - displays the user’s customized “read” and “reading” lists based on what they have added to their lists. 
        - ```books/register.html``` - this is the registration page when new users can create an account and begin accessing the website. 
        - ```books/search.html``` - displays the results from the search form. When a user searched, any titles with the query inside the title are displayed on this page and they books are clickable which take you to the ```booklist.html``` page. 
    - ```models.py``` - contains models for objects
        - User - different users, username, email, password
        - Read - List of books that the user has already read, user and book attributes
        - Reading - List of books user is currently reading, user and book attributes
        - Rating - Stores different ratings for books given by users. Book, rating, and user attributes
        - Comment - Chats sent to my users for a particular book. Book, user, and comment attribute
    - ```urls.py ``` - defines what function/view runs for each url. 
    - ```views.py``` - contains functions for the web application which send and receive https requests. Functions include index, login_view, logout_view, register, newbook (which posts a new book), search(which allows to search via title by accessing POST request), booklist(shows each individual book page details), my books(which shows the read and reading list along with the book count), and chat(which allows users to send messages about books). 
* booksite
    - ```__init__.py``` - this file is empty 
    - ```asgi.py``` - file isunedited, automatically created whens tarting a django project
    - ```settings.py``` - in this file, I installed the books application by adding it to the ```INSTALLED_APPS``` array
    - ```urls.py``` - handles the urls of the application and links to the books app’s urls.py file through include. 
    - ```wsgi.py``` - unedited, automatically created as part of django project
* ```manage.py``` - Unedited file created when starting django project. Allows for us to run commands on the web application in the terminal. 


## Features

__Adding a new book__ - if not already present in the database, a user can add a new book for which any user can rate, comment or add to their reading lists. 

__Book page__ - this feature allows users to view the information on the book to ade in theri selection. It has the title and author, all the rating information gathered from other users, and a short summary on what the book is about

__Read/Reading list__ - this feature allows users to keep track of what they have read, and what they are currently reading as well as how many books are in each list. 

__Rating__ - this feature allows users to rate books on a scale of one to five and then that information is displayed on each book page. 

__Book chats__ - this feature is a chat room that exists for each individual book. It visually looks like text messages. Gray messages are from other users, blue messages are user sent messages, familiar to imessage users. 

__Search__ - users can search for a specific book via title. 

## Installation

__Step 1__:
Download code as zip file and unzip. Navigate to folder in terminal. 
In terminal: 
```pip install -r requirements.txt```

_the only package required to run this application is django_ 

__Step 2__: 
Navigate inside folder on the level of manage.py file.
In terminal: 
```python manage.py runserver```

__Step 3__: 
click register and create a new user. You can create as many users as you want. Then the website is yours to explore. 

[Demonstration Link] (https://youtu.be/-aJYUBsWaWM)













