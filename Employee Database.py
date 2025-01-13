import tkinter as tk
import ttkbootstrap as ttk
from PIL import Image, ImageTk

# Initialize an empty dictionary for employees
Employee = dict()

# Function to add a new record to the dictionary
def add_record():
    emp_id = int(emp_id_entry.get())
    emp_name = emp_name_entry.get()
    emp_dob = emp_dob_entry.get()
    designation = designation_entry.get()

    emp_details = [emp_name, emp_dob, designation]
    Employee[emp_id] = emp_details
    buffer_1['text'] = 'Record Added'
    print("Record Added to Database")

# Function to search for an employee by ID
def search_employee():
    emp_id = int(search_entry.get())
    emp_details = Employee.get(emp_id, "Employee not found")
    search_output.config(text=str(emp_details))

# Function to delete an employee by ID
def delete_employee():
    emp_id = int(delete_entry.get())
    emp_details = Employee.pop(emp_id, "Employee not found")
    delete_output.config(text=str(emp_details))

# Function to display all employees in the dictionary
def display_employees():
    display_output.config(text=str(Employee))

# Create main window
root = ttk.Window(themename = 'darkly')
root.title("Employee Database GUI")
root.geometry('600x700')
root.resizable(False, False)
root.title("Employee Database")

# Load and convert image
image = Image.open('bg3.jpg')
image = ImageTk.PhotoImage(image)

# Create label and configure as background
background_label = tk.Label(root, image=image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


#Heading
entry_label = tk.Label(master=root, text="Employee Database", font="Calibri 20 bold")
entry_label.grid(row=0, column=1)

# Create Labels
emp_id_label = tk.Label(root, text="Employee ID:",font="Calibri 14")
emp_name_label = tk.Label(root, text="Employee Name:", font="Calibri 14")
emp_dob_label = tk.Label(root, text="DOB:", font="Calibri 14")
designation_label = tk.Label(root, text="Designation:", font="Calibri 14")

# Create Entry fields
emp_id_entry = tk.Entry(root, font="Calibri 14")
emp_name_entry = tk.Entry(root, font="Calibri 14")
emp_dob_entry = tk.Entry(root, font="Calibri 14")
designation_entry = tk.Entry(root, font="Calibri 14")

#buffer labels
buffer_1 = tk.Label(root, font="Calibri 14")
buffer_2 = tk.Label(root)
buffer_3 = tk.Label(root)
buffer_4 = tk.Label(root)
buffer_5 = tk.Label(root)
buffer_6 = tk.Label(root, font="Calibri 14")


# Create Buttons
add_button = tk.Button(root, text="Add Record", font="Calibri 14" ,command=add_record)
search_button = tk.Button(root, text="Search Record", font="Calibri 14", command=search_employee)
delete_button = tk.Button(root, text="Delete Record", font="Calibri 14" ,command=delete_employee)
display_button = tk.Button(root, text="Display Record", font="Calibri 14", command=display_employees)

# Create Search, Delete Entry fields, and Output labels
search_entry = tk.Entry(root, font="Calibri 14")
search_output = tk.Label(root, text="", font="Calibri 14")
delete_entry = tk.Entry(root, font="Calibri 14")
delete_output = tk.Label(root, text="", font="Calibri 14")
display_output = tk.Label(root, text="", font="Calibri 14")

# Arrange widgets using grid layout
entry_label.grid(row=0, column=1)
buffer_4.grid(row=1, column=1)
emp_id_label.grid(row=2, column=0)
emp_id_entry.grid(row=2, column=1)
emp_name_label.grid(row=3, column=0)
emp_name_entry.grid(row=3, column=1)
emp_dob_label.grid(row=4, column=0)
emp_dob_entry.grid(row=4, column=1)
designation_label.grid(row=5, column=0)
designation_entry.grid(row=5, column=1)

buffer_6.grid(row=6, column=1)
add_button.grid(row=7, column=1, columnspan=2)
buffer_1.grid(row=8, column=1)

search_entry.grid(row=9, column=1)
search_button.grid(row=10, column=1, columnspan=2)
search_output.grid(row=11, column=0, columnspan=2)
buffer_2.grid(row=12, column=1)

delete_entry.grid(row=13, column=1)
delete_button.grid(row=14, column=1, columnspan=2)
delete_output.grid(row=15, column=0, columnspan=2)
buffer_3.grid(row=16, column=1)

display_button.grid(row=17, column=1, columnspan=2)
display_output.grid(row=18, column=0, columnspan=2)

# Run the Tkinter application
root.mainloop()
