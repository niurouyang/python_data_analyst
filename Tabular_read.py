#.tsv file seperate by tab
#.csv file separate by comma
import csv
path='cars.csv'
with open(path,'r') as csv_file:
    
    csv_reader=csv.DictReader(csv_file)
        #cars.append(dict(row))
        #[{'Year': '1997', 'Make': 'Ford', 'Model': 'E350', 'Price': '3200.00'}, {'Year': '1999', 'Make': 'Chevy', 'Model': 'Venture', 'Price': '4800.00'}, {'Year': '1996', 'Make': 'Jeep', 'Model': 'Grand Cherokee', 'Price': '4900.00'}]
    #csv_reader=csv.reader(csv_file)
        #cars.append(row)
        #[['Year', 'Make', 'Model', 'Price'], ['1997', 'Ford', 'E350', '3200.00'], ['1999', 'Chevy', 'Venture', '4800.00'], ['1996', 'Jeep', 'Grand Cherokee', '4900.00']]
    cars=[]
    for row in csv_reader:
        cars.append(dict(row))

for row in cars:
    print(list(row.values()))

to_update= ['1999', 'Chevy', 'Venture']
new_price='4500.00'
with open('path','w') as csv_file:

    fieldnames=cars[0].keys()
    # get the first dictionary's keys
    writer=csv.DictWriter(csv_file, fieldnames=fieldnames)
    # writer.writeheader()
    # write the header/1st row to the csv file
    for row in cars:
        #print(row.values())
        #print(row.keys())
        #dict_values(['1997', 'Ford', 'E350', '3200.00'])
        #dict_keys(['Year', 'Make', 'Model', 'Price'])
        if set(to_update).issubset(set(row.values())):
            #compaire to see if to_update is inside row.values
            row['Price']= new_price
            #change the price of that column
            print(row)
            writer.writerow(row)

