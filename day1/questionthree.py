
# import the string library in order to get access to its properties
import string
import random

LETTERS = string.ascii_letters
NUMBERS = string.digits  
SYMBOLS = string.punctuation    

from random import *

pass_strength = input("How strong do you want your password to be?")
    # a weak password will only contain letters while a very strong password will contain both letters, special symbols and alphanumerics
if (pass_strength == "weak"):
   characters1 = string.ascii_letters 
   password1 =  "".join(choice(characters1) for x in range(randint(2, 8)))
   print(password1)
elif (pass_strength == "strong"):
    characters2 = string.ascii_letters +  string.digits
    password2 =  "".join(choice(characters2) for x in range(randint(4, 10)))
    print(password2)
elif (pass_strength == "very strong"):
    characters3 = string.ascii_letters + string.punctuation  + string.digits
    password3 =  "".join(choice(characters3) for x in range(randint(6, 15)))
    print(password3)
else:
    print("Kindly enter either strong, weak or very strong ")



