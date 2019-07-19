st = 'Print only the words that start with s in this sentence'
print(st.split())
for x in st.split():
    if x[0] == 's':
        print(x)
for x in range(11):
    if x%2 == 0:
        print(x)

list = [x for x in range(51) if x%3 == 0 ]
print(list)

st = 'Print every word in this sentence that has an even number of letters'

for x in st.split():
    if len(x)%2 == 0:
        print(x +' even')

numlist = [x for x in range(101)]
for x in range(101):
    if x%3 == 0 and x%5 ==0:
        print('FizzBuzz')
    elif x%3 == 0:
        print('Fizz')
    elif x%5 == 0:
        print('Buzz')
    else:
        print(x)

st = 'Create a list of the first letters of every word in this string'
list = [x[0] for x in st.split()]
print(list)
