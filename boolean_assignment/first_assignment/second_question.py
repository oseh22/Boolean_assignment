# List of numbers
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
list3 = [4, 5, 6, 7]

# getting the common elements by using set intersection 
common = set(list1) & set(list2) & set(list3)  

if common:
    print(bool(common))
else:
    print(bool())
