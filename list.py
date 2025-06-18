'''A list is a collection of ordered, mutable and heterogeneous elements. It is one of the most commonly used data types in Python.
Ex:  my_ list = [1, "hello", 3.14, True]'''

#Creating Lists                                                                                                                                
list1 = [1, 2, 3]                    # Integer list
list2 = ["apple", "banana", "mango"] # String list                                            
list3 = [1, "hello", True, 3.14]     # Mixed data types
list4 = list("hello")                # ['h', 'e', 'l', 'l', 'o']
empty = []                           # Empty list

#Accessing Elements
my_list = [10, 20, 30, 40]
print(my_list[0])    # 10
print(my_list[-1])   # 40 (last element)

#Modifying Elements
my_list[1] = 99
print(my_list)  # [10, 99, 30, 40]

#List Operations
a = [1, 2, 3]
b = [4, 5]

#1. Concatenation
print(a + b)      # [1, 2, 3, 4, 5]

#2. Repetition
print(a * 2)      # [1, 2, 3, 1, 2, 3]

#3. Membership
print(2 in a) # True
      
'''append(x) – adds an item to the end of the list
insert (index, item) – inserts an item at a specific index
Extend(list) – adds all elements of another list
Remove(item) – removes the first occurence of the item
Pop(index) – removes and return the item at the given index (default is last)
Clear() – removes all items from the list
Index(item) – returns the index of the first occurence
Count(item)  -- returns the number of times the item appears
Sort () – sorts the list in ascending order
Reverse() – reverses the order of the list
Copy() – returns a copy of the list'''

#Looping through a list
for item in my_list:
    print(item)
# With index
for i in range(len(my_list)):
    print(i, my_list[i])

#List Slicing
nums = [0, 1, 2, 3, 4, 5]
print(nums[1:4])    # [1, 2, 3]
print(nums[:3])     # [0, 1, 2]
print(nums[::2])    # [0, 2, 4]

#Nested Lists
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix[1][2])  # 6

#List Comprehension
squares = [x**2 for x in range(6)]
print(squares)  # [0, 1, 4, 9, 16, 25]
# With condition
even = [x for x in range(10) if x%2 ==0]
print(even)