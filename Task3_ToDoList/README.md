# Task 3 – To-Do List CLI App

## 📌 Overview
This is a command-line To-Do List application developed in Python as part of the CODSOFT internship. It allows users to manage tasks with features like adding, viewing, completing, and deleting tasks. Each task includes timestamps and is stored persistently in a JSON file.

## 🚀 Features

- **Add Task**  
  Input task description with timestamp and confirmation before saving.

- **View Tasks**  
  Display all tasks with status (Pending/Done), creation time, and optional completion time. Tasks are sorted by status and creation time.

- **Mark as Completed**  
  Update task status with a completion timestamp and confirmation prompt.

- **Delete Task**  
  Remove tasks safely with confirmation to prevent accidental deletion.

- **Color-Coded Status**  
  Uses `colorama` to highlight task status (green for done, yellow for pending).

- **Persistent Storage**  
  All tasks are saved in `tasks.json` for long-term access.

## 🧰 Technologies Used

- Python
- Built-in modules: `json`, `os`, `datetime`
- Optional: `colorama` for colored output

## 📦 Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
```

## ▶️ How to Run

Run the script using:

```bash
python to_do_list.py
```

## 🎥 Demo Video

Watch the CLI app in action:  
▶️ [To-Do List CLI App – Demo](https://www.linkedin.com/posts/sai-gowtham-2220a7322_codsoft-python-cliapp-activity-7377303082449166336-YXXr?utm_source=social_share_send&utm_medium=android_app&rcm=ACoAAFGG-noBf6Ra_yXj5kk1v4eztQcMwVzOv9c&utm_campaign=whatsapp)

This video highlights the actual **code output** of the program, including:

- Adding tasks with timestamps and confirmation
- Viewing tasks with color-coded status (✔️ Done / ⏳ Pending)
- Marking tasks as completed with completion time
- Deleting tasks safely with confirmation
- Persistent storage in `tasks.json`

Designed for clarity, modularity, and user-friendly interaction.
