my_list = []

my_list.append("Ward")
my_list.append("Matthew")
my_list.append("Emily")
my_list.append("Hui")

i = my_list.index("Emily")

print(i)
my_list.insert(i, "Yang")

# insert Y into the list at the position before the index number

print(my_list[:3])
print(my_list[2:])

from collections import deque

queue = deque(my_list)
print(queue)
queue.append("YeYe")
queue.popleft()
print(queue)
my_list = list(queue)

stack = []
for name in my_list:
    stack.append(name)
while stack:
    stack.pop()  # remove last item from the list
    print(stack)

# combine 2 list in to a tuple

age=['5','10','15','20','25']
people_list= [(people_name,people_age) for people_name,people_age in zip(my_list,age)]
print(people_list)

collector_cars= {'Make':'Ford','Model':'Mustang','Year':'1964'}
#setdefault won't change the initial value in the dictionary
collector_cars.setdefault('Make','Toyota')
print(collector_cars)
collector_cars['Make']='Toyota'
print(collector_cars)
# use setdefault to add a value to the dictionary
collector_cars.setdefault('Color','Purple')
print(collector_cars)

txt = 'Python is one of the most promising programming languages today. Due to the simplicity of Python syntax, ' \
      'many researchers and sicentists prefer Python over many other languages.'
txt= txt.replace('.','').replace(',','')
lst=txt.split()
print(lst)
dct={}
for w in lst:
    c = dct.setdefault(w,0)
    dct[w] += 1
print(dct)
# sort dictionary
dct_sort= dict(sorted(dct.items(),key=lambda x:x[1], reverse= True))
print(dct_sort)
