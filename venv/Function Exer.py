def lesser_of_two_evens(a,b):
    if a%2 == 0 and b%2 == 0:
        return min(a,b)
    else:
        return max(a,b)
    pass

print(lesser_of_two_evens(2,4))
print(lesser_of_two_evens(4,5))

#Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
#makes_twenty(20,10) --> True
#makes_twenty(12,8) --> True
#makes_twenty(2,3) --> False
def makes_twenty(n1,n2):
    if n1 == 20 or n2 == 20 or n1+n2 == 20:
        return True
    else:
        return False

print(makes_twenty(20,10))
print(makes_twenty(12,8))
print(makes_twenty(2,3))

#  Write a function that capitalizes the first and fourth letters of a name
def old_macdonald(name):
    if len(name) > 3:
        return name[:3].capitalize() + name [3:].capitalize()
    else:
        print("name is too short")
print(old_macdonald('macdonald'))


#Given a sentence, return a sentence with the words reversed¶
#master_yoda('I am home') --> 'home am I'
#master_yoda('We are ready') --> 'ready are We
def master_yoda(text):
    return ' '.join(text.split()[::-1]) #::-1 revers the sentence
print(master_yoda('I am home'))