import tkinter as tk
from tkinter import ttk, messagebox

class Student:
    def _init_(self, name, sap_id, grades=None):
        self.name = name
        self.sap_id = sap_id
        self.grades = grades if grades else []

    def add_grade(self, grade):
        self.grades.append(grade)

    def remove_grade(self, index):
        del self.grades[index]

    def update_grade(self, index, new_grade):
        self.grades[index] = new_grade

    def display_grades(self):
        return "\n".join(self.grades)

def save_data(students):
    with open("student_data.txt", "w") as f:
        for student in students:
            f.write(f"{student.name}:{student.sap_id}:" + ",".join(student.grades) + "\n")

def load_data():
    students = []
    try:
        with open("student_data.txt", "r") as f:
            for line in f:
                parts = line.strip().split(":")
                name = parts[0]
                sap_id = parts[1]
                grades = parts[2].split(",") if len(parts) > 2 else []
                students.append(Student(name, sap_id, grades))
    except FileNotFoundError:
        pass
    return students

def add_student():
    name = entry_name.get()
    sap_id = entry_sap_id.get()
    students.append(Student(name, sap_id))
    update_table()
    messagebox.showinfo("Success", f"Student {name} added successfully.")

def display_grades():
    name = entry_name.get()
    for student in students:
        if student.name == name:
            messagebox.showinfo(f"{name}'s Grades", student.display_grades())
            break
    else:
        messagebox.showerror("Error", "Student not found.")

def save_and_exit():
    save_data(students)
    messagebox.showinfo("Success", "Data saved. Exiting...")
    root.destroy()

def update_table():
    for i in tree.get_children():
        tree.delete(i)
    for student in sorted(students, key=lambda x: x.name):
        tree.insert("", "end", values=(student.name, student.sap_id, student.display_grades()))

def add_grade():
    name = entry_name.get()
    sap_id = entry_sap_id.get()
    grade = entry_grade.get()
    for student in students:
        if student.name == name and student.sap_id == sap_id:
            student.add_grade(grade)
            update_table()
            messagebox.showinfo("Success", f"Grade {grade} added for {name}.")
            return
    messagebox.showerror("Error", "Student not found.")

def sort_by_name():
    students.sort(key=lambda x: x.name)
    update_table()

def sort_by_sap_id():
    students.sort(key=lambda x: x.sap_id)
    update_table()

students = load_data() 

root = tk.Tk()
root.title("Student Grade Management")

label_name = tk.Label(root, text="Student Name:")
label_name.grid(row=0, column=0)

entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

label_sap_id = tk.Label(root, text="Sap ID:")
label_sap_id.grid(row=1, column=0)

entry_sap_id = tk.Entry(root)
entry_sap_id.grid(row=1, column=1)

label_grade = tk.Label(root, text="Grade:")
label_grade.grid(row=2, column=0)

entry_grade = tk.Entry(root)
entry_grade.grid(row=2, column=1)

button_add_student = tk.Button(root, text="Add Student", command=add_student)
button_add_student.grid(row=3, column=0, columnspan=2, pady=5)

button_add_grade = tk.Button(root, text="Add Grade", command=add_grade)
button_add_grade.grid(row=4, column=0, columnspan=2, pady=5)

button_display = tk.Button(root, text="Display Grades", command=display_grades)
button_display.grid(row=5, column=0, columnspan=2, pady=5)

button_exit = tk.Button(root, text="Save and Exit", command=save_and_exit)
button_exit.grid(row=6, column=0, columnspan=2, pady=5)

button_sort_name = tk.Button(root, text="Sort by Name", command=sort_by_name)
button_sort_name.grid(row=7, column=0, pady=5)

button_sort_sap_id = tk.Button(root, text="Sort by Sap ID", command=sort_by_sap_id)
button_sort_sap_id.grid(row=7, column=1, pady=5)

columns = ("Name", "Sap ID", "Grades")
tree = ttk.Treeview(root, columns=columns, show="headings")
tree.grid(row=8, column=0, columnspan=2)

tree.heading("Name", text="Name")
tree.heading("Sap ID", text="Sap ID")
tree.heading("Grades", text="Grades")

update_table()

root.mainloop()