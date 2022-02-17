# Activities & Practices
# --------- [String] ---------
print("--------- [Strings] ---------")
print("----------------------------------")
# Practise 01
print("Practise #01")
favorite_fruit = "blueberry"
print(len(favorite_fruit)) # 9
print(favorite_fruit[0]) # b
print(favorite_fruit[0]) # b
print(favorite_fruit[4:6]) # be
print(favorite_fruit[4:7]) # ber
print(favorite_fruit[3:8]) # eberr
print(favorite_fruit[2:9]) # ueberry
print(favorite_fruit[:4]) # blue
print(favorite_fruit[4:]) # berry
print("----------------------------------")
# Practise 02
print("Practise #02")
fruit_prefix = "blue"
fruit_suffix = "berries"
favorite_fruit = fruit_prefix + fruit_suffix
print(favorite_fruit) # blueberries
fruit_sentence = "My favorite fruit is " + favorite_fruit
print(fruit_sentence) # My favorite fruit is blueberries
print("----------------------------------")
# Practise 03
print("Practise #03")
first_name = "Julie"
last_name = "Blevins"
def account_generator(fName, lName):
    account_name = fName[:3] + lName[:3]
    return account_name

new_account = account_generator(first_name, last_name)
print(new_account) # JulBle
print("----------------------------------")
# Practise 04
print("Practise #04")
favorite_fruit = "blueberry"
# last_char = favorite_fruit[len(favorite_fruit)]
# print(last_char) # IndexError: string index out of range
last_char = favorite_fruit[len(favorite_fruit)-1]
print(last_char) # Output: y
length = len(favorite_fruit)
last_char = favorite_fruit[length-4:]
print(last_char) # Output: erry
print("----------------------------------")
# Practise 05
print("Practise #05")
first_name = "Reiko"
last_name = "Matsuki"

def password_generator(fName, lName):
    account_name = fName[-3:] + lName[-3:]
    return account_name

temp_password = password_generator(first_name, last_name)
print(temp_password) # ikouki
print("----------------------------------")
# Practise 06
print("Practise #06")
# favorite_fruit = "blueberry"
print(favorite_fruit[-1]) # y
print(favorite_fruit[-2]) # r
print(favorite_fruit[-3:]) # rry
sentence0 = "daily life"
second_to_last = sentence0[-2]
print(second_to_last) # f
final_word = sentence0[-4:]
print(final_word) # life
print("----------------------------------")
# Practise 07
print("Practise #07")
first_name = "Bob"
last_name = "Daily"

#first_name[0] = "R"
#print(first_name) # TypeError: 'str' object does not support item assignment
# Strings are Immutable
# We can use it to create other strings, but we cannot change the string itself.

fixed_first_name = "R" + first_name[1:]
print(fixed_first_name) # Rob
print("----------------------------------")
# Practise 08
print("Practise #08")
favorite_fruit_conversation = "He said, \"blueberries are my favorite!\""
print(favorite_fruit_conversation) # He said, "blueberries are my favorite!"
password = "theycallme\"crazy\"91"
print(password) # theycallme"crazy"91
print("----------------------------------")
# Practise 09
print("Practise #09")
def print_each_letter(word):
    for letter in word:
        print(letter)

favorite_color = "blue"
print_each_letter(favorite_color) # b l u e    
#print_each_letter("blue") # b l u e    
print("----------------------------------")
# Practise 10
print("Practise #10")
def get_length(word):
    counter = 0
    for letter in word:
        counter += 1
    return counter

function_test = get_length("HombaGomba")
print(function_test) # 10
print("----------------------------------")
# Practise 11
print("Practise #11")
favorite_fruit = "blueberry"
counter = 0
for character in favorite_fruit:
    if character == "b":
        counter = counter + 1

print(counter) # 2
print("----------------------------------")
# Practise 12
print("Practise #12")
def letter_check(word, letter):
    for character in word:
        if letter == character:
            return True
    return False

test_function = letter_check("Listen to your voice", "O")
print(test_function) # False
test_function = letter_check("Listen to your voice", "o")
print(test_function) # True           
print("----------------------------------")
# Practise 13
print("Practise #13")
# letter in word
print("e" in "blueberry") # True
print("a" in "blueberry") # False
print("blue" in "blueberry") # True
print("blue" in "strawberry") # False
print("----------------------------------")
# Practise 14
print("Practise #14")
def contains(big_string, little_string):
    return little_string in big_string

function_test = contains("Watermelon", "melon")
print(function_test) # True
print("----------------------------------")
# Practise 15
print("Practise #15")
def common_letters(string_one, string_two):
    common = []
    for letter in string_one:
        if (letter in string_two) and not (letter in common):
            common.append(letter)
    return common

function_test = common_letters("watermelon", "melon")
print(function_test) # ['e', 'm', 'l', 'o', 'n']
print("----------------------------------")
# Practise 16
print("Practise #16")
def username_generator(first_name, last_name):
    if len(first_name) < 3:
        user_name = first_name
    else:
        user_name = first_name[0:3]
    if len(last_name) < 4:
        user_name += last_name
    else:
        user_name += last_name[0:4]
    return user_name

function_test = username_generator("Homba", "Gomba")
print(function_test) # HombGomb
print("----------------------------------")
# Practise 17
print("Practise #17")
def password_generator(user_name):
    password = ""
    for i in range(0, len(user_name)):
        password += user_name[i-1]
    return password

function_test = password_generator("Funkey")
print(function_test) # yFunke
print("----------------------------------")
# Practise 18
print("Practise #18")
# String Methods
print('Hello world'.upper()) # HELLO WORLD
print('Hello world'.lower()) # hello world
print('Hello world'.title()) # Hello World
print('Hello world'.split()) # ['Hello', 'world']
print(' '.join(['Hello', 'world'])) # Hello world
print('Hello world'.replace('H', 'J')) # Jello world
print('   Hello world   '.strip()) # Hello world
print('{} {}'.format('Hello', 'world')) # Hello world
print("----------------------------------")