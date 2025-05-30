import os
import pickle

class Employee:
    def __init__(self, name: str = "default Name", id: int = 0, salary: float = 0.0) -> None:
        self.name = name
        self.id = id
        self.salary = salary

    def __str__(self):
        return "{0:^10d} {1:^10s} {2:^10.2f}".format(self.id, self.name, self.salary)

def insert_employee():
    name, id, salary = input("Enter name id salary: ").split()
    new_emp = Employee(name, int(id), float(salary))
    with open("employees.dat", "ab") as f:
        pickle.dump(new_emp, f)

def delete_employee():
    target_id = int(input("Enter Employee ID to delete: "))
    found = False

    # خواندن از فایل اصلی و نوشتن در فایل موقت
    try:
        with open("employees.dat", "rb") as f_in, open("temp.dat", "wb") as f_out:
            while True:
                try:
                    emp = pickle.load(f_in)
                    if emp.id != target_id:
                        pickle.dump(emp, f_out)
                    else:
                        found = True
                except EOFError:
                    break
    except FileNotFoundError:
        print("Employee file not found.")
        return

    # جایگزینی فایل‌ها
    if found:
        os.remove("employees.dat")
        os.rename("temp.dat", "employees.dat")
        print("Delete Successful")
    else:
        os.remove("temp.dat")
        print("Employee Not Found!")

def update_employee():
    target_id = int(input("Enter Employee ID to update: "))
    found = False

    try:
        with open("employees.dat", "rb") as f_in, open("temp.dat", "wb") as f_out:
            while True:
                try:
                    emp = pickle.load(f_in)
                    if emp.id == target_id:
                        print(f"Current Info → Name: {emp.name}, Salary: {emp.salary}")
                        new_name = input("Enter new name: ")
                        new_salary = float(input("Enter new salary: "))
                        emp.name = new_name
                        emp.salary = new_salary
                        found = True
                    pickle.dump(emp, f_out)
                except EOFError:
                    break
    except FileNotFoundError:
        print("Employee file not found.")
        return

    if found:
        os.remove("employees.dat")
        os.rename("temp.dat", "employees.dat")
        print("Update Successful")
    else:
        os.remove("temp.dat")
        print("Employee Not Found!")

def show_all():
    print("{0:^10s} {1:^10s} {2:^10s}".format("ID", "Name", "Salary"))
    try:
        with open("employees.dat", "rb") as f:
            while True:
                try:
                    emp = pickle.load(f)
                    print(emp)
                except EOFError:
                    break
    except FileNotFoundError:
        print("No employee file found.")

# منوی اصلی
while True:
    choice = input("1-Add Employee\n2-Delete Employee\n3-Update Employee\n4-Show All Employees\n5-Exit\n-> ")

    match choice:
        case "1":
            insert_employee()
        case "2":
            delete_employee()
        case "3":
           update_employee()
        case "4":
            show_all()
        case "5":
            break
        case _:
            print("Invalid choice.")
