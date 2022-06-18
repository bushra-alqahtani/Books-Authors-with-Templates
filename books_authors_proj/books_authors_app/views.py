from multiprocessing import context
from django.http import HttpResponse 
from django.shortcuts import redirect, render

from books_authors_app.models import Book, Auther

# Create your views here.

#for main page
def index(request):
    context={
        'books':Book.objects.all()
    }
    return render(request,'index.html',context)


def addbook(request): #add book btn
    #check for post method
    if request.method == "POST":

        title=request.POST.get('title')
        desc=request.POST.get('decription')
        
        Book.objects.create(title=title,desc=desc)
        return redirect('/')

def book(request,id):#render the book details
    book=Book.objects.get(id=id)#to get book by id  

    authers = Auther.objects.exclude()

    context = {
    'book' : book,
    'author' : authers
    }
    return render(request,'book.html',context)


#----------------------------------------------------------------------------------
#author side and pages
def auther(request):#for auther main page
    context={
        "authors":Auther.objects.all()
    }

    return render(request,'addAuthor.html',context)

def addauther(request):#add btn 
    if request.method == "POST":
      first_name=request.POST.get("first_name")
      last_name=request.POST.get("last_name")
      notes=request.POST.get("notes")

      Auther.objects.create(first_name=first_name,last_name=last_name,notes=notes)
      return redirect("/auther")

def oneauther(request,id):
    author=Auther.objects.get(id=id) #to get the information about aother via id
    books=Book.objects.exclude() #to list all the books related to the auther

    context={
      "author":author,
       "books":books
    }
    return render(request,'author.html',context)

def authorToBook(request,authorId): #to assign the aothor to book 
    if request.method == "POST":
        
        bookId=request.post.get("book")
        book=Book.objects.get(id=int(bookId))

        author= Auther.objects.get(id=authorId)
        author.books.add(book)
        return redirect(f'/auther/{authorId}')
        
def bookToAuthor(request,bookId):
    if request.method == "POST":

        authorId=request.POST.get("author")
        author = Auther.objects.get(id=int(authorId))

        book=Book.objects.get(id=bookId)
        book.authers.add(author)
        return redirect(f'/book/{bookId}')
















