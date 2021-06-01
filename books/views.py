from django.shortcuts import render
from faker import Faker
import random
from books.models import *
fake = Faker()

# Create your views here.
def index(request):

# create books 
    n = 10
    for i in range(0, n):
        book = Book(title=fake.color()).save()
    
    # create libraries 

    for i in range(0, int(n/10)):
        library = Library(place=fake.address()).save()
    
    # create readers 

    for i in range(0, n*5):
        reader = Reader(name=fake.name()).save()

    all_books = Book.nodes.all()
    all_library = Library.nodes.all()
    all_reader = Reader.nodes.all()

    for lib in all_library:
        books_in_library = random.sample(all_books, n)
        for book in books_in_library:
            lib.books.connect(book)
            lib.save()
    
    for book in all_books:
        readers_in_total = random.sample(all_reader, n*2)
        for reader in readers_in_total:
            reader.books.connect(book)
            reader.save()

    return render(request, 'books/index.html')
