import random

def generate_number(start, end):
    return random.randint(start, end)

def guess_number(start, end):
    return int(input(f"Enter your guess ({start} to {end}): "))

print("🎯 Welcome to Random Number Guessing Game")

start = int(input("Enter the starting range: "))
end = int(input("Enter the ending range: "))

number = generate_number(start, end)

while True:
    ans = guess_number(start, end)

    if ans < start or ans > end:
        print("Out of range! Try again.")
    elif ans < number:
        print("Too Low! Try again.")
    elif ans > number:
        print("Too High! Try again.")
    else:
        print("🎉 Congratulations! You guessed the correct number.")
        break
