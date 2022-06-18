from django.urls import path , include
from . import views

urlpatterns = [
path("",views.index),
path("addbook",views.addbook),
path("book/<int:id>",views.book ,name='bdetail'),
path("auther",views.auther),
path("addauther",views.addauther),
path("oneauther/<int:id>",views.oneauther,name='adetail'),
path('authorToBook/<int:authorId>',views.authorToBook),
path('bookToAuthor/<int:bookId>',views.bookToAuthor),


]