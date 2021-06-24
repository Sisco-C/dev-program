import csv
#open the file, while r reads it
with open("sample.csv", 'r') as file:
    #creating an object
    csv_file = csv.DictReader(file)
    #iterating over the file
    for row in csv_file:
        #to create dictionaries
        print(dict(row))