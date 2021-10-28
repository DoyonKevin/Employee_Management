#Kevin Doyon
#Python/SQL Assignment

import pyodbc
#Creates tables needed for the database
def Createtables(cnxn,employkey,departkeys,addresskeys):
    #Queries need to make the tables
    SQLcommand1 = f"""CREATE TABLE employees(
                        {employkey[0]} INT PRIMARY KEY,
                        {employkey[1]} VARCHAR(100),
                        {employkey[2]} INT,
                        {employkey[3]} INT,
                        {employkey[4]} INT,
                        {employkey[5]} INT,
                        {employkey[6]} INT);"""

    SQLcommand2 = f"""CREATE TABLE departments(
                        {departkeys[0]} INT PRIMARY KEY,
                        {departkeys[1]} VARCHAR(100),
                        {departkeys[2]} INT,
                        {departkeys[3]} INT);"""

    SQLcommand3 = f"""CREATE TABLE addresses(
                        {addresskeys[0]} INT PRIMARY KEY,
                        {addresskeys[1]} VARCHAR(100),
                        {addresskeys[2]} VARCHAR(100),
                        {addresskeys[3]} VARCHAR(100));"""

    
   
   #Runs the above Queries
    cursor1 = cnxn.cursor()
    cursor1.execute(SQLcommand1)

    cursor2 = cnxn.cursor()
    cursor2.execute(SQLcommand2)

    cursor3 = cnxn.cursor()
    cursor3.execute(SQLcommand3)

    cnxn.commit()

#Used to alter tables after data has been entered
def AlterTables(cnxn,employkey,departkeys,addresskeys):
    #Query needed to alter the tables
    SQLcommand4 =f"""ALTER TABLE employees ADD FOREIGN KEY({employkey[4]}) REFERENCES departments({departkeys[0]});
                    ALTER TABLE employees ADD FOREIGN KEY({employkey[6]}) REFERENCES employees({employkey[0]});
                    ALTER TABLE employees ADD FOREIGN KEY({employkey[5]}) REFERENCES addresses({addresskeys[0]});
                    ALTER TABLE departments ADD FOREIGN KEY({departkeys[3]}) REFERENCES addresses({addresskeys[0]});"""

    #Runs the above querys
    cursor4 = cnxn.cursor()
    cursor4.execute(SQLcommand4)

    cnxn.commit()

#Fills the tables with data
def FillTables(cnxn,employees,departments,addresses):
    #Gets lists of column names
    employkeys = list(employees[0].keys())
    departkeys = list(departments[0].keys())
    addresskeys = list(addresses[0].keys())
    #Base string for creating Queries
    RealSQLCommand1 =''
    RealSQLCommand2 =''
    RealSQLCommand3 =''

    #Creates the Query for adding data to employees table
    for row in employees:
        SQLcommand1 = f"""INSERT INTO dbo.employees({employkeys[0]},{employkeys[1]},{employkeys[2]},{employkeys[3]},{employkeys[4]},{employkeys[5]},{employkeys[6]}) 
                            VALUES('{int(row[employkeys[0]])}','{row[employkeys[1]]}','{int(row[employkeys[2]])}','{int(row[employkeys[3]])}','{int(row[employkeys[4]])}','{int(row[employkeys[5]])}','{int(row[employkeys[6]])}');"""
        RealSQLCommand1= RealSQLCommand1+SQLcommand1

    #executes employee Query
    cursor = cnxn.cursor()
    cursor.execute(RealSQLCommand1)

    #Creates the Query for adding data to the department table
    for row in departments:
        SQLcommand2 = f"""INSERT INTO departments({departkeys[0]},{departkeys[1]},{departkeys[2]},{departkeys[3]}) 
                            Values('{int(row[departkeys[0]])}','{row[departkeys[1]]}','{int(row[departkeys[2]])}','{int(row[departkeys[3]])}');"""
        RealSQLCommand2= RealSQLCommand2+SQLcommand2

    #Executes department Query
    cursor = cnxn.cursor()
    cursor.execute(RealSQLCommand2)

    #Creates the query for adding data to the addresses table
    for row in addresses:
        SQLcommand3 = f"""INSERT INTO addresses({addresskeys[0]},{addresskeys[1]},{addresskeys[2]},{addresskeys[3]}) 
                        Values('{int(row[addresskeys[0]])}','{row[addresskeys[1]]}','{row[addresskeys[2]]}','{row[addresskeys[3]]}');"""
        RealSQLCommand3= RealSQLCommand3+SQLcommand3

    #Executes the addresses Query
    cursor = cnxn.cursor()
    cursor.execute(RealSQLCommand3)
    
    cnxn.commit()


