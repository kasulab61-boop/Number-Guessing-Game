import random

print("=== Number Guessing Game ===")

# Difficulty selection
print("Choose Difficulty Level:")
print("1. Easy (1 to 50)")
print("2. Medium (1 to 100)")
print("3. Hard (1 to 200)")

choice = int(input("Enter your choice (1/2/3): "))

# Set range based on choice
if choice == 1:
    max_num = 50
elif choice == 2:
    max_num = 100
else:
    max_num = 200

# Generate random number
number = random.randint(1, max_num)

attempts = 0

print(f"\nGuess a number between 1 and {max_num}")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("🎉 Correct!!! You guessed it!")
        print("Number of attempts:", attempts)
        break