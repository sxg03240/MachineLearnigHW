# Question 1
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# sorting the list ages
ages.sort()
print(ages)
# To find the minimum age
print(min(ages))
# To find the maximum age
print(max(ages))
# adding min age and Max age to the list
ages.append(min(ages))
ages.append(max(ages))
print(ages)
# find the median
# finding length of the list
L1 = len(ages)
if L1 % 2 == 0:
    median = (ages[L1 // 2] + ages[L1 // 2-1]) / 2
else:
    median = ages[(L1-1)//2]
print(median)
# finding the average age
average = sum(ages)/len(ages)
print(average)
# To find the range of ages
range_ages = (max(ages) - min(ages))
print(range_ages)

# Question 2
# empty dictionary is created
dog = {}
# Add name, color, breed, legs, age to the dog dictionary
dog = {"name": "Teddy", "color": "brown", "breed": "German Shepherd", "legs": 2, "age": 6}

# Create a student dictionary and add first_name, last_name, gender, age, marital status,
# skills, country, city and address as keys for the dictionary
student_dictionary = {"first_name": "Ted", "last_name": "Renu", "gender": "Female", "age": 28, "marital status": "Single", "skills": ["SQL", "MSWord" ,"HTML"] ,"country": "Italy","city":"Milan","address":{
        'street': 'Denicke street',
        'zipcode': '21073'
        }}
# length of the student dictionary
print(len(student_dictionary))
# Get the value of skills and check the data type, it should be a list
print(student_dictionary.get('skills'))
print(type(student_dictionary.get('skills')))
# Modify the skills values by adding one or two skills
student_dictionary['skills'].append('React')
print(student_dictionary)
# Get the dictionary keys as a list
print(student_dictionary.keys())
# Get the dictionary values as a list
print(student_dictionary.values())


# Question 3
# Tuple creation  with names sisters and your brothers
sisters = ('Alex', 'carol', 'Rekha', 'Tara')
Brothers = ('Ted', 'Len', 'Ben')
# To Join brothers and sisters tuples and assigning it to siblings
siblings = sisters + Brothers
print(siblings)
# To calculate number of siblings
print(len(siblings))
# Modify the siblings tuple and add the name of your father and mother and assign it to family members
family_members = siblings + ('Rachel', 'Bing')
print(family_members)

# Question 4
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
#  To Find the length of the set it_companies
print(len(it_companies))
# Adding 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)
# Inserting multiple IT companies at once to the set it_companies
it_companies.update(['Walmart', 'Wipro', 'JC Morgan'])
print(it_companies)
# Remove one of the companies from the set it_companies
it_companies.pop()
print(it_companies)
# Join A and B
print(A.union(B))
# A intersection B
print(A.intersection(B))
# Is A subset of B
print(A.issubset(B))
# Are A and B disjoint sets
print(A.isdisjoint(B))
# Join A with B and B with A
A.update(B)
B.update(A)
print(A)
print(B)
# What is the symmetric difference between A and B
print(A.symmetric_difference(B))
# Delete the sets completely
del it_companies
del A
del B
# Convert the ages to a set and compare the length of the list and the set.
age_st = set(age)
print(age_st)
print(len(age))
print(len(age_st))

# Question 5
radius = 30
from math import pi
# Calculate the area of a circle and assign the value to a variable name of _area_of_circle_
_area_of_circle_ = pi * radius * radius
print(_area_of_circle_)

# Calculate the circumference of a circle and assign the value to a variable name of _circum_of_circle_
_circum_of_circle_ = 2 * pi * radius
print(_circum_of_circle_)

# Take radius as user input and calculate the area
r = float(input('enter the radius of the circle : '))
area = pi * r * r
print("The area of the circle is :" + str(area))

# Question 6
string = "I am a teacher and I love to inspire and teach people"
input_split = string.split()  # returns a list of all the words in a string
print(input_split)
# How many unique words have been used in the sentence? Use the split methods and set
# to get the unique words.
input_set = set(input_split)
print(input_set)
print(len(input_set))

# Question 7
# Use a tab escape sequence to get the following lines.
txt = "Name \t \t Age \t Country \t City \nAsabeneh \t 250 \t Finland \t Helsinki"
print(txt)

# Question 8
# Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
print("The area of the circle with radius {} is {} meters square.".format(radius, area))

# Question 9
# creating an empty list
lst = []
# number of elements as input
n = int(input("Enter number of elements : "))
# iterating till the range
for i in range(0, n):
    element = int(input())
    lst.append(element)  # adding the input element to the list
print('students weights in lbs : ',  lst)
# Converting lbs to kgs into a new list
students_kgs = [float(x) * 2.2 for x in lst]
print('students weights in kgs : ',  students_kgs)
