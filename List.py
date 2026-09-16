'''List in Python
List is a collection of items which are ordered and changeable. It allows duplicate members.
List is defined by enclosing the items in square brackets [] and separated by commas.
List can contain items of different data types like integers, floats, strings, booleans,
and even other lists.

#list
f=[]
fruits = [10, 20, 30, 40, 5.4, True]
print(f)
print(fruits)
print(fruits[0]) #10
print(fruits[1]) #20
print(fruits[-1]) #True
print(fruits[-4]) #40
print(fruits[-3]) #5.4
print(fruits[-5]) #20

#List slicing
print(fruits[1:4]) #[20, 30, 40]
print(fruits[:3]) #[10, 20, 30]
print(fruits[3:]) #[40, 5.4, True]
print(fruits[::2]) #[10, 30, 5.4]
print(fruits[::-1]) #[True, 5.4, 40, 30, 20, 10]


#operations on list
a=[1,2,3]
b=[3,4,5]
c = a+b
print(c) #[1, 2, 3, 3, 4, 5]
d=a*3
print(d) #[1, 2, 3, 1, 2, 3]

#repeat list
e=[0]*5
print(e) #[0, 0, 0, 0, 0]
print('-'*20) #--------------------
f=a[1:3]
print(f) #[2, 3]

#update list
a[1] = 20
print(a) #[1, 20, 3]

#delete list
del a[1]
print(a) #[1, 3]
del b[2]
print(b) #[3, 4]

#delete with slice
list =[10,20,30,40,50]
del list[1:2]
print(list) #[10, 30, 40, 50]
del list[::2]
print(list) #[30, 50]

del list[:]
print(list) #[]
del list
#print list  #NameError: name 'list' is not defined


#Nested list
nested_list = [
                [1, 2, 3],
                [3, 4, 5],
                5,
                1000
            ]
print(nested_list) #[[1, 2, 3], [3, 4, 5], 5, 1000]
print(nested_list[2]) #[1, 2, 3]
print(nested_list[0][1]) #2
print('length of nested list: ', len(nested_list)) #4
print('length of nested list[0]: ', len(nested_list[0])) #3
print('length of nested list[1]: ', len(nested_list[1])) #3
#print('length of nested list[2]: ', len(nested_list[2])) #TypeError: object of type 'int' has no len()

#append list
list = [1, 2, 3]
list.append(4)
print(list) #[1, 2, 3, 4]

#insert list
list.insert(1, 20)
print(list) #[1, 20, 2, 3, 4]

#extend list
list2 = [5, 6, 7]
list.extend(list2)
print(list) #[1, 20, 2, 3, 4, 5, 6, 7]

#append list with another list
list.append(list2)
print(list) #[1, 20, 2, 3, 4, 5, 6, 7, [5, 6, 7]]


list = [1,2,3,33,4, 5, 6, 7, 55, 5, 6, 8, 9, 10]
#index of list
print(list.index(2)) #1
print(list.index(5)) #4

#count of list
print(list.count(6)) #1
print(list.count(5)) #2

#sort list
list.sort()
print(list) #[1, 2, 3, 4, 5, 5, 6, 6, 7, 8, 9, 10, 33, 55]
list.sort(reverse=True)
print(list) #[55, 33, 10, 9, 8, 7, 6, 6, 5, 5, 4, 3, 2, 1]


list = [1,2,3,33,4, 15, 6, 7, 55, 5, 46, 8]
#sorted list
sorted_list = sorted(list)
print(sorted_list) #[1, 2, 3, 4, 5, 5, 6, 6, 7, 8, 9, 10, 33, 55]
sorted_list_desc = sorted(list, reverse=True)
print(sorted_list_desc) #[55, 33, 10, 9, 8, 7, 6, 6, 5, 5, 4, 3, 2, 1]

#reserve list
list.reverse()
print(list) #[55, 33, 10, 9, 8, 7, 6, 6, 5, 5, 4, 3, 2, 1]

set1={10,34,2,67,23}
result=sorted(set1)
print(result) #[2, 10, 23, 34, 67]
print(set1) #{10, 34, 2, 67, 23}


list = [1,2,3,33,4, 15, 11]
#remove list
val = list.remove(4)
print(val) #[1, 2, 3, 33, 4]
val = list.pop(1)
print(val) #2
print(list) #[1, 3, 33, 4]

#implementation of stack using list
stack = []
stack.append(1)
stack.append(2)
stack.append(3)
print(stack) #[1, 2, 3]
v=stack.pop()
print(v) #3
print(stack) #[1, 2]

list.clear()
print(list) #[]


list1=['John', 'Alice', 'Bob']
r = sorted(list1, key=len)
r1 = sorted(list1, key=max)
print(r) #[Bob, John, Alice]
print(r1) #[Alice, Bob, John]

r2-= sorted(list1, key=lambda name: len(name))
print(r2) #[Bob, John, Alice]
'''

#array
import array
arr = array.array('i', [1, 2, 3, 4, 5])
print(arr) #array('i', [1, 2, 3, 4, 5])

arr = array.array('i')
arr.append(1)
arr.append(2)
print(arr) #array('i', [1, 2])

print(type(arr)) #<class 'array.array'>
