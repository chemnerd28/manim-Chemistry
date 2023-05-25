import csv

ElementDict = {}
File = input("Enter CSV with .csv: ")
with open (File) as csvfile:
    reader = csv.DictReader(csvfile)# fieldnames=('AtomicNumber', 'Name', 'Symbol', 'AtomicMass', 'Color'))

    for row in reader:
        ElementDict[int(row['AtomicNumber'])] = {'Element': (row['Name']), 'Symbol': row['Symbol'], 'AtomicMass': float(row['AtomicMass']), 'Color': row['Color']}
        with open("Elements_FR.txt", 'a') as f:
            print(ElementDict, file = f)
