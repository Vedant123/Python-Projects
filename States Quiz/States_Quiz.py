import random

#this class manages the user capabilities
class userManager:
    def __init__(self):
        self.userName = ""
        self.userScore = 0

        self.data = [""]
        
        self.dataWriter = open("userData.txt", 'r+')
        
    def setName(self, name):
        self.userName = name

    def setScore(self, score):
        self.userScore = score

    def addScore(self, userName, userScore):
        for x in range(0, len(self.data)):
            if(self.data[x][:self.data[x].find(" ")] == userName):
                self.data[x] = self.data[x][:-2] + " " + userScore + " ]"
                
                return

        self.data.append(userName + " - " + "[" + userScore + " ]")
        
    def getScores(self, userName):
        userScores = ""
        
        for x in range(0, len(self.data)):
            if(self.data[x][:self.data[x].find(" ")] == userName):
                userScores = self.data[x][self.data[x].find("[") + 1: self.data[x].find("]") - 1].split(" ")

        return userScores
        
    def readFile(self):
        self.data = self.dataWriter.read().split('\n')

    def exists(self, userName):
        for x in range(0, len(self.data)):
            if(self.data[x][:self.data[x].find(" ")] == userName):
                return True

        return False

    def write(self):
        dataOverWriter = open("userData.txt", 'w+')
        
        for x in range(0, len(self.data)):
            line = self.data[x]
            
            dataOverWriter.write(line + "\n")

        dataOverWriter.close()

    def close(self):
        self.dataWriter.close()
        
UserManager = userManager()

#states and capitals array that were genereated through text file analysis    
states = ["Alabama", "Alaska ", "Arizona ", "Arkansas ", "California ", "Colorado ", "Connecticut ", "Delaware ", "Florida ", "Georgia ", "Hawaii ", "Idaho ", "Illinois ",  "Indiana ", "Iowa ", "Kansas ", "Kentucky ", "Louisiana ", "Maine ", "Maryland ", "Massachusetts ", "Michigan ", "Minnesota ", "Mississippi ", "Missouri ", "Montana",  "Nebraska ", "Nevada ", "New Hampshire ", "New Jersey ", "New Mexico ", "New York ", "North Carolina ", "North Dakota ", "Ohio ", "Oklahoma ", "Oregon ", "Pennsylvania",  "Rhode Island ", "South Carolina ", "South Dakota ", "Tennessee ", "Texas ", "Utah ", "Vermont ", "Virginia ", "Washington ", "West Virginia ", "Wisconsin ", "Wyoming"]
capitals = ["Montgomery", "Juneau", "Phoenix", "Little Rock", "Sacramento", "Denver", "Hartford", "Dover", "Tallahassee", "Atlanta", "Honolulu", "Boise", "Springfield", "Indianapolis", "Des Moines", "Topeka", "Frankfort", "Baton Rouge", "Augusta", "Annapolis", "Boston", "Lansing", "St. Paul", "Jackson", "Jefferson City", "Helena", "Lincoln", "Carson City", "Concord", "Trenton", "Santa Fe", "Albany", "Raleigh", "Bismarck", "Columbus", "Oklahoma City", "Salem", "Harrisburg", "Providence", "Columbia", "Pierre", "Nashville", "Austin", "Salt Lake City", "Montpelier", "Richmond", "Olympia", "Charleston", "Madison", "Cheyenne"]

#initializes the avaliableStates array
avaliableStates = [0] * 50

#initializes the score to 0
score = 0

UserManager.readFile()

#sets the avaliableStates to values from 0 to 49
for x in range(0, 50):
    avaliableStates[x] = x

def runGame(userName):
    global score
    
    for x in range(0, 10):
        currentState = random.randint(0, len(avaliableStates) - 1)
        
        answer = input("What is the state capital of " + states[avaliableStates[currentState]] + ": ")

        if(answer == capitals[avaliableStates[currentState]]):
            print("Correct!\n")

            score += 1
        else:
            print("Incorrect. The answer actually was " + capitals[avaliableStates[currentState]] + '\n')

        del avaliableStates[currentState]

    print("Your final score was " + str(score * 10) + "%\n")

    UserManager.addScore(userName, str(score * 10))


choice = -1

while(choice != 3):
    name = input("Please enter your name: \n")
    
    if(UserManager.exists(name)):
        choice = int(input("\nWelcome back " + name + ". To play the game, enter 1. To check your scores, enter 2. To terminate the game, enter 3\n\n"))

        if(choice == 1):
            runGame(name)
        elif(choice == 2):
            print("**************" + name + "**************")

            for x in range(0, len(UserManager.getScores(name))):
                print(UserManager.getScores(name)[x] + "%")

            print("")
    else:
        choice = int(input("\nHello " + name + ". To play the game, enter 1. To terminate the game, enter 3\n"))

        if(choice == 1):
            runGame(name)

UserManager.write()
UserManager.clocheesse()

