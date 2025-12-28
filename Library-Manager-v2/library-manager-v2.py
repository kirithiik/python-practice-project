import json
import os

DATA_FILE = "library_data.json"


# ---------- File Handling ----------
def load_books():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []


def save_books(books):
    with open(DATA_FILE, "w") as f:
        json.dump(books, f)


# ---------- Menu ----------
def menu():
    print("\n📚 Library Manager")
    print("1. Add book")
    print("2. View all books")
    print("3. Search books by author")
    print("4. Issue a book")
    print("5. Return a book")
    print("6. Exit")


# ---------- Features ----------
def add_book(books):
    title = input("Enter book title: ").strip()
    author = input("Enter book author: ").strip()

    books.append({
        "title": title,
        "author": author,
        "issued": False
    })

    save_books(books)
    print("✅ Book added successfully")


def view_books(books):
    if not books:
        print("❌ No books available")
        return

    for book in books:
        status = "Issued" if book["issued"] else "Available"
        print(f"Title: {book['title']} | Author: {book['author']} | Status: {status}")


def search_books_by_author(books):
    author_name = input("Enter author name: ").strip().lower()
    found = False

    for book in books:
        if book["author"].lower() == author_name:
            status = "Issued" if book["issued"] else "Available"
            print(f"Title: {book['title']} | Status: {status}")
            found = True

    if not found:
        print("❌ No books found for this author")


def issue_book(books):
    title = input("Enter book title to issue: ").strip().lower()

    for book in books:
        if book["title"].lower() == title:
            if not book["issued"]:
                book["issued"] = True
                save_books(books)
                print("✅ Book issued successfully")
            else:
                print("⚠️ Book is already issued")
            return

    print("❌ Book not found")


def return_book(books):
    title = input("Enter book title to return: ").strip().lower()

    for book in books:
        if book["title"].lower() == title:
            if book["issued"]:
                book["issued"] = False
                save_books(books)
                print("✅ Book returned successfully")
            else:
                print("⚠️ Book was not issued")
            return

    print("❌ Book not found")


# ---------- Main ----------
def main():
    books = load_books()
    print("📖 Welcome to Library Manager")

    while True:
        menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_book(books)
        elif choice == "2":
            view_books(books)
        elif choice == "3":
            search_books_by_author(books)
        elif choice == "4":
            issue_book(books)
        elif choice == "5":
            return_book(books)
        elif choice == "6":
            save_books(books)
            print("💾 Data saved. Goodbye 👋")
            break
        else:
            print("❌ Invalid choice. Try again.")


if __name__ == "__main__":
    main()
