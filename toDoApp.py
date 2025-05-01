import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("TodoApp")

width = 400
height = 600
root.geometry(f"{width}x{height}+{int((root.winfo_screenwidth()/2)-(width/2))}+{int((root.winfo_screenheight()/2)-(height/2))}")  # OPEN IN CENTER
root.iconbitmap("icon.ico")
root.resizable(False, False)

heading = ttk.Label(root, text="ALL TASKS", font="arial 16 bold")
heading.pack()

tasksList = []  # Define the tasks list

# Corrected openTask function
def openTask():
    with open('dataBase.txt', 'r') as file:
        tasks = file.readlines()  # Read all lines
    for task in tasks:
        task = task.strip()  # Remove newline character
        if task:  # Check if task is not empty
            listBox.insert(tk.END, task)
            tasksList.append(task)

def addTask(event=None):
    task = tasks.get()
    tasks.delete(0, tk.END)
    if task:
        with open('dataBase.txt', 'a') as file:
            file.write(f"{task}\n")  # Write task to file
        listBox.insert(tk.END, task)
        tasksList.append(task)
       

def deleteList():
    deleteTask = listBox.get(tk.ANCHOR)
    listBox.delete(tk.ANCHOR)
    tasksList.remove(deleteTask)
    with open('dataBase.txt', 'w') as file:
            for task in tasksList:
                file.write(f"{task}\n") 
                
                
                
frame = ttk.Frame(root, width=400, height=50)
tasks = ttk.Entry(frame, font="arial  12", width=30)
frame.pack(pady=12)
tasks.pack()

tasks.bind("<Return>", addTask)

listFrame = ttk.Frame(root, height=250, width=300)
listFrame.pack()

listBox = tk.Listbox(listFrame, font="arial 12", width=40, height=22)
listBox.pack(pady=12)

openTask()  # Load tasks from the file when the app starts

delete = ttk.Button(root, text="Delete", command=deleteList)
delete.pack(side="bottom", pady='15')

root.mainloop()
