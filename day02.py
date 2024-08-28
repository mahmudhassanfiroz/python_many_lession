"""Authore:
Mahmud Hassan Firoz
"""
print('\n')
""" # Sum 
sum_number1 = input('Enter Your First Number ')
sum_number2 = input('Enter Your Second Number ')
sum = int(sum_number1) + int(sum_number2)
print('Sum : ' , sum)
print('\n')
# Subtraction
subtraction_number1 = input('Enter Your First Number ')
subtraction_number2 = input('Enter Your Second Number ')
subtraction = int(subtraction_number1) - int(subtraction_number2)
print('Subtraction: ' , subtraction)
print('\n')
# Multiplication
multiplication_number1 = input('Enter Your First Number ')
multiplication_number2 = input('Enter Your Second Number ')
multiplication = int(multiplication_number1) * int(multiplication_number2)
print('Multiplication: ' , multiplication)
print('\n')
# Division
division_number1 = input('Enter Your First Number ')
division_number2 = input('Enter Your Second Number ')
division = int(division_number1) / int(division_number2)
print('Division: ' , division)
print('\n')
# Sum of Three Number
sum_number1 = input('Enter Your First Number ')
sum_number2 = input('Enter Your Second Number ')
sum_number3 = input('Enter Your 3rd Number ')
sum = int(sum_number1) + int(sum_number2) + int(sum_number3)
print('Sum: ' ,sum)
print('\n')
# Area of Triangle
base = input('Enter Your Base ')
height = input('Enter Your Height ')
area = 0.5 * int(base) * int(height) 
print('Area Of Triangle: ' , area)
print('\n')
# Find the area of ​​the quadrilateral
side1 = input('Enter Your First Side ')
side2 = input('Enter Your Second Side ')
area_of_quadrilateral = int(side1) * int(side2)
print('Area Of Quadrilateral: ' , area_of_quadrilateral )
print('\n')
# Find the area of ​​a circle
radius = input('Enter Your Radius ')
area_or_circle = 3.14 * int(radius) * int(radius)
print('Area Of Circle: ' , area_or_circle)
print('\n')
 """
price = 45
age = 24
# print(price)
# print(age)
price = 50
# print(price)
another_price = price = 60
# print(price)
# print(another_price)

# number1 = input(' Enter First Number: ')
# number2 = input('Enter Second Number: ')
# sum = number1 + number2
# print(sum)
# number1 = int(input(' Enter First Number: '))
# number2 = int(input('Enter Second Number: '))
# sum = number1 + number2
# print(sum)
# course = 'Python for beginners'
# print(course[0])
# print(course[-1])
# print(course[0:3])
# course[0]='F'
# print(course)
# print(len(course))
# print(course.find('p'))
# print(course.find('P'))
# print(course.replace)
# text = 'Hello , world!' 
# words = text.split(" , ")
# print(words)
# List 
numbers = [1, 2, 3, 4, 5]
fruits = ['apple', 'banana', 'cherry']
mixed_list = [10, 'hello', 3.14, True]
empty_list = []
lists = [1,2,3,[4,5]]
# print(numbers)
# print(numbers[0])
# print(lists[3])
# print(lists[3][1])
# print(lists[4])
sliced_list = numbers[1:4]
# print(sliced_list)
empty_list.append('Firoz')
# print(empty_list)
# print(mixed_list)
# print(lists.remove[3][1])
# print(lists.remove([3][1]))
# print(lists.remove(3))
# print(lists)
# print(lists[2].remove(4))
# print(lists)\
# last_fruit = fruits.pop()
# print(last_fruit)
# print(fruits)
numbers = [1,2,3,4,5,6]
cubes = [x**3 for x in numbers]
# print(cubes)
# even_numbers = [x%2==0 for x in numbers]
even_numbers = [x for x in numbers if x%2==0]
# print(even_numbers)
# Tuple 
numbers_tuple = (1,2,3,4,5)
fruits_tuple = ("apple", "banana", "cherry")
mixed_tuple = (10, "hello", 3.14, True)
single_element_tuple = (42)
empty_tuple = ()
# print(numbers_tuple[0])
# print(numbers_tuple[0:3])
# Dictionary
person = {"name" : "Firoz", "age" : 25, "city" : "New York"}
# Dictionary Method 
# print(person.keys())
# print(person.values())
# print(person.items())
person.update({"emal": "firoz90@gmail.com"})
# print(person)
squar_dict = {num: num**2 for num in numbers}
# print(squar_dict)
# Set 
numbers_set = {1, 2, 3, 4, 5}
fruits_set = {'apple', 'banana', 'cherry'}
mixed_set = {10, 'hello', 3.14, True}
empty_set ={}
# print(numbers_set)
# print(numbers_set.add(6))
# print(numbers_set)
# print(numbers_set.remove(6))
# print(numbers_set)
# print(numbers_set.pop())
# print(numbers_set)
# print(numbers_set.discard(6))
# print(numbers_set)
# print(numbers_set.intersection(numbers_set))
# print(numbers_set.union(numbers_set))
# print(numbers_set.difference(numbers_set))
# print(numbers_set.symmetric_difference(numbers_set))
# print(numbers_set.issubset(numbers_set))
# print(numbers_set.issuperset(numbers_set))
# print(numbers_set.isdisjoint(numbers_set))
# print(numbers_set.copy())
# print(numbers_set.clear())
# https://github.com/mAhmedSiddiki/Python_Full_Course
# https://www.slideshare.net/slideshow/python-programming-full-course-beginner-to-intermediate-bangla-codinglaugh/258882557

