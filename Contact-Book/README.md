# Contact Book (Python)

A simple command-line Contact Book application built using Python.
This project was created to practice working with lists, dictionaries, functions, and file handling using JSON.

## Features
- Add new contacts (name, phone number, email)
- View all saved contacts
- Search contacts by name (case-insensitive, partial match)
- Delete contacts using index number
- Persistent storage using JSON

## Concepts Used
- Functions and modular programming
- Lists and dictionaries
- File handling with JSON
- `os.path.exists()` for safe file loading
- Menu-driven command line interface
- Basic input validation

## How It Works
- Contact data is stored in a JSON file (`contacts.json`)
- When the program starts, existing contacts are loaded automatically
- Any change (add/delete) is immediately saved
- Data persists even after restarting the program

## How to Run
1. Make sure Python is installed.
2. Run the program using:
   ```bash
   python contact_book.py
