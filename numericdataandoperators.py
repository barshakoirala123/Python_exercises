#Exercise 1: Numeric Data
#Create two variables num_1 as 7, num_2 as 3.5 and:
#Display their data types
#Display their sum
#Display their difference
#Display their product
#Display their division
#Convert both num_1 and num_2 into string and display sum again
#Repeat above exercise but with storing both variables with a complex number
#Create variable num_3 as 15 and num_4 as 4. Swap their values and display the result

num_1= 7
num_2 = 3.5
print(type(num_1))
print(type(num_2))
print(num_1 + num_2)
print(num_1 - num_2)
print(num_1*num_2)
print(num_1/num_2)
print(str(num_1)+str(num_2))

num_3 = 15
num_4 = 4
print(type(num_3))
print(type(num_4))
print(num_3 + num_4)
print(num_3 - num_4)
print(num_3*num_4)
print(num_3/num_4)
print(str(num_3)+str(num_4))

num_3 = 4
num_4 = 15
print(type(num_3))
print(type(num_4))
print(num_3 + num_4)
print(num_3 - num_4)
print(num_3*num_4)
print(num_3/num_4)
print(str(num_3)+str(num_4))


#Create two variables num_1 as 7, num_2 as 3.5 and:
#Display their data types
#Display their sum
#Display their difference
#Display their product
#Display their division
#Convert both num_1 and num_2 into string and display sum again
#Repeat above exercise but with storing both variables with a complex number
#Create variable num_3 as 15 and num_4 as 4. Swap their values and display the result

num_z1 = 2+ 3j
num_z2 = 4+ 5j
print(f"sum is {num_z1+num_z2}")
print(f"difference is {num_z1-num_z2}")
print(f"product is {num_z1*num_z2}")
print(f"division is {num_z1/num_z2}")

# Exercise 2: Assignment Operators
# Assign mark_1, mark_2, mark_3 with value 78, 85, 92. Calculate total and average mark
mark_1=78
mark_2=85
mark_3=92
total = mark_1+ mark_2+ mark_3
print(total)
# Assign weight_1, weight_2, weight_3, weight_4 all having value as 70


# Add 5 to weight_1 and reassign to weight_1
# Subtract 10 from weight_2 and reassign to weight_2
# Multiply weight_3 by 1.1 and reassign to weight_3
# Divide weight_4 by 2 and reassign to weight_4
weight_1=weight_2=weight_3=weight_4= 70
weight_1=weight_1+5
weight_2=weight_2-10
weight_3= weight_3*1.1
weight_4=weight_4/2
print(weight_1)
print(weight_2)
print(weight_3)
print(weight_4)
# Assign variable my_num as 15. Find remainder when divided by 2 as reassign to itself

my_num=15%2
print(my_num)

# Find the value when 1.1 is raised to the power of 3 i.e. 1.1 ^ 3. Assign is to result
num=1.1**3

# Exercise 3: Comparison & Logical Operators
# Assign your age to variable my_age and:
my_age = 30
# Check if your age 16
print(my_age == 16)
# Check if your age is not 70
print(my_age != 70)
# Check if you are a child (age less than 13)
print(my_age<13)
# Check if you are an adult (age 20 or above)
print(my_age>=20)
# Check if you are eligible to vote (18+ can vote)
print(my_age>=18)
# Check if you are a teenager (age between 13 and 19)
print(my_age>=13 and my_age<=19)
# Check if you lie on passive population (below 5 and over 65 considered passive)
print(my_age<5 and my_age>65)
# Check if you are eligible for driving license (age between 18 and 65)
print(my_age>=18 and my_age<=65 )

# Exercise 4: Membership Operators
# Assign variable my_name as your name and check if:
# Letter a is in your name
# Letter a is not in your name


my_name = "Barsha"
print("a" in my_name)
print("a" not in my_name)

# Assign variable movie_collection as a list of your favorite movies and check if:
# Movie Avatar is in your collection
# Movie Avatar is not in your collection

movie_collection = ['Avatar', 'kri', 'Ramayan']
print('Avatar' in movie_collection)
print('Avatar' not in movie_collection)

# Repeat exercise 2 but creating movie_collection as a tuple
movie_collection1 = ('Avatar', 'kri', 'Ramayan')
print('Avatar' in movie_collection1)
print('Avatar' not in movie_collection1)

# Repeat exercise 2 but creating movie_collection as a set
movie_collection2 = {'Avatar', 'kri', 'Ramayan'}
print('Avatar' in movie_collection2)
print('Avatar' not in movie_collection2)

