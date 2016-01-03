class CD:
    def __init__(self):
        self.Title = ""
        self.Author = ""
        
        self.Cost = 0
        self.Songs = 0

    def setTitle(self, title):
        self.Title = title

    def setAuthor(self, author):
        self.Author = author

    def setCost(self, cost):
        self.Cost = cost

    def setSongCount(self, songCount):
        self.Songs = songCount

    def getTitle(self):
        return self.Title

    def getAuthor(self):
        return self.Author

    def getCost(self):
        return self.Cost

    def getSongCount(self):
        return self.Songs

    def getInfo(self):
        retArr = list()

        retArr.append(self.Title)
        retArr.append(self.Author)
        retArr.append(self.Cost)
        retArr.append(self.Songs)

        return retArr
    
class DataManager():
    def __init__(self):
        self.flag = ""
        self.fileReader = open("tunesData.txt", "r")
        self.fileData = list()
        
    def initializeFile(self):
        self.fileData = self.fileReader.read().split("\n")

    def addCD(self, inputCD):
        strEntry = "CD: "

        for x in range(0, 4):
            strEntry += inputCD.getInfo()[x] + ", "
            
        self.fileData.append(strEntry)
        
    def editCD(self, inputTitle, cdInfo):
        for x in range(0, len(self.fileData)):
            if(self.fileData[x][self.fileData[x].find(":") + 2: self.fileData[x].find(",")] == cdTitle):
                self.fileData[x] = self.fileData[x][self.fileData[x].find(":") + 2]
                
                for j in range(0, 4):
                     self.fileData[x] += cdInfo[j] + ", "
    
    def deleteCD(self, cdTitle):
        for x in range(0, len(self.fileData)):
            if(self.fileData[x][self.fileData[x].find(":") + 2: self.fileData[x].find(",")] == cdTitle):
                del fileData[x]
                
    def getInfo(self, title):
        for x in range(0, len(self.fileData)):
            if(self.fileData[x][self.fileData[x].find(":") + 2: self.fileData[x].find(",")] == title):
                retArr = list()

                retArr = self.fileData[x][self.fileData[x].find(":") + 2:].split(", ")

                return retArr

    def getCDs(self):
        retArr = list()

        for fileDataLine in self.fileData:
            if(len(fileDataLine) > 1):
                retArr.append(fileDataLine[fileDataLine.find(":") + 2:].split(", "))

        return retArr
    
    def write(self):
        dataOverWriter = open("tunesData.txt", 'w')

        for dataLine in self.fileData:
            if(len(dataLine) > 1):
                dataOverWriter.write(dataLine + "\n")

        dataOverWriter.close()

    def close(self):
        self.fileReader.close()

dataManager = DataManager()

dataManager.initializeFile()
        
print("***********************************Welcome to Tunes.***********************************")

choice = input("\n1. Add CD\n2. Edit CD\n3. Get CD Data\n4. View Tunes\n5. Terminate Program\n")

while(choice != "5"):
    if(choice == "1"):
        newCD = CD()

        title = input("Enter the title of the CD: \n")
        group = input("Enter the author of the CD: \n")
        cost = input("Enter the cost of the CD: \n")
        tuneCount = input("Enter the number of tunes on the recording: \n")

        newCD.setTitle(title)
        newCD.setAuthor(group)
        newCD.setCost(cost)
        newCD.setSongCount(tuneCount)

        dataManager.addCD(newCD)
    elif(choice == "2"):
        cdTitle = input("\nEnter the title of the CD: \n")
        
        print("\nEnter 1 to delete the CD: ")
        editChoice = input("Enter 2 to edit the CDs information: \n")

        if(editChoice == "1"):
            dataManager.delete(cdTitle)
        elif(editChoice == "2"):
            newCdInfo = list()

            newCdInfo.append(cdTitle)
            
            newCdInfo.append(input("Enter the author of the CD: \n"))
            newCdInfo.append(input("Enter the cost of the CD: \n"))
            newCdInfo.append(input("Enter the number of tunes on the recording: \n"))

            dataManager.editCD(cdTitle, newCdInfo)
    elif(choice == "3"):
        userTitle = input("\nEnter the title of the CD: \n")

        cdInfo = dataManager.getInfo(userTitle)

        print("\nTitle: " + cdInfo[0])
        print("Author: " + cdInfo[1])
        print("Cost: " + cdInfo[2])
        print("Songs in Recording: " + cdInfo[3])

    elif(choice == "4"):
        CdList = dataManager.getCDs()
        IndexOrder = list()

        sortChoice = input("\nEnter 1 to sort by title. \nEnter 2 to sort by author.\n")
        
        print("|       Title        |       Author       |       Cost         |   Songs in Recording    |")
        print("------------------------------------------------------------------------------------------")

        for x in range(0, len(CdList)):
            if(len(CdList[x]) > 1):
                if(sortChoice == "1"):
                    IndexOrder.append(CdList[x][0] + str(x))
                elif(sortChoice == "2"):
                    IndexOrder.append(CdList[x][1] + str(x))

        IndexOrder.sort()

        for x in range(0, len(IndexOrder)):
            IndexOrder[x] = IndexOrder[x][-1]

        for x in range(0, len(IndexOrder)):
            print("|", end = "")
            
            for j in range(0, 4):
                currentItem = CdList[int(IndexOrder[x][0])][j]
                
                spaceIndex = int((20 - len(currentItem)) / 2)

                if(j != 3):
                    print((" " * (spaceIndex)) + currentItem + (" " * ((20 - len(currentItem)) - spaceIndex)) + "|", end = "")
                else:
                    print((" " * (spaceIndex + 3)) + currentItem + (" " * ((20 - len(currentItem)) - spaceIndex + 2)) + "|", end = "") 
            print("")
            
        print("\n")      

    print("")
    choice = input("1. Add CD\n2. Edit CD\n3. Get CD Data\n4. View Tunes\n5. Terminate Program\n")
    
dataManager.write()
dataManager.close()
        
