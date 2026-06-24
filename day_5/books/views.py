from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth import logout
from .models import Book
from .form import BookForm

def book_list(request):
    all_my_books = Book.objects.all()
    my_dict = {'books': all_my_books}
    return render(request, 'books/book_list.html', my_dict)

def book_detail(request, pk):
    my_book = get_object_or_404(Book, pk=pk)
    my_book.views = my_book.views + 1
    my_book.save()
    my_dict = {'book': my_book}
    return render(request, 'books/book_detail.html', my_dict)

@login_required
def book_create(request):
    if request.method == "POST":
        my_form = BookForm(request.POST)
        if my_form.is_valid():
            my_book = my_form.save(commit=False)
            my_book.user = request.user
            my_book.save()
            my_form.save_m2m()
            return redirect('book_list')
    else:
        my_form = BookForm()
    
    my_dict = {'form': my_form, 'action': 'Make new book'}
    return render(request, 'books/book_form.html', my_dict)

@login_required
def book_update(request, pk):
    my_book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        my_form = BookForm(request.POST, instance=my_book)
        if my_form.is_valid():
            my_form.save()
            return redirect('book_detail', pk=my_book.pk)
    else:
        my_form = BookForm(instance=my_book)
        
    my_dict = {'form': my_form, 'action': 'Change book'}
    return render(request, 'books/book_form.html', my_dict)

@login_required
@permission_required('books.delete_book', raise_exception=True)
def book_delete(request, pk):
    my_book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        my_book.delete()
        return redirect('book_list')
    my_dict = {'book': my_book}
    return render(request, 'books/book_confirm_delete.html', my_dict)

def signup(request):
    if request.method == 'POST':
        my_form = UserCreationForm(request.POST)
        if my_form.is_valid():
            new_user = my_form.save()
            login(request, new_user)
            return redirect('book_list')
    else:
        my_form = UserCreationForm()
    
    my_dict = {'form': my_form}
    return render(request, 'registration/signup.html', my_dict)

def logout_view(request):
    logout(request)
    return redirect('book_list')