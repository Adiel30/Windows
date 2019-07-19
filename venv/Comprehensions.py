# Will put a list on evrey letter in th word
lst = [x for x in 'word'] # x in 'word' PRINT W O R D # x for x  Crete the , fo the list
print(lst)
# Example 2
lst = [x**2 for x in range(0,11)] # # in Range of 0-10 Make A list of evrey number in power of 2
print(lst)
#Example 3
lst = [x for x in range(11) if x % 2 == 0] # In range of 0-10 make a list just for modlue = 0 # כלומר תעשה את הפעולה רק כאשר המשתנה יהיה שווה ל...
print(lst)

# Example 4
lst = [x for x in range(11) if x % 2 != 0]
print(lst)

#Example 5
# Convert Celsius to Fahrenheit
celsius = [0,10,20.1,34.5]

fahrenheit = [((9/5)*temp + 32) for temp in celsius ] # Divid 9/5*temp(varlible) + 32 FOR EACH value in Celsius List

print(fahrenheit)
#Example 6
# Nasted FOR INSIDE FOR
lst = [ x**2 for x in [x**2 for x in range(11)]] #Start For Inside # X in power of 2 in range 0-10 List # once Again X power of 2 for evrey number in the first list
print(lst)