# Create a list by picking an odd-index items from the first list and even index items from the second

list1 = [1,2,3,4,5,6,7]
list2 = [ 'a','b','c','d','e']
list3 = []

print('Element at odd-index positions from list one -')
odd_index = list1[0:len(list1):2]
print(odd_index)
print('Element at even-index positions from list two -')
even_index = list2[1:len(list2):2]
print(even_index)

list3.extend(odd_index)
list3.extend(even_index)
print('Printing final third list -')
print(list3)