class Student:
    def __init__(self):
        self.name = ""
        self.gradeLevel = 0
        self.address = ""
        self.grade = ""

    def setName(self, name):
        self.name = name

    def setGradeLevel(self, gradeLevel):
        self.gradeLevel = gradeLevel

    def setAddress(self, address):
        self.address = address

    def setGrade(self, grade):
        self.grade = grade

    def getName(self):
        return self.name

    def getGrade(self):
        return self.grade

    def getAddress(self):
        return self.address

    def getGrade(self):
        return self.grade
class Class:
    def __init__(self):
        self.students = list()
        
class FileManager:
    def __init__(self):
        self.fileReader = open("studentData.txt", 'r')
        self.fileData = list()
        
    def readFile(self):
        self.fileData = self.fileReader.read().split("Class: ")

        for x in range(0, len(self.fileData)):
            self.fileData[x] = self.fileData[x].split("\n")

        del self.fileData[0]
        
    def write(self):
        fileOverWriter = open("studentData.txt", 'w')

        for dataLine in self.fileData:
            if(len(dataLine) > 1):
                dataOverWriter.write(dataLine + "\n")

        dataOverWriter.close()

    def getFileData(self):
        return self.fileData
    
    def close(self):
        self.fileReader.close()

classSize = 0



def swap(arr, indexA, indexB):
    temp = arr[indexB]

    arr[indexB] = arr[indexA]
    arr[indexA] = temp

def generateGrade(aCount, bCount, cCount, dCount, fCount, percentage, classNo):
    if(percentage >= 90 and percentage <= 100):
        aCount[classNo] += 1
        
        return "A"
    elif(percentage >= 80):
        bCount[classNo] += 1

        return "B"
    elif(percentage >= 70):
        cCount[classNo] += 1
        
        return "C"
    elif(percentage >= 65):
        dCount[classNo] += 1
        
        return "D"
    elif(percentage >= 50):
        fCount[classNo] += 1
        
        return "F"
    else:
        return "Invalid"

def main():
    global classSize
    
    fileManager = FileManager()

    fileManager.readFile()
    
    studentDataLines = fileManager.getFileData()

    Classes = list()
    
    indexOrder = list()

    classSize = len(studentDataLines)
    
    classCount = 0

    aCount = [0] * classSize
    bCount = [0] * classSize
    cCount = [0] * classSize
    dCount = [0] * classSize
    fCount = [0] * classSize

    for x in range(0, len(studentDataLines)):
        print("-------------------Class: " + studentDataLines[x][0] + "-------------------")

        Classes.append(studentDataLines[x][0])
        
        for j in range(0, len(studentDataLines[x])):
            studentDataLines[x][j] = studentDataLines[x][j].split("\t")
            
            swap(studentDataLines[x][j], 0, -1)

            if(studentDataLines[x][j][0].isdigit()):
                studentDataLines[x][j][0] = int(studentDataLines[x][j][0])
            
        del studentDataLines[x][0]

        while(studentDataLines[x][-1] == ['']):
            del studentDataLines[x][-1]
        
        studentDataLines[x].sort()
        
        for j in range(0, len(studentDataLines[x])):
            swap(studentDataLines[x][j], 0, -1)
            print("Name: " + studentDataLines[x][j][0])
            print("Grade Level: " + studentDataLines[x][j][1])
            print("Percentage: " + str(studentDataLines[x][j][3]))
            print("Grade: " + generateGrade(aCount, bCount, cCount, dCount, fCount, int(studentDataLines[x][j][3]), classCount))

            print("")
         
        classCount += 1
        
    print("")

    seperationChoice = input("Do you wish to seperate the classes in the graph. Enter 1 for Yes and 0 for No.\n")

    if(seperationChoice == "1"):
        print("")
        
        for x in range(0, classSize):
            print("Class " + Classes[x] + ": ")
            print("A (90-100)\t| " + "*" * aCount[x])
            print("B (80-89)\t| " + "*" * bCount[x])
            print("C (70-79)\t| " + "*" * cCount[x])
            print("D (65-69)\t| " + "*" * dCount[x])
            print("F (50-64)\t| " + "*" * fCount[x])

            print("")
            
    elif(seperationChoice == "0"):
        print("A (90-100)\t| " + "*" * sum(aCount))
        print("B (80-89)\t| " + "*" * sum(bCount))
        print("C (70-79)\t| " + "*" * sum(cCount))
        print("D (65-69)\t| " + "*" * sum(dCount))
        print("F (50-64)\t| " + "*" * sum(fCount))
    
main()
