inputString = input("Enter the string you wish to test: ")

inputString = inputString.replace(" ", "")
inputString = inputString.replace(",", "")
inputString = inputString.replace("'", "")

inputString = inputString.lower()
    
if(inputString == inputString[::-1]):
    print("Palindrome True")
else:
    print("Palindrome False")
            
while(input != ""):
    inputString = input("Enter the string you wish to test: ")

    inputString = inputString.replace(" ", "")
    inputString = inputString.replace(",", "")
    inputString = inputString.replace("'", "")
    
    inputString = inputString.lower()

    if(inputString == inputString[::-1]):
        print("Palindrome True")
    else:
        print("Palindrome False")
