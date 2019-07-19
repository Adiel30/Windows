# Enumerate = .format
index_count = 0
# its over all the STRING 'abcde'
for letter in 'abcde':
                                       #A put the value of the Varlible      #B Put the Value Of 'abcde'
    print("At index {} the letter is {}".format(index_count,letter))
    index_count += 1
# Makes Unpacking to the tuple and put number for evrey values in this case 0-4
# [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd'), (4, 'e')]
for i,letter in enumerate('abcde'):
    print("At index {} the letter is {}".format(i,letter))

# Zipping Can Use for Make a List Of Tupple
mylist1 = [1,2,3,4,5]
mylist2 = ['a','b','c','d','e']
list(zip(mylist1,mylist2))
#[(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]

# Zip As Generator =
for item1, item2 in zip(mylist1,mylist2):
    print('For this tuple, first item was {} and second item was {}'.format(item1,item2))

# min and max , random
print(min(mylist1))
print(max(mylist1))
from random import shuffle
shuffle(mylist1)
print(mylist1)
# randint brings a random integer from range
from random import randint
mylist = randint(0,100)
print(mylist)

