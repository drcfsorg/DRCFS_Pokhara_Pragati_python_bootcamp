my_dict = {}
while True:
    print("="*100)
    print("What do you want to do?")
    print("0. exit 1. Get meaning of word 2. add word to dictionary")
    print("="*100)

    option = int(input())
    if option == 1:
        word = input("Enter the Word: ")
        print("*"*100)

        try:
            print(my_dict[word.upper()])
        except KeyError:
            print("WORD not Found on our Dictionary!!")

        print("*"*100)

    if option == 2:
        word = input("Enter Word: ")
        meaning = input("Enter Meaning: ")

        my_dict[word.upper()] = meaning
    if option == 0:
        break

for key,value in my_dict.items():
    print(f"{key.lower()} means: {value}")