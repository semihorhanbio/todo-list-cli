todos = []

while True:
  user_action = input("Type add, show, edit or exit: ")
  user_action = user_action.strip()

  match user_action:
    case "add":
      todo = input("Add a todo: ")
      todos.append(todo)
    case "show":
      print("\n".join(todos))
    case "edit":
      number = int(input("Number of the todo to edit: "))
       #Adjust for zero indexing
      number -= 1
      new_todo = input("Enter new todo: ")
      # Change todo with new one
      todos[number] =  new_todo
    case "exit":
      break

print("Bye")