#Kevin Doyon
#Python/SQL Assignment

import gendata
import exportCSV
import exportYAML
import pyodbc
import PythonSQL




def main():
    #generates all addresses
    address = gendata.gen_address()
    print('#################################################')
    #generates all departments
    departments= gendata.gen_depart()
    print('#################################################')
    # generates all employees
    employees = gendata.gen_employ()
    print('#################################################')
    
    #Stores all data as CSV
    exportCSV.StoreDataCSV(employees,"employ.csv")
    exportCSV.StoreDataCSV(departments,"depart.csv")
    exportCSV.StoreDataCSV(address,"address.csv")

    #Stores departments as YAML
    exportYAML.runyaml(departments,"depart.yaml")

    #Reads CSV files for data
    employees = exportCSV.ImportCSV("employ.csv")
    address = exportCSV.ImportCSV("address.csv")
    departments = exportCSV.ImportCSV("depart.csv")

    #Sets up server
    server = 'DESKTOP-7QJS3GV'
    db = 'Assignment'
    cnxn = pyodbc.connect(driver='{ODBC Driver 17 for SQL Server}',host=server,database=db,trusted_connection="yes")

    #Makes a list of dictionary keys
    employkeys = list(employees[0].keys())
    departkeys = list(departments[0].keys())
    addresskeys = list(address[0].keys())
    
    #Creates, then alters the table keys
    PythonSQL.Createtables(cnxn,employkey=employkeys,departkeys=departkeys,addresskeys=addresskeys)
    #Fills tables with data from CSV
    PythonSQL.FillTables(cnxn,employees=employees,departments=departments,addresses=address)
    #Alters the tables to include foreign keys
    PythonSQL.AlterTables(cnxn,employkey=employkeys,departkeys=departkeys,addresskeys=addresskeys)
    #Runs the 4 SQL Queries
    Q1, Q2, Q3, Q4 = PythonSQL.SQLcommands(cnxn)

    #Closes the server connection
    cnxn.close()

    #Stores the Queries into CSV
    exportCSV.StoreData(Q1,"Query1.csv")
    exportCSV.StoreData(Q2,"Query2.csv")
    exportCSV.StoreData(Q3,"Query3.csv")
    exportCSV.StoreData(Q4,"Query4.csv")

    #Stores the Queries into YAML
    exportYAML.runyaml(Q1,"Query1.yaml")
    exportYAML.runyaml(Q2,"Query2.yaml")
    exportYAML.runyaml(Q3,"Query3.yaml")
    exportYAML.runyaml(Q4,"Query4.yaml")
    



if __name__ == "__main__":
    main()