import json
path="cars.json"
with open(path,'r') as json_file:
    json_cars= json.load(json_file)
    for car in json_cars['cars']:
        print('Year: ' + car['Year'])
        print('Make: ' + car['Make'])
        print('Model: '+ car['Model'])
        print('Price: '+ car['Price'])
        print('\n')