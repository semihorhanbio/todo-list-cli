todos = []

while True:
  user_action = input("Type add, show or exit:")
  user_action = user_action.strip()

  match user_action:
    case "add":
      todo = input("Add a todo:")
      todos.append(todo)
    case "show":
      print("\n".join(todos))
    case "exit":
      break

print("Bye")