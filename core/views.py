from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Book, Borrower, BorrowRecord


class HomeView(ListView):
    model = Book
    template_name = 'core/home.html'
    context_object_name = 'books'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            return queryset.filter(title__icontains=query) | queryset.filter(author__icontains=query)
        return queryset


class BookDetailView(DetailView):
    model = Book
    template_name = 'core/book_detail.html'
    context_object_name = 'book'


class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    template_name = 'core/book_form.html'
    fields = ['title', 'author', 'isbn', 'published_date', 'description', 'page_count', 'genre']
    success_url = reverse_lazy('home')


class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    template_name = 'core/book_form.html'
    fields = ['title', 'author', 'isbn', 'published_date', 'description', 'page_count', 'genre']
    success_url = reverse_lazy('home')


class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Book
    template_name = 'core/book_confirm_delete.html'
    success_url = reverse_lazy('home')


class BorrowerListView(LoginRequiredMixin, ListView):
    model = Borrower
    template_name = 'core/borrower_list.html'
    context_object_name = 'borrowers'
    paginate_by = 10


class BorrowerDetailView(LoginRequiredMixin, DetailView):
    model = Borrower
    template_name = 'core/borrower_detail.html'
    context_object_name = 'borrower'


class BorrowRecordCreateView(LoginRequiredMixin, CreateView):
    model = BorrowRecord
    template_name = 'core/borrow_form.html'
    fields = ['book', 'borrower', 'borrow_date', 'due_date']
    success_url = reverse_lazy('home')


def return_book(request, pk):
    borrow_record = get_object_or_404(BorrowRecord, pk=pk)
    if request.method == 'POST':
        borrow_record.returned = True
        borrow_record.return_date = request.POST.get('return_date')
        borrow_record.save()
        return redirect('borrower_detail', pk=borrow_record.borrower.pk)
    return render(request, 'core/return_book.html', {'borrow_record': borrow_record})