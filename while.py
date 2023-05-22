import random
user_number = None
random_number = random.randint(1,10)
i = 1
game = True
while user_number != random_number:
    user_number = int(input("Enter number between 1 and 10: "))

    if user_number == random_number:
        print("you win")

    elif user_number > random_number:
        print("Wrong choice, Your number is larger")

    elif user_number < random_number:
        print("Wrong choice, Your number is smaller")
    
    print(f"Unlucky person you failed {i} times")
    i+=1
# print("Thanks for playing my game")