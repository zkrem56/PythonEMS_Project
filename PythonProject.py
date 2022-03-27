#Import Modules
import csv
import re
from pprint import pprint

#Creating Custom Exception Classes
class AgeException(Exception): pass
class NumberEmployeesException(Exception): pass
class NotAnOptionException(Exception): pass

class Employee:
    #Adds an Employee
    def addEmployee():
        max_employees = 3
        employees = []
        header = []

        #Get data employee data from employee2.csv
        try:
            with open("./resources/employee2.csv", "rt") as file:
                reader = csv.DictReader(file, ["id","First Name","Last Name","age","Date of Employment","Salary","Department"])
                header = next(reader)
                for row in reader:
                    employees.append(row)
        except FileNotFoundError: print("File Not Found")

        while True:
            try:
                #Gets employee name
                employNum = int(input("Enter number of employees you will add: "))
            
                #Check to see if employNum is over 20 and through exception
                if employNum > max_employees:
                    raise NumberEmployeesException

            except ValueError:
                print("Integer was not entered")
            except NumberEmployeesException:
                print(f"You cannot enter more than {max} employees")
            else: break
        
        for i in range(employNum):
            try:
                age = int(input("Enter your age: "))
                if age < 18:
                    raise AgeException

                #birthYear = date.today().year - age
                
                firstName, lastName = input("Enter your name with a space in the middle: ").split()
                firstName = firstName.capitalize()
                lastName = lastName.capitalize()

                #name = firstName + " " + lastName
                #email = f"{firstName}.{lastName}{birthYear%100}@company.com"
                while True:
                    datofemploy = input("Enter Date of Employment (mm-dd-yyyy): ")

                    #Gets if the regex statement matches
                    match = re.search("^\d{2}\-\d{2}\-\d{4}$", datofemploy)
                    if match:
                        break
                    else:
                        print("Please enter correct format mm-dd-yy")
                
                while True:
                    try: 
                        salary = int(input("Enter employee salary: "))
                        break
                    except ValueError: print("Enter a integer")
                
                department = input("Enter department employee is in: ")
            
                #Gets new Id
                id = Employee.assignId(employees)

                employees.append(dict({"id": id, "First Name": firstName, "Last Name": lastName, "age": age, "Date of Employment": datofemploy, "Salary": salary, "Department": department}))

            except ValueError: print("Enter a Integer")
            except AgeException:
                print("You are too young")
                continue
            

        try:
            with open("./resources/employee2.csv", "wt", newline="") as file:
                header = employees[0].keys()
                writer = csv.DictWriter(file, header)
                writer.writeheader()
                writer.writerows(employees)
        except FileNotFoundError: print("File Not Found")
        #except: print("Something went wrong")

#===============================================================================================================

    #Update an Employees information

    def updateEmployee():
        employees = []
        header = []

        try:
            with open("./resources/employee2.csv", "rt") as file:
                reader = csv.DictReader(file, ["id","First Name","Last Name","age","Date of Employment","Salary","Department"])
                header = next(reader)
                for row in reader:
                    employees.append(row)
        except FileNotFoundError: print("File Not Found")

        print("Employees: ")
        for i in range(len(employees)):
            id = int(employees[i].get("id"))
            firstName = employees[i].get("First Name")
            lastName = employees[i].get("Last Name")

            print(f"{id}: {firstName} {lastName}")

            
        #pprint(employees)

        while True:
            try: 
                numId = int(input("Enter the id of the employee that you want to update: "))
                break
            except ValueError: print("Did not enter a integer")
        
        print("What would you like to change:")
        print("1 First Name\n2 Last Name\n3 Department\n4 Salary\n5 Age\n6 Date of Employment")

        while True:
            try: 
                choice = int(input("Enter number for what you want to change: "))
                if choice < 1 or choice > 5:
                    raise NotAnOptionException
                break
            except ValueError: print("Did not enter an Integer") #Makes sure number is an int
            except NotAnOptionException: print("You did not enter a option") #Makes sure the user chooses an option
        
        for i in range(len(employees)):
            print(i)
            if numId == int(employees[i].get("id")):
                if choice == 1:
                    firstName = input("Enter new First name: ")
                    employees[i].update({"First Name":firstName})
                elif choice == 2:
                    lastName = input("Enter new Last Name: ")
                    employees[i].update({"Last Name":lastName})
                elif choice == 3:
                    department = input("Enter new Department: ")
                    employees[i].update({"Department":department})
                elif choice == 4:
                    while True:
                        try:
                            salary = int(input("Enter new Salary: "))
                            break
                        except ValueError: print("Enter a Integer")
                    employees[i].update({"Salary":salary})
                elif choice == 5:
                    while True:
                        try:
                            age = int(input("Enter new Age: "))
                        except ValueError: print("Enter a Integer")
                    employees[i].update({"age":age})
                break
        

        try:
            with open("./resources/employee2.csv", "wt", newline="") as file:
                writer = csv.DictWriter(file, header)
                writer.writeheader()
                writer.writerows(employees)
                print("Database updated Successful")
        except FileNotFoundError: print("File Not Found")
        #except: print("Something went wrong")