# Ternari Operator (condition ? value_if_true: value_if_false)
# result = value_if_true if condition else value_if_false 
x = 5 
y = 10
max_value = x if x>y else y 
# print('Maximum value between x and y is: ', max_value)
numbers = [1, 2, 3, -3, 4, -5, 0]
positive_numbers = [num for num in numbers if num > 0]
# print('positive numbers in the list are: ', positive_numbers if positive_numbers else 'No positive numbers found')
numbers = [5, -3, 0, 10, -8, 2]
positive_count = 0 
negative_count = 0
zero_count = 0
for num in numbers:
    if num > 0:
        positive_count += 1
    elif num < 0:
        negative_count += 1
    else:
        zero_count += 1
# print(f'Positive numbers: {positive_count}')
# print(f'Negative numbers: {negative_count}')
# print(f'Zeroes: {zero_count}')
# Lambda functions
add = lambda a, b : a+b 
# print(add(5,3))
numbers = [1, 2, 3, 4, 5]
doubled = map(lambda x : x*2, numbers)
# print(list(doubled))
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(lambda x : x%2 == 0, numbers)
# print(list(even_numbers))
points = [(1,2), (3,1), (5,4), (2,3)]
sorted_points = sorted(points, key=lambda point:point[1])
# print(sorted_points)
# If statment 
a = 'Chocolate'
b = 'Canday'
c = 'Shinchan'
if a == 'Chocolate':
    # print('Home work done')
    if c == 'Doreaemon':
        # print('Eat food')
        pass
    else:
        # print('Not eating')
        pass
elif b == 'Cake':
    # print('Home work done')
    pass
else:
    # print('Home work not finished')
    pass
# print('Codinglaugh')
# While loop 
# while True:
    # print('OKKey')

# While nested loop
# i = 1
# j = 1
# while i <= 5:
    # while j <= 5:
        # print('i=', i, ' j=', j, sep='')
        # j += 1
    # else:
        # print('j is end')
    # i += 1
    # j = 1
# for loop 
a = 'codinglaugh'
# tuple, list, set, dictionary, string
for i in a:
    # print(i)
    pass
# range for loop
for i in range(1,11,3): # start, end, step
    # print(i)
    pass
