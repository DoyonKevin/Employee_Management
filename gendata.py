#Kevin Doyon
#Python/SQL Assignment

#Prompts users to generate employees
def gen_employ():
    """Allows user to generate employees"""
    employees = []
    employ_id = 1
    #Asks for the number of employees to generate
    while(True):
        try:
            num_employ = int(input("How many employees do you want to create?: "))
        except ValueError:
            print("Please input an integer for the number of employees")
        else:
            break

    #Makes the number of employees requested
    while(num_employ>=employ_id):
        print('-------------------------------------------------')
        try:
            temp_employ = {
                'employ_id': employ_id,
                'employ_name':input("Enter an employee name: "),
                'employ_age':int(input("Enter the employee's age: ")),
                'employ_salary':int(input("Enter the employee's salary: ")),
                'depart_id':int(input("Enter the department the employee works for: ")),
                'address_id':int(input("Enter the employee's address ID: ")),
                'manager_id':int(input("Enter the employee's manager ID: ")),
            }
        except ValueError:
            pass
        else:
            print(f"This employee's ID is {employ_id}")
            employees.append(temp_employ)
            employ_id +=1

    return employees



#Prompts users to generate departments
def gen_depart():
    """Allows users to generate departments"""
    depart_id = 1
    departments = []

    #Asks for the number of departments to be generated
    while(True):
        try:
            num_depart = int(input("How many departments do you want to create?: "))
        except ValueError:
            print("Please input an integer for the number of deparments")
        else:
            break
    
    #Makes the number of departments requested
    while(num_depart>=depart_id):
        print('-------------------------------------------------')
        try:
            temp_depart = {
                'depart_id':depart_id,
                'depart_name':input("What is the name for the department: "),
                'depart_manage':int(input("What is the manager's ID: ")),
                'depart_address':int(input("Enter the department's address ID: ")),
            }
        except ValueError:
            pass
        else:
            print(f"This department's ID is {depart_id}")
            departments.append(temp_depart)
            depart_id +=1
    return departments



#Prompts users to generate addresses
def gen_address():
    """Allows users to generate addressess"""
    addressess = []
    address_id = 1

    #Asks for the number of departments to be generated
    while(True):
        try:
            num_address = int(input("How many addresses do you want to create?: "))
        except ValueError:
            print("Please input an integer for the number of deparments")
        else:
            break

    #Makes the number of addresses requested
    while(num_address>=address_id):
        print('-------------------------------------------------')
        try:
            temp_address = {
                'address_id':address_id,
                'street_name':input("What is the Street name: "),
                'city_name':input("What is the City name: "),
                'state_name':input("What is the State name: "),
            }
        except ValueError:
            pass
        else:
            print(f"This address's ID is {address_id}")
            addressess.append(temp_address)
            address_id +=1
    return addressess




if __name__ == '__main__':
    print("This is gendata to generate data")