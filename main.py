todos = []

while True:
  user_action = input("Type add, show, edit, complete or exit: ")
  user_action = user_action.strip()

  match user_action:
    case "add":
      todo = input("Add a todo: ")
      todos.append(todo)
    
    case "show":
      for index, item in enumerate(todos):
        print(f"{index + 1}-{item}")
    
    case "edit":
      number = int(input("Number of the todo to edit: "))
       #Adjust for zero indexing
      number -= 1
      new_todo = input("Enter new todo: ")
      # Change todo with new one
      todos[number] =  new_todo

    case "complete":
      number = int(input("Number of the todo to complete: "))
      todos.pop(number - 1)
      
    case "exit":
      break

print("Bye")