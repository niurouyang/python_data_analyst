l = [
    {
        "name": "photo1.jpg",
        "tags": {'coffee', 'breakfast', 'drink', 'table', 'tableware', 'cup', 'food'}
    },
    {
        "name": "photo2.jpg",
        "tags": {'food', 'dish', 'meat', 'meal', 'tableware', 'dinner', 'vegetable'}
    },
    {
        "name": "photo3.jpg",
        "tags": {'city', 'skyline', 'cityscape', 'skyscraper', 'architecture', 'building', 'travel'}
    },
    {
        "name": "photo4.jpg",
        "tags": {'drink', 'juice', 'glass', 'meal', 'fruit', 'food', 'grapes'}
    }
]

photo_group = {}

for i in range(0, len(l)):
    # for j in range(0, len(l[i]['tags'])):
    # list_1=list(l[i]['tags'])
    for j in range(i + 1, len(l)):
        x = l[i]['tags'].intersection(l[j]['tags'])
        if len(x)>1:

            print(x)
            y = list(x)
            mystring = '_'.join(y)
            photo_group.setdefault(mystring, [l[i]['name'], l[j]['name']])
print(photo_group)
