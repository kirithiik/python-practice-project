from datetime import datetime
def add_expense(expenses):
  amount=float(input("enter the amount: "))
  category=input("enter the category: ")
  note=input("enter the note: ")

  expense={
    "amount": amount,
    "category": category,
    "note": note,
    "time": datetime.now().strftime("%d-%m-%Y %H:%M")
  }
  expenses.append(expense)

def view_expenses(expenses):
  if len(expenses)==0:
    print("no expenses found")
    return
  
  for i,exp in enumerate(expenses,start=1):
    print(i,exp["amount"],exp["category"],exp["note"],exp["time"])

def total_expenses(expenses):
  total = 0
  for exp in expenses:
    total+=exp["amount"]
  print("Total expenses:",total)

def delete_expense(expenses):
  view_expenses(expenses)
  idx = int(input("enter expense number to delete : "))
  if 1<=idx <=len(expenses):
    removed=expenses.pop(idx-1)
    print("Deleted: ",removed)
  else:
    print("invalid input")
expenses = []
def menu():
  print("1. Add expense")
  print("2. View expenses")
  print("3. Total expense")
  print("4. Delete expense")
  print("5. Exit")

while True:
  menu()
  choice=input("enter your choice")
  if choice=="1":
    add_expense(expenses)
  elif choice=="2":
    view_expenses(expenses)
  elif choice=="3":
    total_expenses(expenses)
  elif choice=="4":
    delete_expense(expenses)
  elif choice=="5":
    print("....exiting....")
    break
  else:
    print("invalid input")