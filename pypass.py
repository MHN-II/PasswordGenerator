#10-24 characters
#1 upper case 1 lowe case 
#1 number
# q special character 

from random import randint, shuffle 
Password = ''
special = "-|@.,?/!~#%^&*(){}[]\=*"

def rdmNum():
	num =randint(0,9)
	return str(num)

def rdmLower():
	num = chr(randint(97,122))
	return num

def rdmUpper():
	num = chr(randint(65,90))
	return num

def scramble(word):
	wordmix = list(word)
	shuffle(wordmix)
	Password = ''.join(wordmix)
	return Password

def rdmSpecial(): 
	speciallist = list(special)
	num =randint(0,22)
	return speciallist[num]



print('Password Generator')
print('Enter Length of Password (10-24 characters)')
plength = int(input())
			
for i in range(plength): 
	
	mod = i%4
	if mod == 0: 
		Password = Password+rdmNum()
	if mod == 1: 
		Password = Password+rdmLower()
	if mod == 2: 
		Password = Password+rdmUpper()
	if mod == 3: 
		Password = Password+rdmSpecial()


Password = scramble(Password)
print()
print('Your Password is :'+Password)		


		