# nested loop
for i in range(1,6):
    for j in range(1,6):
        # print('i=', i, ' j=', j, sep='')
        # dictionary for loop
        # dict = {'a': 1, 'b': 2, 'c': 3}
        # enumerate for loop
        # dict = {'a': 1, 'b': 2, 'c': 3}
        # break and continue
        # for i in range(1,11):
        # if i == 5:
        # break
        # print(i)
        pass
    else:
        # print('j is end')
        pass
# break 
for i in range(1,6):
    pass
i = 1
while i <= 5:
    if i == 3:
        pass
    # print(i)
    i += 1

a = 5
a= None
# print(type(20>2))
# None Boolean Number
# none
a = 10
a = None
a = 5 
if a ==None:
    # print('a is None')
    pass
else:
    # print('Not None')
    pass
# print(type(a))
# Boolean
# print(type(10<20))
a = 10>20
if a == True:
    # print('10 is small')
    pass
else:
    # print('20 is big')
    pass
# int float complex
a = 3
# print(a,type(a))
b=3.14
# print(b,type(b))
# print("{:.3f}".format(b))
# real and imaginary
c = 10+12j
# print(c, type(c))
# print(20.354j+c)
# String
a = 'Mahmudhassanfiroz'
b = 'Nusratjahanliza'
# print(a,type(a))
# print(b,type(b))
c = 'youtube channel name is "Mahmudhassanfiroz"'
# print(c)
d = """ Mahmud Hassan Firoz has learn something everyday """
# print(d,type(d))
e = 'Mahmudhassanfiroz'
f = 'Hassan'
g = 'Firoz'
h = 'Liza'
# print(e+f+g+h)
# print(e*5)
# print('c' not in e)
# print(len(e))
length = 0
for i in e:
    # print(i, end="")
    length += 1
# print()
# print(length)
i = 'Mahmudhassanfiroz'
if 'Nusratjahanfiroz' != i:
    # print('matched')
    pass
else:
    # print('Something wrong')
    pass
i='abc'
j='ABC'
# print(i>j)
# print(e[-12])
# String Method 
a = "      mhf   "
# print(a.isspace)
# print(a.isdigit())
# print(a.isnumeric())
# print(a.istitle)
# print(a.islower)
# print(a.replace("Liza", "Nusrat"))
# print(a.zfill(20))
# print(a.swapcase())
# List 
a = ["Doreamon", "Shinchan", "Tom and Jerry", 1,3,4,'Shinchan',1.4]
b,c = ["Doreamon", "dorejsdhfamon", "Shinchan", "shhdsvssinchan"],[1,5,3,8,2,4]
# print(sum(c))
# print(min(b))
# def length(i):
    # return len(i)
# c.sort(reversed(c,reverse=True))
# print(sorted(c,reverse=True))
# a.reverse()
# print(a)
# print(a.count(1.4))
# print(a.index("Doreamon"))
b = ["jdhbf",2,3,4,"jdshbf"]
# print(b+a)
# b = a.copy()
if "Shinsjdbhfchan" in a:
    # print("paichi")
    pass
else:
    # print("pai nai")
    pass
# print(len(a))
for i in a:
    print(i)
    pass
# del a[1:4]
# a.remove('Shinchan')
# a.pop(2)
# a.clear()
# print(a)
# a[2] = "Meena"
# print(a)
a[2:5] = ["Meena",2,"Hello"]
# print(a)
a.append("Hey")
a.extend(["Hello","I","Am"])
a.insert(1,4)
# print(a)
c = []
for i in b:
    if type(i) is list:
        c = i.copy()
        # for j in i:
            # print(j)
    else:
        # print(i)
        pass
# print(c)
# tupple
a = ("Doreamon","sdjfhan","Tom and Jerry")
b = (1,2,34,5,3,3)
# print(b.count(3))
# print(sorted(a,reverse=True))
# print(a.index("Tom and Jerry"))
# print(sum(b))
# print(min(b))
# print(len(a))
# print(b+a)
# print(a*2)





print(" ")