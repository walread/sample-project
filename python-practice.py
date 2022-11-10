import random
import sys

x = sys.argv[1]
y = sys.argv[2]

answer = random.randint(int(x), int(y))
print(answer)

while True:
    try:
        guess = int(input("Guess a number between 1 and 10: "))
        if guess == answer:
            print("Correct")
            break
        else:
            print("Incorrect")
    except ValueError:
        print("Please enter a number")
        continue
