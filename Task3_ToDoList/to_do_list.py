import json
import os
from datetime import datetime
try: 
    from colorama import Fore,Style
    color_enabled=True
except ImportError:
    color_enabled=False

tasks_file="tasks.json"

def load_tasks():
    if not os.path.exists(tasks_file):
        return []
    with open(tasks_file,'r') as file:
        return json.load(file)
    
def save_tasks(tasks):
    with open(tasks_file,'w') as file:
        json.dump(tasks,file,indent=4)

def add_task():
    task=input("Enter task description: ").strip()
    if not task:
        print("Task cannot be empty.")
        return
    timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    tasks=load_tasks()
    tasks.append({
        "task":task,
        "completed":False,
        "created_at":timestamp
    })
    confirm=input("Save this task? (y/n): ").strip().lower()
    if confirm == 'y':
        save_tasks(tasks)
        print("Task added successfully.")
    else:
        print("Task not saved.")

def view_tasks():
    tasks=load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    tasks.sort(key=lambda t:(t["completed"],t.get("created_at","")))
    print("\n--- To-Do List ---")
    for i,t in enumerate(tasks,1):
        status="✔️ Done" if t["completed"] else "⏳ Pending"
        created=t.get("created_at","Unknown")
        completed=t.get("completed_at",None)
        if color_enabled:
            color=Fore.GREEN if t["completed"] else Fore.YELLOW
            status_display=f"{color}{status}{Style.RESET_ALL}"
        else:
            status_display=status
            
        print(f"{i}. {t['task']} [{status_display}]")
        print(f"   Created: {created}")
        if completed:
            print(f"   Completed: {completed}")
        print("-"*40)
            
def mark_completed():
    tasks=load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    
    view_tasks()
    try:
        index=int(input("Enter task number to mark as complete: "))-1
        if 0<=index<len(tasks):
            task=tasks[index]
            if task["completed"]:
                print(f"Task '{task['task']}' is already marked as completed.")
                return
            
            confirm=input(f"Mark task '{task['task']}' as completed? (y/n): ")
            if confirm=='y':
                task['completed']=True
                task["completed_at"]=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                save_tasks(tasks)
                print(f"✔️ Task'{task['task']}' marked as completed as {task['completed_at']}.")
            else:
                print("Operation cancelled.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
        
def delete_task():
    tasks=load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    tasks.sort(key=lambda t:(t["completed"],t.get("created_at","")))
    view_tasks()
    try:
        index=int(input("Enter task number to delete: "))-1
        if 0<=index<len(tasks):
            task=tasks[index]
            confirm= input(f"Are you sure you want to delete task '{task['task']}'? (y/n): ").strip().lower()
            if confirm =='y':
                removed=tasks.pop(index)
                save_tasks(tasks)
                print(f"Deleted task: {removed['task']}")
            else:
                print("Deletion cancelled.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")
        try:
            choice=int(input("Select an option: "))
        except ValueError:
            print("Please enter a number between 1 and 5.")
            continue
        
        if choice==1:
            add_task()
        elif choice==2:
            view_tasks()
        elif choice==3:
            mark_completed()
        elif choice==4:
            delete_task()
        elif choice==5:
            print("Session ended. Your tasks are saved.")
            break
        else:
            print("Invalid option. Please try again.")
            
if __name__=="__main__":
    main()
