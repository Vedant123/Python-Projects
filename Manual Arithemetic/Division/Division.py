#Vedant Mathur
#Divides large numbers to a certain degree of accuracy

#prompts user for information
num1 = input("Enter the number you wish to divide: ")
num2 = input("Enter the divisor: ")
num3 = int(input("Enter the number of decimal points you want it to contain: "))

#splits the dividend
num1Arr = list(num1)

"""if the user wants a decimal within their answer, this will add a respective number of 0s so that the decimal aspects can be continued.
The decimal point will come later"""

num1Arr = num1Arr + ["0"] * (num3)

#intializes the answer array
ansArr = ["0"] * 60

ansIndex = 0

#iterates through the dividend
for x in range(0, len(num1Arr)):
    #pushes the quotient of the digit divded by the divisor with an int cast onto the answer array
    ansArr[x] = int(int(num1Arr[x]) / int(num2))

    #adds the modulus of the division * 10 to the next digit
    if(x != (len(num1Arr) - 1)):
        num1Arr[x + 1] = str(int(num1Arr[x + 1]) + int(num1Arr[x]) % int(num2) * 10)


#removes 0s
ansArr = ansArr[:len(num1Arr)]

#inserts the decimal point
ansArr.insert(len(num1Arr) - num3, ".")

#removes leading 0s
while(ansArr[ansIndex] == 0):
    del ansArr[ansIndex]

#converts the answert array into a string and prints it
print(''.join(map(str, ansArr)))