#Executes Several SQL Queries
def SQLcommands(cnxn):
    Query1 = []
    Query2 = []
    Query3 = []
    Query4 = []

    #The full data for each Employee with their address as a string, department name, and manager name
    SQLcommand1 = """SELECT 
        e1.employ_id,e1.employ_name,e1.employ_age,e1.employ_salary,
        e2.employ_name 'Manager Name',
        d.depart_name,
        a1.street_name + ', ' + a1.city_name  + ', ' + a1.state_name AS 'Address'

    FROM
        employees e1
    LEFT JOIN
        departments d
    ON 
        e1.depart_id = d.depart_id
    LEFT JOIN
        employees e2
    ON
        e2.employ_id = e1.manager_id
    LEFT JOIN
        addresses a1
    ON 
        e1.address_id = a1.address_id;"""

    ## the 5 highest paid and lowest paid employees
    SQLcommand2 = """SELECT
        *
    FROM
        employees
    WHERE
        employ_salary IN (
        SELECT 
            employ_salary
        FROM
            employees
        ORDER BY
            employ_salary DESC
        OFFSET 0 ROWS
        FETCH NEXT 5 ROWS ONLY
        )
    UNION
    SELECT
        *
    FROM
        employees
    WHERE
        employ_salary IN(
        SELECT
            employ_salary
        FROM
            employees
        ORDER BY
            employ_salary ASC
        OFFSET 0 ROWS
        FETCH NEXT 5 ROWS ONLY
        )
    ORDER BY
        employ_salary DESC;"""

    # The total salary for each department, the manager's name, sorted by highest total
    SQLcommand3 = """SELECT
        d.depart_name,e1.employ_name AS 'Manager', SUM(e2.employ_salary) 'Sum Salary'
    FROM
        departments d
    LEFT JOIN
        employees e1
    ON
        e1.employ_id = d.depart_manage
    LEFT JOIN
        employees e2
    ON 
        d.depart_id = e2.depart_id
    GROUP BY
        d.depart_name, e1.employ_name
    ORDER BY
        'Sum Salary' DESC;"""

    #Each employee that lives in a given state (The state can be hard coded for now)
    SQLcommand4 = """SELECT
        employ_id, employ_name
    FROM
        employees
    WHERE
        address_id IN (
        SELECT DISTINCT
            address_id
        FROM
            addresses
        WHERE 
            state_name = 'Texas'
        );"""

    #Executes Query 1 and saves data in list of lists
    cursor1 = cnxn.cursor()
    result1 = cursor1.execute(SQLcommand1)
    for row in result1:
        Query1.append(row)

    #Executes Query 2 and saves data in list of lists
    cursor2 = cnxn.cursor()
    result2 = cursor2.execute(SQLcommand2)
    for row in result2:
        Query2.append(row)

    #Executes Query 3 and saves data in list of lists
    cursor3 = cnxn.cursor()
    result3 = cursor3.execute(SQLcommand3)
    for row in result3:
        Query3.append(row)

    #Executes Query 4 and saves data in list of lists
    cursor4 = cnxn.cursor()
    result4 = cursor4.execute(SQLcommand4)
    for row in result4:
        Query4.append(row)

    return Query1, Query2, Query3, Query4

if __name__ == "__main__":
    server = 'DESKTOP-7QJS3GV'
    db = 'Assignment'
    cnxn = pyodbc.connect(driver='{ODBC Driver 17 for SQL Server}',host=server,database=db,trusted_connection="yes")

    #SQLcommands(cnxn)
    #FillTables(cnxn,employees,departments,addresses)
    #Createtables(cnxn)
    cnxn.close()