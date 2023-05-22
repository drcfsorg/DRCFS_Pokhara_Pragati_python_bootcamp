import random

random_number = random.randint(1,10)
print('Welcome to my game. You have 5 lives to complete it')
for i in range(5):
    user_number = int(input("Enter number between 1 and 10: "))

    if user_number == random_number:
        print("you win")
        break

    elif user_number > random_number:
        print("Wrong choice, Your number is larger")

    elif user_number < random_number:
        print("Wrong choice, Your number is smaller")

    print("lives left: ",5-i-1)

# print("Thanks for playing my game")