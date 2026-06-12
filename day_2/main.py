import os 
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")


connection = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_NAME
)
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS employee (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    age INT,
    department VARCHAR(255),
    salary FLOAT,
    managed_department VARCHAR(255)
)
""")
connection.commit()

class Employee:
    all_employees = []

    def __init__(self, first_name, last_name, age, department, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.department = department
        self.salary = salary
        
        Employee.all_employees.append(self)
        
        cursor.execute(
            "INSERT INTO employee (first_name, last_name, age, department, salary) VALUES (%s, %s, %s, %s, %s)",
            (self.first_name, self.last_name, self.age, self.department, self.salary)
        )
        connection.commit()
        self.db_id = cursor.lastrowid

    def transfer(self, new_department):
        self.department = new_department
        cursor.execute("UPDATE employee SET department = %s WHERE id = %s", (self.department, self.db_id))
        connection.commit()

    def fire(self):
        if self in Employee.all_employees:
            Employee.all_employees.remove(self)
        cursor.execute("DELETE FROM employee WHERE id = %s", (self.db_id,))
        connection.commit()

    def show(self):
        print("First Name:", self.first_name)
        print("Last Name:", self.last_name)
        print("Age:", self.age)
        print("Department:", self.department)
        print("Salary:", self.salary)

    @classmethod
    def List_employees(cls):
        cursor.execute("SELECT * FROM employee")
        records = cursor.fetchall()

        for record in records:
            print(
                f"ID: {record[0]} | "
                f"Name: {record[1]} {record[2]} | "
                f"Age: {record[3]} | "
                f"Department: {record[4]} | "
                f"Salary: {record[5]}"
            )

class Manager(Employee):
    def __init__(self, first_name, last_name, age, department, salary, managed_department):
        super().__init__(first_name, last_name, age, department, salary)
        self.managed_department = managed_department
        cursor.execute(
            "UPDATE employee SET managed_department = %s WHERE id = %s",
            (self.managed_department, self.db_id)
        )
        connection.commit()

    def show(self):
        print("First Name:", self.first_name)
        print("Last Name:", self.last_name)
        print("Age:", self.age)
        print("Department:", self.department)
        print("Salary: confidential")
        print("Managed Department:", self.managed_department)

while True:
    print()
    print("Operations:")
    print("add - Add new employee")
    print("transfer - Transfer employee")
    print("fire - Fire employee")
    print("show - Show employee")
    print("list - List all employees")
    print("q - Exit")
    
    op = input("Enter operation: ")
    
    if op == "q":
        break
    elif op == "add":
        emp_type = input("If manager press 'm' / if employee press 'e': ")
        print("Please insert data")
        first_name = input("First Name:>> ")
        last_name = input("Last Name:>> ")
        age = input("Age:>> ")
        department = input("Department:>> ")
        salary = input("Salary:>> ")
        
        if emp_type == "m":
            managed_department = input("Managed Department:>> ")
            Manager(first_name, last_name, age, department, salary, managed_department)
        elif emp_type == "e":
            Employee(first_name, last_name, age, department, salary)
    elif op == "transfer":
        idx = int(input("Enter employee index: "))
        new_dept = input("Enter new department: ")
        Employee.all_employees[idx].transfer(new_dept)
    elif op == "fire":
        idx = int(input("Enter employee index: "))
        Employee.all_employees[idx].fire()
    elif op == "show":
    
        emp_id = int(input("Enter employee ID: "))

        cursor.execute(
        "SELECT * FROM employee WHERE id = %s",
        (emp_id,)
        )

        employee = cursor.fetchone()

        if employee:
                print(employee)
        else:
            print("Employee not found")
    elif op == "list":
        Employee.List_employees()
