
def factorial(num):
	number = num
	for i in range (1,number):
		num *=i
	return num
		
	
def main():
	number = input("Enter a number")
	print ("Factorial is : ",factorial(number))
if __name__ =="__main__": main()
