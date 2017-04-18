#Demonstrates the Collatz Sequence

#Define the collatz function
def collatz(number):
    while (number != 1):
        
        #If the value is even, divide by 2
        if number % 2 == 0:
            number = number / 2
            
        #Else, if the value is odd, multiple by 3 and add 1
        else:
            number = 3 * number + 1
            
        print(int(number))

#Collect user input
userInput = input()

#Error handling to validate input as an integer, call the collatz function
try:
    collatz(int(userInput))
except ValueError:
    print('Error: You must input an integer')
