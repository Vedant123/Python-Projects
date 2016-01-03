#Vedant Mathur
#RPN Evalutator

#Initializes class for the Tokens, to run the general logistics of the token
class Token:
    def __init__(self):
        self.value = ""
  
    def setValue(self, tokenVal):
        self.value = tokenVal

    def isDigit(self):
        return (self.value).isdigit()
    
    def getValue(self):
        return self.value

Tokens = list()
Stack = list()

#Prompts user for postfix expression
expression = input("Enter the postfix expression you wish to evaluate: ")

#Splits the expression by the delimeter of a space character
Tokens = expression.split(" ")

#Loops through the tokens
for x in range(0, len(Tokens)):
    #Implements the Token class
    token = Token()

    token.setValue(Tokens[x])

    #Checks if the token is a numerical value, and accordingly pushes it to the output stack
    if(token.isDigit()):
        Stack.append(float(token.getValue()))
    else:
        num2 = Stack.pop()
        num1 = Stack.pop()
        
        if(token.getValue() == "+"):
            Stack.append(num1 + num2)
        elif(token.getValue() == "-"):
            Stack.append(num1 - num2)
        elif(token.getValue() == "*"):
            Stack.append(num1 * num2)
        elif(token.getValue() == "/"):
            Stack.append(num1 / num2)
        elif(token.getValue() == "%"):
            Stack.append(num1 % num2)

#Prints answer
print(Stack.pop())
