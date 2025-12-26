def menu():
  print("1. Add")
  print("2. Subtract")
  print("3. Multiply")
  print("4. Divide")
  print("5. Exit")

def add():
  a=float(input("Enter first number: "))
  b=float(input("Enter second number: "))
  print("The sum of numbers is: ",a+b)

def subtract():
  a=float(input("Enter first number: "))
  b=float(input("Enter second number: "))
  print("The difference of numbers is: ",a-b)

def multiply():
  a=float(input("Enter first number: "))
  b=float(input("Enter second number: "))
  print("The product of numbers is: ",a*b)

def divide():
  a=float(input("Enter first number: "))
  b=float(input("Enter second number: "))
  if b==0:
    print("Error: Division by zero is not allowed.")
  else:
    print("The quotient of numbers is: ",a/b)

def main():
  print("Welcome to the Simple Calculator!")
  menu()
  while True:
    n=input("Enter the choice: ")
    if n=="1":
      add()
    elif n=="2":
      subtract()
    elif n=="3":
      multiply()
    elif n=="4":
      divide()
    elif n=="5":
      print("Exiting the calculator.")
      break
    else:
      print("invalid choice. try again")

if __name__ == "__main__":
  main()