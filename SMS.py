import tkinter as tk
from tkinter import ttk

class StudentManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("STUDENT MANAGEMENT SYSTEM")
        self.root.geometry("1250x1000")
        self.root.configure(bg="lightblue")

        # Dark blue title bar
        title_bar = tk.Label(self.root, text="STUDENT MANAGEMENT SYSTEM", font=("Helvetica", 24, "bold"), bg="#1e3d59", fg="white", padx=10, pady=10)
        title_bar.pack(side="top", fill="x")

        self.students = []

        self.create_gui()

    def create_gui(self):
        # Labels and Entry Boxes
        label_frame = ttk.Frame(self.root, padding=(20, 20))
        label_frame.pack(side="left", padx=20, pady=20)

        labels = ["ID", "NAME", "GENDER", "AGE", "RESULT"]
        entry_boxes = {}

        for i, label_text in enumerate(labels):
            label = ttk.Label(label_frame, text=label_text, foreground="darkblue", font=("Helvetica", 14))
            label.grid(row=i, column=0, sticky="w", pady=10)
            entry_box = ttk.Entry(label_frame, font=("Helvetica", 14))
            entry_box.grid(row=i, column=1, padx=10, pady=10, sticky="ew")
            entry_boxes[label_text] = entry_box

        # Buttons
        button_frame = ttk.Frame(self.root, padding=(20, 20))
        button_frame.pack(side="left", padx=20, pady=20)

        add_button = ttk.Button(button_frame, text="ADD", command=lambda: self.add_to_grid(entry_boxes), style="TButton")
        delete_button = ttk.Button(button_frame, text="DELETE", command=self.delete_grid, style="TButton")
        update_button = ttk.Button(button_frame, text="UPDATE", command=lambda: self.update_grid(entry_boxes), style="TButton")

        add_button.grid(row=0, column=0, pady=10, sticky="ew")
        delete_button.grid(row=1, column=0, pady=10, sticky="ew")
        update_button.grid(row=2, column=0, pady=10, sticky="ew")

        # Treeview (Grid View)
        grid_frame = ttk.Frame(self.root, padding=(20, 20))
        grid_frame.pack(side="right", fill="both", expand=True)

        self.tree = ttk.Treeview(grid_frame, columns=labels, show="headings", selectmode="browse")
        for col in labels:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150, anchor="center")
        self.tree.grid(row=0, column=0, sticky="nsew")

        # Add a vertical scrollbar to the treeview
        vsb = ttk.Scrollbar(grid_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=vsb.set)
        vsb.grid(row=0, column=1, sticky="ns")

        # Configure row and column weights so that they expand proportionally
        grid_frame.grid_rowconfigure(0, weight=1)
        grid_frame.grid_columnconfigure(0, weight=1)

        # Style for the buttons
        style = ttk.Style()
        style.configure("TButton", foreground="white", background="#1e3d59", font=("Helvetica", 12))

    def add_to_grid(self, entry_boxes):
        student_data = [entry.get() for entry in entry_boxes.values()]

        if all(student_data):
            self.students.append(student_data)
            self.update_treeview()
        else:
            tk.messagebox.showerror("Error", "Please fill in all fields.")

    def delete_grid(self):
        selected_item = self.tree.selection()

        if not selected_item:
            tk.messagebox.showwarning("Warning", "Please select a row to delete.")
            return

        # Get the index of the selected item
        index = self.tree.index(selected_item)

        # Delete the selected row from the treeview and the students list
        self.tree.delete(selected_item)
        del self.students[index]

    def update_grid(self, entry_boxes):
        selected_item = self.tree.selection()

        if not selected_item:
            tk.messagebox.showwarning("Warning", "Please select a row to update.")
            return

        # Get the index of the selected item
        index = self.tree.index(selected_item)

        # Get the updated data from entry_boxes
        updated_data = [entry.get() for entry in entry_boxes.values()]

        # Update the data in the students list
        self.students[index] = updated_data

        # Update the treeview
        self.update_treeview()

    def update_treeview(self):
        # Clear existing data
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Insert updated data
        for student in self.students:
            self.tree.insert("", "end", values=student)

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentManagementSystem(root)
    root.mainloop()
