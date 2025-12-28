books = [
  {"title": "1984", "author": "Orwell", "issued": False}
]
def menu():
  print("1. Add books")
  print("2. View all books")
  print("3. Search books by author")
  print("4. Issue a book")
  print("5. return a book")
  print("6. Exit")

def add_book():
  t=input("Enter book title: ")
  a=input("Enter book author: ")
  books.append({"title":t, "author":a, "issued":False})
  print("book added successfully")

def view_books():
  for book in books:
    status = "Issued" if book["issued"] else "Available"
    print(f"Title : {book["title"]}, Author : {book["author"]}, Status : {status}")

def search_books_by_author():
  auth=input("Enter author name: ")
  found = False
  for book in books:
    if book["author"].lower() == auth.lower():
      status = "Issued" if book["issued"] else "Available"
      print(f"Title : {book["title"]}, Author : {book["author"]}, Staus : {status}")
      found = True
  if not found:
    print("No books found by that author.")

def issue_book():
  take=input("Enter book title to be issued: ")
  found = False
  for book in books:
    if book["title"].lower() == take.lower():
      found = True
      if not book["issued"]:
        book["issued"] = True
        print("book issued successfully")
      else:
        print("book is already issued")
  if not found:
    print("book not found")

def return_book():
    ret = input("Enter the book title to be returned: ")
    found = False

    for book in books:
        if book["title"].lower() == ret.lower():
            found = True
            if book["issued"]:
                book["issued"] = False
                print("Book returned successfully")
            else:
                print("Book was not issued")
            break

    if not found:
        print("Book not found")



def main():
  print("Welcome to the Library Manager!")
  while True:
    menu()
    choice=input("Enter the choice: ")
    if choice == "1":
      add_book()
    elif choice == "2":
      view_books()
    elif choice == "3":
      search_books_by_author()
    elif choice == "4":
      issue_book()
    elif choice == "5":
      return_book()
    elif choice == "6":
      print("Exiting the Library Manager. Goodbye!")
      break
    else:
      print("Invalid choice. Please Try again.")

if __name__=="__main__":
  main()