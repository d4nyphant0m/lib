from django.contrib import admin
from .models import Book, Borrower, BorrowRecord


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'published_date', 'genre')
    list_filter = ('genre', 'published_date')
    search_fields = ('title', 'author', 'isbn')
    ordering = ('title',)


@admin.register(Borrower)
class BorrowerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'registration_date', 'active')
    list_filter = ('active', 'registration_date')
    search_fields = ('first_name', 'last_name', 'email')
    ordering = ('last_name', 'first_name')


@admin.register(BorrowRecord)
class BorrowRecordAdmin(admin.ModelAdmin):
    list_display = ('book', 'borrower', 'borrow_date', 'due_date', 'return_date', 'returned')
    list_filter = ('returned', 'borrow_date', 'due_date')
    search_fields = ('book__title', 'borrower__last_name', 'borrower__first_name')
    ordering = ('-borrow_date',)