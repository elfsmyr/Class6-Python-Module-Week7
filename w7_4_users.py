import csv
with open('users.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["first name", "last name"])
    writer.writerow(["1", "a"])
    writer.writerow(["2", "b"])
    writer.writerow(["3", "c"])
    writer.writerow(["4", "d"])
    
def print_names():
    with open('users.csv', 'r', encoding='utf-8') as csvf: 
        csvReader = csv.DictReader(csvf) 
        for row in csvReader: 
            print(row["first name"],row["last name"])
def add_name():
    first_name=input("enter name:")
    last_name=input("enter last name:")
    with open('users.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([first_name, last_name])
print_names()
add_name()
print_names()
    