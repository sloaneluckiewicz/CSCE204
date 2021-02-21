# Author: Sloane Luckiewicz
# To Dos 

todoList = []
completedList = []

print("Welcome to your todo list!")

while True:
    command = input("(V)iew, (A)dd, (R)emove, or (Q)uit: ").lower().strip()

    if command == "q":
        print("Goodbye")
        break
    
    elif command == "v":
        action = input("View (T)odos or (C)ompleted Items? ") .strip() .lower()
        if action == "t":
            if len(todoList) == 0:
                print("There are no items in the todo list.")
            else:
                for i in range(len(todoList)):
                    print(f"{i+1}. {todoList[i]}")
        elif action == "c":
            if len(todoList) == 0:
                print("There are no items in the todo list.")
            else:
                for i in range(len(completedList)):
                    print(f"{i+1}. {completedList[i]}")
        else:
            print("Invalid input, try again.")
            action = input("View (T)odos or (C)ompleted Items? ") .strip() .lower()
    
    elif command == "a":
        todo = input("Enter todo: ").lower().strip()

        if(todo != "" and (todo in todoList) == False):
            todoList.append(todo)
        else:
            print("Todo already in the list")

    elif command == "r":
        todo = input("Enter completed: ") .lower() .strip()
        if todo in todoList:
            todoList.remove(todo)
            completedList.append(todo)
        else:
            print(f"Sorry, {todo} is not in your list.")
    
    else:
        print("Invalid command")
        command = input("(V)iew, (A)dd, (R)emove, or (Q)uit: ").lower().strip()
    
