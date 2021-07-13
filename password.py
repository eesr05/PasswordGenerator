import random
import string

print('Hello, Welcome to Password generator!')

#input the length of password
length = int(input('\nEnter the length of password: '))

#Define data
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
#symbols = string.punctuation

#combine the data
all = lower + upper + num 

#use random
temp = random.sample(all, length)

#create the password
password = "".join(temp)

print('New password: ' + password)


