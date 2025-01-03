import tkinter as tk
from tkinter import messagebox, filedialog

# Initialize the main window
root = tk.Tk()
root.title("Notes and To-Do List")
root.geometry("500x400")


bg_color = "#333333"  # Dark background color
fg_color = "#FFFFFF"  # Light text color
btn_color = "#555555" # Button background color
entry_color = "#444444" # Entry background color

# Apply the dark mode colors to the window
root.configure(bg=bg_color)

# Text area for notes with dark mode
notes_label = tk.Label(root, text="Notes:", bg=bg_color, fg=fg_color)
notes_label.pack()
notes_text = tk.Text(root, height=10, bg=entry_color, fg=fg_color, insertbackground=fg_color)
notes_text.pack()

# To-Do List with dark mode
todo_label = tk.Label(root, text="To-Do List:", bg=bg_color, fg=fg_color)
todo_label.pack()

task_entry = tk.Entry(root, width=40, bg=entry_color, fg=fg_color, insertbackground=fg_color)
task_entry.pack()

task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, bg=entry_color, fg=fg_color)
task_listbox.pack()

# Functions for buttons
def add_task():
    task = task_entry.get()
    if task != "":
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def delete_task():
    try:
        selected_task = task_listbox.curselection()
        task_listbox.delete(selected_task)
    except:
        messagebox.showwarning("Warning", "Please select a task to delete")

def save_notes():
    notes = notes_text.get("1.0", tk.END)
    with filedialog.asksaveasfile(mode='w', defaultextension=".txt") as file:
        file.write(notes)

# Buttons with dark mode
add_task_button = tk.Button(root, text="Add Task", command=add_task, bg=btn_color, fg=fg_color)
add_task_button.pack()

delete_task_button = tk.Button(root, text="Delete Task", command=delete_task, bg=btn_color, fg=fg_color)
delete_task_button.pack()

save_notes_button = tk.Button(root, text="Save Notes", command=save_notes, bg=btn_color, fg=fg_color)
save_notes_button.pack()

# Run the main loop
root.mainloop()