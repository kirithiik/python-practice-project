import json
import os

DATA_FILE = "contacts.json"
contacts = []


def menu():
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")


def load_contacts():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []


def save_contacts(contacts):
    with open(DATA_FILE, "w") as f:
        json.dump(contacts, f)


def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email
    })

    save_contacts(contacts)
    print("Contact added successfully.")


def view_contacts(contacts):
    if len(contacts) == 0:
        print("No contacts found.")
        return

    print("\n--- Contact List ---")
    for i, cnt in enumerate(contacts, start=1):
        print(f"{i}. {cnt['name']} | {cnt['phone']} | {cnt['email']}")


def search_contact(contacts):
    if len(contacts) == 0:
        print("No contacts found.")
        return

    name = input("Enter contact name to search: ").lower()
    found = False

    for cnt in contacts:
        if name in cnt["name"].lower():
            print(f"{cnt['name']} | {cnt['phone']} | {cnt['email']}")
            found = True

    if not found:
        print("No matching contact found.")


def delete_contact(contacts):
    if len(contacts) == 0:
        print("No contacts found.")
        return

    view_contacts(contacts)
    idx = int(input("Enter contact number to delete: "))

    if 1 <= idx <= len(contacts):
        deleted = contacts.pop(idx - 1)
        save_contacts(contacts)
        print(f"Deleted contact: {deleted['name']}")
    else:
        print("Invalid contact number.")


contacts = load_contacts()

while True:
    menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact(contacts)
    elif choice == "2":
        view_contacts(contacts)
    elif choice == "3":
        search_contact(contacts)
    elif choice == "4":
        delete_contact(contacts)
    elif choice == "5":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
