from django.db import models
from neomodel import StructuredNode, StringProperty, DateProperty, RelationshipTo

class Book(StructuredNode):
    title = StringProperty()

class Library(StructuredNode):
    place = StringProperty()
    books = RelationshipTo(Book, 'IS_FROM')

class Reader(StructuredNode):
    name = StringProperty()
    books = RelationshipTo(Book, 'IS_FROM')