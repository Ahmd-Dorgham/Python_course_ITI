import random
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.core.validators import MaxLengthValidator

class Category(models.Model):
    name = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(2, message="Error! Name is too short.")]
    )

    class Meta:
        verbose_name_plural = "All Categories"

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(
        max_length=50,
        validators=[
            MinLengthValidator(10, message="Bad length for the book name."),
            MaxLengthValidator(50, message="Bad length for the book name.")
        ]
    )
    desc = models.TextField()
    rate = models.FloatField()
    views = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books')
    categories = models.ManyToManyField(Category, related_name='books')

    def __str__(self):
        return self.title

def generate_isbn():
    my_string = ""
    for i in range(13):
        n = random.randint(0, 9)
        my_string = my_string + str(n)
    return my_string

class ISBN(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE, related_name='isbn')
    author_title = models.CharField(max_length=100)
    book_title = models.CharField(max_length=100)
    isbn_number = models.CharField(max_length=50, unique=True, default=generate_isbn)

    class Meta:
        verbose_name = "Book ISBN"
        verbose_name_plural = "Book ISBNs"

    def __str__(self):
        return self.book_title + " and " + self.isbn_number