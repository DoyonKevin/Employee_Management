#Kevin Doyon
#Python/SQL Assignment

import csv

#Stores list of dictionaries into CSV
def StoreDataCSV(data:list,filename):
    try:
        with open(filename,'w',newline='') as file:
            writer = csv.DictWriter(file,data[0].keys())
            writer.writeheader()
            writer.writerows(data)

    except FileNotFoundError:
        print("The file could not be found")

#Stores list of lists into CSV
def StoreData(data:list,filename):
    try:
        with open(filename,'w',newline='') as file:
            write = csv.writer(file)
            write.writerows(data)
            
    except FileNotFoundError:
        print("The file could not be found")

#Reads CSV and turns it into list of dictionaries
def ImportCSV(filename = 'employ.csv'):
    try:
        with open(filename,"rt") as file:
            reader = csv.DictReader(file)
            data = []
            for row in reader:
                data.append(row)
        return data
    except:
        pass


if __name__ == "__main__":
    print("This is exportCSV")