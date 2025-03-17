from django.db import models


class Book(models.Model):
    """Book model representing a library book."""
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, unique=True)
    published_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)
    page_count = models.PositiveIntegerField(null=True, blank=True)
    genre = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return f"{self.title} by {self.author}"


class Borrower(models.Model):
    """Model representing a person who can borrow books."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True)
    registration_date = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class BorrowRecord(models.Model):
    """Model representing a book borrowing record."""
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='borrow_records')
    borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE, related_name='borrow_records')
    borrow_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    due_date = models.DateField()
    returned = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-borrow_date']

    def __str__(self):
        return f"{self.book.title} borrowed by {self.borrower}"