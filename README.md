# Python/SQL Exercise

This project is an exercise for writing bot Python and SQL scripts

It was written and tested using Python 3.8.8, and on a Windows machine

The module pyodbc is needed to use the programs, 
	and can be found with "pip install pyodbc"

The completed requirements are listed below:

# description: |
  You will create an Employee Management System using Python Scripts and SQL commands
  The employee Data should be use fully Normalized Data
projects:
- Python:
  - Create Python scripts to read in user input for Employees, Addresses, and Departments
  - The Manager should also be an employee
  - Each Python Script should output data as CSV
  - Export Departments as a YAML file
- SQL:
  - Create tables for Employee, Address, and Department 
  - Import your CSV data that you created for the Python portion
  - commands:
    - The full data for each Employee with their address as a string, department name, and manager name
    - the 5 highest paid and lowest paid employees
    - The total salary for each department, the manager's name, sorted by highest total
    - Each employee that lives in a given state (The state can be hard coded for now)
- Bonus:
  - scripts:
    - Create a Python Script that will create the tables automatically
    - Create a Python Script that will read any CSV file and write the data to the database
    - Create a Python script that can execute each of the required SQL commands
    - Export the results of the SQL queries to CSV, and YAML
data: 
- employees:
  - id
  - name
  - age
  - salary
  - department id
  - address id
  - manager id
- address:
  - id
  - street
  - city
  - state
- department:
  - id
  - name
  - manager id
  - headquarters address id
