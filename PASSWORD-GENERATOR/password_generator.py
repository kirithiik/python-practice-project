import random
import string

def password_generator(length):
  characters = string.ascii_letters + string.digits + string.punctuation
  password=""
  for i in range(length):
    password+=random.choice(characters)
  return password


def main():
  length=int(input("Enter the desired password length: "))
  if length < 4:
    print("Password length should be atleast 4 characters.")
  elif length > 64:
    print("Password length should not exceed 64 characters.")
  else: 
    password=password_generator(length)  
    print("Generated Password: ",password)

if __name__ == "__main__":
  main()