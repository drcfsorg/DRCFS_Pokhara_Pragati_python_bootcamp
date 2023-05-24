todo_file = open("todo.txt",'w')

def print_todo(live = None):
    print("*"*100)
    print("You have the following contents on your todo: \n")
    if live is not None:
        for i, todo in enumerate(live):
            print(f"{i+1}. {todo}")
        return 0

    my_file = open('todo.txt','r').readlines()
    for i, todo in enumerate(my_file):
        print(f"{i+1}. {todo}")

todo_list = []
while True:
    print("="*100)
    inp = input("DO you want to add to your todo list?: ")
    print("="*100)

    if ((inp.upper() == "Y") or (inp.upper() == "YES")):
        write = input("Write your todo here: ")
        todo_file.write(write)
        todo_file.write('\n')

        todo_list.append(write)
        print_todo(todo_list)
    else:
        break

todo_file.close()
print_todo()