#============================================================================================

    #Delete Employee method

    def deleteEmployee():
        employees = []
        header = []
        try:
            with open("./resources/employee2.csv", "rt") as file:
                reader = csv.DictReader(file, ["id","First Name","Last Name","age","Date of Employment","Salary","Department"])
                header = next(reader)
                for row in reader:
                    employees.append(row)
        except FileNotFoundError: print("File Not Found")

        print("Here are the employees:")
        for i in range(len(employees)):
            id = int(employees[i].get("id"))
            firstName = employees[i].get("First Name")
            lastName = employees[i].get("Last Name")
            print(f"{id}: {firstName} {lastName}")

        numId = int(input("Enter id of employee you want to delete: "))
        for i in range(len(employees)):
            if int(employees[i].get("id")) == numId:
                employees.pop(i)
                break

        try:
            with open("./resources/employee2.csv", "wt", newline="") as file:
                writer = csv.DictWriter(file, header)
                writer.writeheader()
                writer.writerows(employees)
                print("Remove of Employee was successful")
        except FileNotFoundError: print("File Not Found")
        #except: print("Something went wrong")

##################################################################################################


    #Show Employee method

    def getEmployee():
        employees = []
        displayDept = []
        try:
            with open("./resources/employee2.csv", "rt") as file:
                reader = csv.DictReader(file, ["id","First Name","Last Name","age","Date of Employment","Salary","Department"])
                header = next(reader)
                for row in reader:
                    employees.append(row)
        except FileNotFoundError: print("File Not Found") 

        #Ask user question if the user wants to serach for employee by department
        dpart = input("Do you want to search for employee by department (y (Yes), n (No):")
        if dpart == "y":
            dpartList = []

            print("Getting Departments")
            dpartList = [dp.get("Department") for dp in employees]

            pprint(set(dpartList))
            
            dpartName = input("Which department would you like to see: ")
            
            displayDept = [dp for dp in set(dpartList) if dp == dpartName]

            print(displayDept)



        while True:
            print("Employee List:")
            for i in range(len(employees)):
                if not displayDept:
                    id = employees[i].get("id")
                    firstName = employees[i].get("First Name")
                    lastName = employees[i].get("Last Name")
                    print(f"{id}: {firstName} {lastName}")
                else:
                    if displayDept[0] == employees[i].get("Department"):
                        id = employees[i].get("id")
                        firstName = employees[i].get("First Name")
                        lastName = employees[i].get("Last Name")
                        print(f"{id}: {firstName} {lastName}")

            numId = int(input("Enter Id of employee you want to see information on:"))

            for i in range(len(employees)):

                if numId == int(employees[i].get("id")):
                    pprint(employees[i])
                    break

            choice = int(input("Do you want to view another employee (1 yes, 2 no: "))
            if choice == 2:
                break



    def assignId(empList = []):
        max = 0
        for i in range(len(empList)):
            if max < int(empList[i].get("id")):
                max = int(empList[i].get("id"))
        
        return max+1


def main():
    employee = []
    while True:
        print("Welcome to the Employee Menu:")
        print("1 Add Employee\n2 Update Employee\n3 Delete Employee\n4 Show Employee\n5 Exit")
        
        while True:
            try:
                choice = int(input("Enter the function you want to do: "))
                break
            except ValueError: print("Need to enter a Integer")
        
        try:
            if choice == 1:
                Employee.addEmployee()
            elif choice == 2:
                Employee.updateEmployee()
            elif choice == 3:
                Employee.deleteEmployee()
            elif choice == 4:
                Employee.getEmployee()
                pprint(employee)
            elif choice == 5:
                print("Have a nice day!")
                exit(0)
            else:
                raise NotAnOptionException
        except NotAnOptionException: print("You did not enter a choice")


#Runs the program
main()