tasks = []

def menu():
  print("1. Add task")
  print("2. View task")
  print("3. Mark task as complete")
  print("4. Delete task")
  print("5. Exit")

def Add_task(tasks):
  title=input("Enter the title: ")
  priority=input("Enter priority (High / Medium / Low): ")
  task={
    "title" : title,
    "priority" : priority,
    "completed" : False
  }
  tasks.append(task)
  print("Added successfully")

def View_task(tasks):
  if len(tasks)==0:
    print("no task found")
    return
  for i,task in enumerate(tasks,start=1):
    status ="✔️" if task["completed"] else "❌"
    title = task["title"]
    priority=task["priority"]

    print(f"{i}. [{status}] {title} | priority: {priority}")

  
def Mark_task_as_completed(tasks):
  if len(tasks)==0:
    print("No task is found")
    return
  View_task(tasks)

  idx=int(input("enter the task number"))

  if 1 <= idx <=len(tasks):
    tasks[idx-1]["completed"]=True
    print("Task marked as completed ✔️")
  else:
    print("invalid task number")

def Delete_task(tasks):
  if len(tasks) == 0:
    print("No tasks to delete")
    return
  View_task(tasks)

  idx=int(input("enter the task number: "))
  if 1<=idx<=len(tasks):
    removed = tasks.pop(idx-1)
    print(f"Deleted task: {removed['title']}")
  else: 
    print("Invalid task number")

while True:
  menu()
  choice = int(input("Enter the choice: "))
  if choice==1:
    Add_task(tasks)
  elif choice==2:
    View_task(tasks)
  elif choice==3:
    Mark_task_as_completed(tasks)
  elif choice==4:
    Delete_task(tasks)
  elif choice==5:
    print(".....Exiting.....")
    break
  else:
    print("Invalid input")
  


