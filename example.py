# comment

"""Welcome to Python"""

""" Data Types """
name = 'Felix'
age = 5
is_old = False
sei_1019 = True

print(name)

""" Methods for a string """
sentence = 'Today is Nicole birthday'

# splits into an array
nicole_birthday = sentence.split(' ')
print(nicole_birthday)

#joing the array
new_sentence = " ".join(nicole_birthday)
print(new_sentence)

# find index
print(new_sentence.index('N'))

#Upper and lower case
name.upper()
name.lower()

# replace
day_sentence = sentence.replace('birthday', 'Day')
print(day_sentence)

# in keyword returns a boolean of true or false is the keyword is in
is_day = 'Day' in day_sentence
print(is_day)

day_sentence

#ranges
last_letter = day_sentence[-1]

nicole_range = day_sentence[9:15]
print(nicole_range)

# length
print(len(nicole_range))

# logical operator
equal_to = 5 == 5
not_equal = 5 != 5
true_story = 5 <= 5
this_should_be_true = 6 >= 5

print(9 < 38 )

print(5 and 1)
print(5 or 1)

print(5 < age < 6)


# python dont say arrays we call them lists.
#lists
numbers = [3,4,5,6]
print(len(numbers))

print(numbers[1])
print(numbers[-1])

print(numbers[len(numbers) - 1 * 2])

five_felix = ['felix'] * 5
print((five_felix))

one_through_five = list(range(5))
print(one_through_five)

for i in range(len(one_through_five)):
    num = one_through_five[i]
    print(num)

# create a list and iterate through the list and print value

my_list = ['one', 'two', 'three']
for i in range(len(my_list)):
    haha = my_list[i]
    print(haha)

random_numbers = [45, 88, 4, 17]
random_numbers.sort()
sorted_numbers = random_numbers
print(sorted_numbers)

random_numbers.append(33)
print(random_numbers)

reverse_random_numbers = random_numbers[::-1]
print(reverse_random_numbers)

thirty_three = random_numbers.pop()
print(thirty_three)

random_numbers.insert(0, 99)
print(random_numbers)

random_numbers.insert(1, 77)
print(random_numbers)

# help
#print(help(random_numbers))

#dictionary are what they call objects in javascript

car = {
    "color": "Red",
    "make": "Tesla",
    "model": "S",
    "all_colors": ['Red', 'white', 'black'],
    "cool_car" : True,
    "other_tesla_products":{
        "product": "Model 3",
        "product2" : "Model X",
        "product3" : "Cybertruck"
    }
}

print(car["make"])

# add a key value
car["speed"] = 200

print(car)

#print(help(car))


print(car.get("color"))
print(car.items())
print(car.keys())

#type conversion
int('33')
str(33)
float(33)
bool(0) #false
bool(3) #true

#string interpolation
print('hello my name is ' + name)
print(f"Hello my name is {name}")

phrase = 'This {} is a phrase {}'
print(phrase.format('sentace' ,name))




#functions using def

def list_name(someone):
    return someone

print(list_name("Will"))

def old_enough(age):
    if age < 21:
        return 'Not old enough'
    elif age == 21:
        return 'You made it to adulthood'
    else:
        return 'Your older, nice'

print(old_enough(21))

def add(num1, num2):
    print('inside add function')
    return num1 + num2

def subtract(num1, num2):
    print('inside subtract function')
    return num1 - num2

def random_function(weather):
    if weather < 60:
        return 'freezing'
    elif weather ==  60:
        return 'ok'
    else:
        return 'great weather'

print(subtract(3 ,6))
