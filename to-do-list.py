tasks = []

def execute():
  while True:
    print("-----------TO DO LIST------------")
    print("Choose One Option")
    print("1. Add Task")
    print("2. See Tasks")
    print("3. Set task as done or remove it")
    print("4. Quit Programme")
    print(" ")
    chosen = input("Choose the action: ")

    if chosen == "1":
      add_task()

    if chosen == "2":
      see_tasks()
    
    if chosen == "3":
      set_done()

    if chosen == "4":
      quit()


def add_task():
  task = input("Name tasks: ")
  tasks.append(task)
  print("\nTask added successfully!\n")

  
def set_done():
  validate = len(tasks) > 0 
  if validate:
    num = int(input("Which one do you want to mark as done? (Number)"))
    if 0 <= num < len(tasks):
      if not tasks[num].endswith(" - (DONE) "):
          tasks[num] += " - (DONE) " 
          print(f"Task marks how done!\n")
      else:
        tasks[num] = tasks[num].replace(" - (DONE) ", " ")
        print(f"Task marked undone!\n")
    else:
      print("Número de tarefa inválido!\n")
  else:
    print("Withou task added!\n")

def see_tasks():
  validate = len(tasks) > 0 
  
  if validate:
    print("\nTasks:")
    for tk in tasks:
      print(tk) 
  else: 
    print("\nNo Tasks... Add at least one!\n") 
    return


execute()
