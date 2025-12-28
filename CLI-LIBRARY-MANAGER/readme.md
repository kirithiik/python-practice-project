# 📚 CLI Library Manager (Python)

A simple command-line based Library Management System built using Python.  
This project helps manage books in a library by allowing users to add, view, search, issue, and return books.

---

## 📌 Project Overview

The CLI Library Manager simulates a basic library system where each book has:
- a title
- an author
- an issued status (available or issued)

The system focuses on **state management** and **clean control flow**, making it a good practice project for understanding how real-world systems work.

---

## ✨ Features

- Add new books to the library
- View all books with their current status
- Search books by author
- Issue a book (mark as taken)
- Return a book (mark as available)
- Menu-driven interface
- Input validation and clear feedback messages

---

## 🧠 Concepts Used

- Lists and dictionaries
- Boolean state management
- Loops and conditional logic
- Functions and modular design
- Control flow correctness
- Case-insensitive string comparison

---

## 🗂️ Data Structure

Each book is stored as a dictionary inside a list:

```python
books = [
    {
        "title": "1984",
        "author": "Orwell",
        "issued": False
    }
]
