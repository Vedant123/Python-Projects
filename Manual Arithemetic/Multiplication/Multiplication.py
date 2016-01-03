#Vedant Mathur
#Program to replicate the conventional multiplication algorithm

num1 = ""
num2 = ""

#prompts user for numbers
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

#answer array
answer = ["0"] * 120

#initialization of the final product string
product = ""

#index to remove the leading 0s
index = 0

#nested for loops to iterate through both numbers
for x in range(0, len(num1)):
    for f in range(0, len(num2)):
        #initializes the variable prod to the sum of the digits in the string
        prod = int(num1[- x - 1]) * int(num2[- f - 1])

        #creates a variable "productDigit", and assigns the value of the "prod" + the current value in the sum
        productDigit = int(prod + int(answer[-x-f-1]))

        #creates an integer that holds the units digit of "productDigit"
        productDigitAns = 0
        productDigitAns =  productDigit - int(productDigit / 10) * 10

        #assigns the respective item in the "answer" array to the digits
        answer[-x - f - 1] = str(productDigitAns)
        answer[-x - f - 2] = int(productDigit / 10) + int(answer[-x -f - 2])

        #checks if there is a two digit number in only one element of the array, and then runs through the carry algorithm
        if(int(answer[-x - f - 1]) > 10):
            answer[-x - f - 2] = int(answer[-x - f - 2]) + int(answer[-x - f - 1] / 10)
            answer[-x - f - 1] = int(answer[-x - f - 1]) - int(answer[-x - f - 1] / 10) * 10

#increments the index integer to ignore the leading 0s   
while(answer[index] == "0"):
    index += 1

#adds the items of the "answer" array to the final product string
for x in range(index + 1, len(answer)):
    product = str(product) + str(answer[x])

#prints the product
print(product)
