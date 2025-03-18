#Initializing an empty list
my_list = []
print(my_list)

#Appending elements to the list
my_list.append(10)
print(my_list)
my_list.append(20)
print(my_list)
my_list.append(30)
print(my_list)
my_list.append(40)
print(my_list)

#Inserting elements at a specific index
my_list.insert(1, 15)
print(my_list)

#Extending the list with another list
my_second_list = [50, 60, 70]
my_list.extend(my_second_list)
print(my_list)

#Removing elements from the list
my_list.pop()
print(my_list)

#Sorting the list in ascending order
my_list.sort()
print(my_list)

#Fetching elements from the list using their index
print(my_list[3])
print(my_list)