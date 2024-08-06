from functions import get_todos, write_todos
import time

taim = time.strftime("%b %d, %Y %H:%M:%S")
print(taim)
while True:
    user_pr = input("Type add, show, edit(eg. edit 3), complete or exit: ")
    user_pr = user_pr.strip()


    if user_pr.startswith("add"):
        todo = user_pr[4:] + "\n"
        todos = get_todos()
        todos.append(todo)
        write_todos(todos)

    elif user_pr.startswith("show") or user_pr.startswith("display"):
        todos = get_todos()

        for index,items in enumerate(todos):
            items = items.strip("\n")
            print(f"{index+1}-{items}")

    elif user_pr.startswith("edit"):
        try:
            inp = int(user_pr[5])
            inp = inp-1
            todos = get_todos()
            print("These are the existing todos",todos)
            inp2 = input("Enter a new todo: ")
            todos[inp] = inp2 + "\n"
            print("New todos are", todos)
            write_todos(todos)
        except ValueError:
            print("Command you entered is invalid")
            continue
        except IndexError:
            print("The number you have entered exceeds the number of todos!")

    elif user_pr.startswith("complete"):
        try:
            inp3 = int(user_pr[9:])
            todos = get_todos()
            num = inp3-1
            todos.pop(num)
            write_todos(todos)
        except IndexError:
            print("The number you have entered exceeds the number of todos!")
            continue

    elif user_pr.startswith("exit"):
        break

    else:
        print("Please enter a valid command!")

print("adios")
