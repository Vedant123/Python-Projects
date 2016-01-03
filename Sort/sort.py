import random

#Searching Class
class SearchingTool:
    def __init__(self):
        self.index = 0

    #searches array through an iteration
    def searchArray(self, arr, value):
        for x in range(0, len(arr)):
            if(str(arr[x]) == str(value)):
                return x
            
        return -1
    
#prompts user for their choices
choice = input("Is the data you want a number or string: ")
sortChoice = input("Enter 0 for bubble sort and 1 for selection sort: ")

#swaps two index values
def swap(inputArr, indexA, indexB):
    temp = inputArr[indexA]

    inputArr[indexA] = inputArr[indexB]
    inputArr[indexB] = temp
    
def bubbleSort(inputArr):
    decrementIndex = 0

    swapped = True

    #continues the loop until the n^2 has been achieved
    while(swapped):
        decrementIndex += 1

        swapped = False

        #iterates through the loop until the len(inputArr) - decrementIndex, becuase the largest numbers move per iteration, meaning one less index is needed
        for x in range(0, len(inputArr) - decrementIndex):
            if(inputArr[x] > inputArr[x + 1]):
                swap(inputArr, x, x + 1)

                #displays the progress of the algorithm
                print(inputArr)
                
                swapped = True

def selectionSort(inputArr):
    #iterates through the array
    for x in range(0, len(inputArr) - 1):
        index = x

        #displays the progress of the algorithm
        print(inputArr)

        #iterates through the array again checking if the current lowest number is truely the lowest
        for j in range(x + 1, len(inputArr) ):
            if(inputArr[index] > inputArr[j]):
                index = j

        if(index != x):
            swap(inputArr, x, index)

arr = list()            

#generates the 100 elements of the array
for x in range(0, 30):
    if(choice.lower() == "numbers" or choice.lower() == "number"):
        randomNumber = random.randint(0, 999)

        #checks if the randomNumber exists in the array, and will continue to change it until it's not
        while(randomNumber in arr):
            randomNumber = random.randint(0, 999)

        arr.append(randomNumber)
        
    elif(choice.lower() == "strings" or choice.lower() == "string"):
        randomNumber = random.randint(65, 122)

        while(chr(randomNumber) in arr):
            randomNumber = random.randint(65, 122)
            
        arr.append(chr(randomNumber))
        

#prints the initial array    
print(arr)

#checks the sortChoice, and accordingly performs the respective sort
if(sortChoice == "0"):
    bubbleSort(arr)
if(sortChoice == "1"):
    print(arr)
    selectionSort(arr)

print("\n --------------------------------------------Sorted Array --------------------------------------------")

searchCheck = input("\nDo you want to search for a specific element in the array. Enter Yes if so: ")

#checks if the user wants to search for an index
if(searchCheck.lower() == "yes"):
    searchingTool = SearchingTool()
    
    value = input("Enter the value you wish to search for: ")

    valIndex = searchingTool.searchArray(arr, value)

    #checks if the index exists
    if(valIndex != -1):
        print("Value found at index " + str(valIndex))
    else:
        print("Not found")
    
