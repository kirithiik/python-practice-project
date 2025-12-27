def main():
  email = input("Enter your email adress: ")
  if "@" not in email:
    print("Invalid Email Adress")
    return
  username, domain = email.split("@")
  print(f"Username: {username}")
  print(f"Domain: {domain}")


if __name__ == "__main__":
  main()