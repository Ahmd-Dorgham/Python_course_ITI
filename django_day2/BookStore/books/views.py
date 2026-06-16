from django.shortcuts import render, redirect
from books.models import Book

def book_list(request):
    all_books = Book.objects.all()
    context = {'books': all_books}
    return render(request, 'books/all_books.html', context)

def create_book(request):
    if request.method == 'POST':
        new_book = Book()
        new_book.title = request.POST['title']
        new_book.desc = request.POST['desc']
        new_book.rate = request.POST['rate']
        new_book.views = request.POST['views']
        new_book.save()
        return redirect('book_list')
    else:
        return render(request, 'books/add_book.html')

def update_book(request, id):
    the_book = Book.objects.get(id=id)
    if request.method == 'POST':
        the_book.title = request.POST['title']
        the_book.desc = request.POST['desc']
        the_book.rate = request.POST['rate']
        the_book.views = request.POST['views']
        the_book.save()
        return redirect('book_list')
    else:
        context = {'book': the_book}
        return render(request, 'books/edit_book.html', context)

def delete_book(request, id):
    book_to_delete = Book.objects.get(id=id)
    book_to_delete.delete()
    return redirect('book_list')