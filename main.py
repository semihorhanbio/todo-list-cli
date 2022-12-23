while True:
  user_action = input("Type add, show, edit, complete or exit: ")
  user_action = user_action.strip()

  
  if "add" in user_action:
    todo = input("Add a todo: ") + "\n"
    
    with open("todos.txt", "r") as file:
      todos = file.readlines()
    
      todos.append(todo)
    
    with open("todos.txt", "w") as file:
      file.writelines(todos)
  
  elif "show" in user_action:
    with open("todos.txt", "r") as file:
      todos =  file.readlines()
    
    for index, item in enumerate(todos):
      item = item.strip("\n")
      print(f"{index + 1}-{item}")
  
  elif "edit" in user_action:
    number = int(input("Number of the todo to edit: "))
    #Adjust for zero indexing
    number -= 1
    new_todo = input("Enter new todo: ")
    with open("todos.txt", "r") as file:
      todos =  file.readlines()
    
    # Change todo with new one  
    todos[number] =  new_todo + "\n"
    
    with open("todos.txt", "w") as file:
      file.writelines(todos)
  
  elif "complete" in user_action:
    number = int(input("Number of the todo to complete: "))
    with open("todos.txt", "r") as file:
      todos = file.readlines()
    
    removed_todo = todos.pop(number - 1).strip("\n")
    
    with open("todos.txt", "w") as file:
      file.writelines(todos)
    
    print(f"Todo {removed_todo} was removed from the list")
  
  elif "exit" in user_action:
    break

print("Bye")