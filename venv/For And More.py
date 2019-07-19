list1 = [1,2,3,4,5,6,7,8,9,10]
list_sum = 0

for num in list1:
    list_sum = list_sum + num

print(list_sum)

for num in list1:
    list_sum += num

print(list_sum)

for letter in 'This is a string.':
    print(letter)

tup = (1,2,3,4,5)

for t in tup:
    print(t)

list2 = [(2,4),(6,8),(10,12)]
for tup in list2:
    print(tup)
for (t1, t2) in list2:
    print(t1)

d = {'k1':1,'k2':2,'k3':3}
for item in d:
    print(item)
for item in d.values():
    print(item)
# Since the .items() method supports iteration, we can perform dictionary unpacking to separate keys and values just as we did in the previous examples
d.items()

for k,v in d.items():
    print(k)
    print(v)
