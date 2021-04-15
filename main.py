#get Name function
def getName():
	userName = input("What's your name? ")
	#user name variable is specific to this function
	return userName
	print("Hello, " + userName)


def greetUser(name): #parameter variables are specific to the function
	print("Hello, " + name)
	#print("Hello, " + name + ". We need to talk")

greetUser(getName())
greetUser(getName())
greetUser(getName())

#ask the user for two numbers: num1 and num2
#write a function that takes num1 and num2 as parameters
#prints the sum


def sum(numList):
	total = 1
	for i in numList:
		total *= i
	print("The sum is " + str(total))

sum([1,2,3,4,5,6,7,8,9,10]) #55