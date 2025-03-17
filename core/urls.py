from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('book/new/', views.BookCreateView.as_view(), name='book_create'),
    path('book/<int:pk>/edit/', views.BookUpdateView.as_view(), name='book_update'),
    path('book/<int:pk>/delete/', views.BookDeleteView.as_view(), name='book_delete'),
    path('borrowers/', views.BorrowerListView.as_view(), name='borrower_list'),
    path('borrower/<int:pk>/', views.BorrowerDetailView.as_view(), name='borrower_detail'),
    path('borrow/new/', views.BorrowRecordCreateView.as_view(), name='borrow_create'),
    path('borrow/<int:pk>/return/', views.return_book, name='return_book'),
]