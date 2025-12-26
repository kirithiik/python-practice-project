import random

print("Welcome to the Dice Roll Simulator!")

def roll_dice():
    return random.randint(1, 6)

def main():
    roll_count = 0

    while True:
        choice = input("Roll the dice? (y/n): ").lower()

        if choice == 'y':
            result = roll_dice()
            roll_count += 1
            print(f"You rolled a {result}. Total rolls so far: {roll_count}")

        elif choice == 'n':
            print("Exiting the dice simulator.")
            break

        else:
            print("Invalid input. Please enter 'y' or 'n'.")

if __name__ == "__main__":
    main()
