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


