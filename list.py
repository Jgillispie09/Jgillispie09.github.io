# This is a to-do list application
# Its main functionality is to add items to the list, remove items from the list once completed and check remaining tasks on list
# List can handle up to 999 items before issues may occur
# Working to add ability to keep track of completed tasks rather than just deleting them from the application
# Can now keep track of completed tasks
# Input 'x' at main menu to quit program. Input 'x' at any other menu to go back to main menu. *Inputting 'x' on 'Create a new task' menu will not go back to main menu without affecting the list but rather input 'x' as list item.
# This is in case user has need to add letters or variables to the list such as 'x'
# Using the pickle module, list automatically saves at end of each iteration of while loop
# Creating GUI using tkinter

import tkinter as tk
from tkinter import simpledialog, messagebox
import pickle
import os

window = tk.Tk()
window.title("To-Do Organizer")
window.geometry("510x600")

window.columnconfigure([0, 1,], weight=1)
window.rowconfigure([0, 1, 2, 3], weight=1)

task_list = []
completed = []

def save_state():
    global listnum
    with open("task_list.pkl", "wb") as file:
        pickle.dump(task_list, file)
    with open("completed.pkl", "wb") as file:
        pickle.dump(completed, file)
    with open("listnum.txt", "w") as file:
        file.write(str(listnum))

def load_listnum():
    try:
        with open("listnum.txt", "r") as file:
            return int(file.read())
    except (FileNotFoundError, ValueError):
        return 1


listnum = load_listnum()
if listnum == 0:
    listnum = 1

if os.path.exists("task_list.pkl"):
    with open("task_list.pkl", "rb") as file:
        task_list = pickle.load(file)
else:
    task_list = []

if os.path.exists("completed.pkl"):
    with open("completed.pkl", "rb") as file:
        completed = pickle.load(file)
else:
    completed = []



def create_task():
    global listnum
    task = simpledialog.askstring("Create a new task", "Enter a new task: ")
    if task:
        task_list.append(str(listnum) + '.' + ' ' + task)
    elif not task:
        return
    listnum += 1
    #messagebox.showinfo("", f"{task} has been successfully added!")
    update_showlist()
    save_state()

def remove_task():
    global listnum
    task = simpledialog.askinteger("Remove a task", "Enter the task number you would like to remove: ")
    if task and 1 <= task <= len(task_list):
        complete = messagebox.askyesno("", "Would you like to mark this task as complete?")
        if complete:
            if task_list[int(task)-1][1] == '.':
                completed.append(task_list[int(task)-1][3:])
            elif task_list[int(task)-1][2] == '.':
                completed.append(task_list[int(task)-1][4:])
            elif task_list[int(task)-1][3] == '.':
                completed.append(task_list[int(task)-1][5:])
        task_list.remove(task_list[int(task)-1])
        listnum -= 1
        for i in task_list[int(task)-1:]:
            indexnum = task_list.index(i)
            indexval = task_list[indexnum][1:]
            if indexval[0] == '.':
                task_list[indexnum] = str(indexnum + 1) + indexval
            elif indexval[1] == '.':
                indexval = task_list[indexnum][2:]
                task_list[indexnum] = str(indexnum + 1) + indexval
            elif indexval[2] == '.':
                indexval = task_list[indexnum][3:]
                task_list[indexnum] = str(indexnum + 1) + indexval
        update_showlist()
        save_state()

def view_list():
    if task_list:
        update_showlist()
    elif not task_list:
        messagebox.showerror("", "No items are in your list!")

def view_completed_list():
    if completed:
        update_completed()
    elif not completed:
        messagebox.showerror("", "You do not have any completed tasks!")

def delete_list():
    global task_list
    global completed
    global listnum
    certainty = messagebox.askyesno("", "Are you sure you want to delete your list?")
    if certainty:
        messagebox.showwarning("", "Your list has been deleted!")
        task_list = []
        completed = []
        listnum = 1
        save_state()
        update_showlist()
    else:
        pass

def update_showlist():
    showlist.delete(0, tk.END)
    for task in task_list:
        showlist.insert(tk.END, task + "\n")

def update_completed():
    showlist.delete(0, tk.END)
    for task in completed:
        showlist.insert(tk.END, task + "\n")

button_frame = tk.Frame(master=window)
button_frame.grid(row=0, column=0, padx=5, pady=5)
button_create = tk.Button(
    master=button_frame,
    text="Create a new task",
    command=create_task,
)
button_create.grid(row=0, column=0, padx=5, pady=5)
button_remove = tk.Button(
    master=button_frame,
    text="Remove a task",
    command=remove_task
)
button_remove.grid(row=0, column=1, padx=5, pady=5)
button_refresh = tk.Button(
    master=button_frame,
    text="Refresh list",
    command=update_showlist
)
button_refresh.grid(row=0, column=2, padx=5, pady=5)
button_delete_list = tk.Button(
    master=button_frame,
    text="Delete list",
    command=delete_list
)
button_delete_list.grid(row=0, column=3, padx=5, pady=5)
button_show_complete = tk.Button(
    master=button_frame,
    text="Show completed tasks",
    command=view_completed_list
)
button_show_complete.grid(row=0, column=4, padx=5, pady=5)
showlist = tk.Listbox(
    window, 
    height=35, 
    width=80,
)
showlist.grid(row=1,column=0, padx=5, pady=5)
window.after(100, update_showlist())
window.mainloop()


'''while True:
    index = -1
    command = input("Please select a prompt: \n1. Create a new task\n2. Remove a task\n3. View all tasks\n4. View completed tasks\n5. Delete entire list\nType 'x' to return to main menu\n")
    if command == '1':
        create_task()
    elif command == '2':
        remove_task()
    elif command == '3':
        view_list()
    elif command == '4':
        view_completed_list()
    elif command == '5':
        delete_list()
    elif command == 'x' or command == 'X':
        break
    with open("task_list.pkl", "wb") as file:
        pickle.dump(task_list, file)
    with open("completed.pkl", "wb") as file:
        pickle.dump(completed, file)
    save_state()'''
    


