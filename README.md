# 📚 Library Management System

A modern Django application for managing a library's books, borrowers, and loan records.

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Django](https://img.shields.io/badge/Django-4.2+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Features

- 📖 Complete book catalog management
- 👥 Borrower registration and management
- 📅 Loan tracking with due dates
- 🔍 Search functionality for books
- 🛡️ User authentication and permissions
- 📱 Mobile-responsive design

## 🚀 Installation

### Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.9 or higher
- pip (Python package manager)
- Git

### Step 1: Clone the Repository

```bash
git clone https://github.com/d4nyphant0m/lib.git
cd lib
```

### Step 2: Set Up a Virtual Environment

#### On macOS/Linux:

```bash
python -m venv venv
source venv/bin/activate
```

#### On Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 5: Create a Superuser

```bash
python manage.py createsuperuser
```

### Step 6: Start the Development Server

```bash
python manage.py runserver
```

Your library management system is now running at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)!

## 🖥️ Usage

- **Admin Interface**: Access the admin panel at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) to manage books, borrowers, and loans.
- **Book Catalog**: Browse the book collection on the home page.
- **Borrower Management**: Register and track library members.
- **Loan Management**: Record and track book loans with due dates.

## 🏗️ Project Structure

```
lib/
├── config/             # Project settings
├── core/               # Main application
│   ├── models.py       # Database models
│   ├── views.py        # View controllers
│   ├── urls.py         # URL routing
│   └── admin.py        # Admin interface
├── templates/          # HTML templates
├── static/             # Static assets
├── manage.py           # Django command-line utility
└── requirements.txt    # Dependencies
```

## 🛠️ Development

- **Create a new app**: `python manage.py startapp app_name`
- **Run tests**: `python manage.py test`
- **Generate migrations**: `python manage.py makemigrations`
- **Apply migrations**: `python manage.py migrate`
- **Collect static files**: `python manage.py collectstatic`

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

Made with ❤️ using Django