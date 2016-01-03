class Stock:
    def __init__(self):
        self.Company = ""
        self.Ticker = ""
        self.Shares = 0
        self.Pur = 0.0
        self.Latest = 0.0
        self.Value = 0
        self.GL = 0.0

        self.infoArr = list()
    
    def setTicker(self, tickerSymbol):
        self.Ticker = tickerSymbol

        self.infoArr.append(tickerSymbol)

    def setCompany(self, company):
        self.Company = company

        self.infoArr.append(company)

    def setShares(self, share):
        self.Shares = share

        self.infoArr.append(share)
        
    def setPur(self, pur):
        self.Pur = pur

        self.infoArr.append(pur)
        
    def setLatest(self, latest):
        self.Latest = latest

        self.infoArr.append(latest)
        
    def setValue(self, value):
        self.Value = value

        self.infoArr.append(value)
        
    def setGL(self, gl):
        self.GL = gl

        self.infoArr.append(gl)

    def getTicker(self):
        return self.ticker()
    
    def getInfo(self):
        return self.infoArr
    
class FileManager:
    def __init__(self):
        self.fileReader = open("portfolio.dat")
        self.fileData = list()

        self.filePath = ""
        
    def loadFile(self, filePath):
        self.fileReader = open(filePath)
        
        self.fileData = self.fileReader.read().split("\n")

        for x in range(0, len(self.fileData)):
            if(self.fileData[x] == ''):
                del self.fileData[x]
            else:
                self.fileData[x] = self.fileData[x].split("\t")

        self.filePath = filePath
        
    def swap(self, inputArr, indexA, indexB):
        temp = inputArr[indexB]

        inputArr[indexB] = inputArr[indexA]
        inputArr[indexA] = temp
        
    def addStock(self, stock):
        dataList = list()
        
        for item in stock.getInfo():
            dataList.append(str(item))
            
        self.fileData.append(dataList)
  
    def deleteStock(self, ticker):
        for x in range(0, len(self.fileData)):
            if(self.fileData[x][0] == ticker):
                del self.fileData[x]
    
    def update(self):
        print("Update stock prices (<Return> to keep current value)...\n")

        for x in range(0, len(self.fileData)):
            newPrice = input(self.fileData[x][0] + ": ")
            
            if(newPrice[0].isdigit()):
                self.fileData[x][4] = newPrice
                self.fileData[x][5] = int(float(newPrice) * float(self.fileData[x][2]))
                self.fileData[x][6] = "%.1f" % (((float(newPrice) / float(self.fileData[x][3])) - 1) * 100)
    
    def report(self):
        sortChoice = input("Sort output on (N)ame, or (V)alue? ")

        bkpArr = self.fileData
        
        if(sortChoice.lower() == "n"):
            for x in range(0, len(bkpArr)):
                self.swap(bkpArr[x], 0, 1)
              
            bkpArr.sort()

            for x in range(0, len(bkpArr)):   
                self.swap(bkpArr[x], 0, 1)
        elif(sortChoice.lower() == "v"):
            for x in range(0, len(bkpArr)):
                self.swap(bkpArr[x], 0, 5)
                bkpArr[x][0] = float(bkpArr[x][0])
                
            bkpArr.sort()
            
            for x in range(0, len(bkpArr)):
                self.swap(bkpArr[x], 0, 5)
                bkpArr[x][5] = str(bkpArr[x][5])
        self.fileData = bkpArr    
            
        print("")
        
        print("Company                 Shares    Pur.    Latest    Value    G/L")
        print("==================================================================")

        for x in range(0, len(self.fileData)):
            reportLine = ""

            reportLine += self.fileData[x][1] + " (" + self.fileData[x][0] + ")"
            
            reportLine += (" " * (28 - len(self.fileData[x][2]) + 1 - len(reportLine)))
            reportLine += self.fileData[x][2]

            reportLine += (" " * (37 - len(self.fileData[x][3]) + 1 - len(reportLine)))
            reportLine += self.fileData[x][3]
            
            reportLine += (" " * (47 - len(self.fileData[x][4]) + 1 - len(reportLine)))
            reportLine += self.fileData[x][4]
            
            reportLine += (" " * (56 - len(str(self.fileData[x][5])) + 1 - len(reportLine)))
            reportLine += str(self.fileData[x][5])
           
            reportLine += (" " * (63 - len(str(self.fileData[x][6])) + 1 - len(reportLine)))
            reportLine += str(self.fileData[x][6] + "%")

            print(reportLine)
    
    def write(self):
        fileOverWriter = open(self.filePath, 'w')
        
        for x in range(0, len(self.fileData)):
            for j in range(0, len(self.fileData[x])):
                fileOverWriter.write(self.fileData[x][j] + "\t")

            fileOverWriter.write("\n")
            
        fileOverWriter.close()
        
    def close(self):
        self.fileReader.close()
def main():
    choice = "-1"
    
    fileManager = FileManager()
    
    while(choice.lower() != "q"):
        choice = input("(A)dd/(D)elete stocks, (L)oad file, (U)pdate prices, (R)eport, or (Q)uit?\n")

        if(choice.lower() == "a"):
            newStock = Stock()
            
            print("Add a stock to your portfolio... \n")
            
            newStock.setTicker(input("Ticker: "))
            newStock.setCompany(input("Company name: "))
            newStock.setShares(input("Number of shares: "))
            newStock.setPur(float(input("Purchase price per share: ")))
            newStock.setLatest(float(newStock.getInfo()[3]))
            newStock.setValue(str(int(newStock.getInfo()[2]) * newStock.getInfo()[4]))
            newStock.setGL(1 - newStock.getInfo()[4] / newStock.getInfo()[3])

            fileManager.addStock(newStock)
            
            print("")
        elif(choice.lower() == "d"):
            delTicker = input("Enter the ticker symbol of the stock  to remove: ")
        elif(choice.lower() == "l"):
            fileManager.loadFile(input("Load file: "))
            print("")
        elif(choice.lower() == "u"):
            fileManager.update()
            print("")
        elif(choice.lower() == "r"):
            fileManager.report()
            print("")
        elif(choice.lower() == "q"):
            print("")

    fileManager.write()
    fileManager.close()
    
main()
