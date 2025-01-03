import tkinter as tk

class NoteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Note Array")
        self.root.configure(bg="#333333")
        self.notes = []  # Store note data
        self.note_frames = []  # Store reference to note frames
        self.note_expanded = []  # Store expansion state
        # self.create_note_array()
        
        frame = tk.Frame(self.root, bg="#333333")
        frame.pack(expand=True, fill="both")
        self.add_note(frame, 0, 0)
        
    def create_note_array(self):
        # Create a grid layout for notes
        frame = tk.Frame(self.root, bg="#333333")
        frame.pack(expand=True, fill="both")
        
        for i in range(9):  # Creating a 3x3 grid
            row = i // 3
            col = i % 3
            self.add_note(frame, row, col)

    def add_note(self, parent, row, col):
        # Default size for collapsed note
        note_frame = tk.Frame(parent, width=100, height=100, bg="#444444", bd=2, relief="raised")
        note_frame.grid(row=row, column=col, padx=10, pady=10)
        
        note_text = tk.Text(note_frame, wrap="word", bg="#555555", fg="#FFFFFF", 
                            width=10, height=5, bd=0, highlightthickness=0)
        note_text.insert("1.0", f"Note {row * 3 + col + 1}")
        note_text.pack(expand=True, fill="both")
        note_text.config(state="disabled")  # Disable editing when collapsed
        
        self.notes.append(note_text)
        self.note_frames.append(note_frame)
        self.note_expanded.append(False)
        
        note_frame.bind("<Button-1>", lambda event, index=row*3+col: self.toggle_note(index))

    def toggle_note(self, index):
        # Toggle between expanded and collapsed state
        if self.note_expanded[index]:
            # Collapse note
            self.note_frames[index].configure(width=100, height=100)
            self.notes[index].configure(width=10, height=5)
            self.notes[index].config(state="disabled")
        else:
            # Expand note
            self.note_frames[index].configure(width=300, height=200)
            self.notes[index].configure(width=40, height=10)
            self.notes[index].config(state="normal")
        
        self.note_expanded[index] = not self.note_expanded[index]

if __name__ == "__main__":
    root = tk.Tk()
    app = NoteApp(root)
    root.mainloop()