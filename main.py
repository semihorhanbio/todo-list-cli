while True:
  user_action = input("Type add, show, edit, complete or exit: ")
  user_action = user_action.strip()

  
  if user_action.startswith("add"):
    todo = user_action[4:]
    
    with open("todos.txt", "r") as file:
      todos = file.readlines()
    
      todos.append(todo + "\n")
    
    with open("todos.txt", "w") as file:
      file.writelines(todos)
  
  elif "show" in user_action:
    with open("todos.txt", "r") as file:
      todos =  file.readlines()
    
    for index, item in enumerate(todos):
      item = item.strip("\n")
      print(f"{index + 1}-{item}")
  
  elif user_action.startswith("edit"):
    try:
      number = int(user_action[5:])
      #Adjust for zero indexing
      number -= 1
      new_todo = input("Enter new todo: ")
      with open("todos.txt", "r") as file:
        todos =  file.readlines()
      
      # Change todo with new one  
      todos[number] =  new_todo + "\n"
      
      with open("todos.txt", "w") as file:
        file.writelines(todos)
    
    except ValueError:
      print("Your command is not valid")
      continue
      
  elif user_action.startswith("complete"):
    try:
      number = int(user_action[9:])
      with open("todos.txt", "r") as file:
        todos = file.readlines()
      
      removed_todo = todos.pop(number - 1).strip("\n")
      
      with open("todos.txt", "w") as file:
        file.writelines(todos)
      
      print(f"Todo {removed_todo} was removed from the list")
    except IndexError:
      print("There is no number with that item.")
      
  elif user_action.startswith("exit"):
    break
  else:
    print("command not found")

print("Bye")