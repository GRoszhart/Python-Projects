import json

class InventoryItem:
    def __init__( self, itemName ):
        self.name = itemName
        self.totalStocked = 0
        self.totalInStock = 0
        self.totalSlots = 0
        
    def addToStocked( self, stockAmt ):
        self.totalStocked = self.totalStocked + stockAmt
        
    def addToInStock( self, inStockAmt ):
        self.totalInStock = self.totalInStock + inStockAmt
        
    def incrementSlots( self ):
        self.totalSlots = self.totalSlots + 1

    def getNumberSold( self ):
        return self.totalStocked - self.totalInStock
    
    def getSoldPct( self ):
        return self.getNumberSold() / self.totalStocked
    
    def getStockNeed( self ):
        return 8 * self.totalSlots - self.totalInStock
    
    def getName( self ):
        return self.name

    def getNumberInStock( self ):
        return self.totalInStock

    def __repr__( self ):
        return '{} In Stock: {}, Stocked: {}, Slots: {}'.format( self.name, self.totalInStock, self.totalStocked, self.totalSlots )

class MachineStatus:
    def __init__(self, machineLabel):
        self.label = machineLabel
        self.totalCurrentStock = 0
        self.totalLastStock = 0
        self.totalSales = 0
    
    def updateStatus(self,currentStock,lastStock,itemPrice):
        self.totalCurrentStock = self.totalCurrentStock + currentStock
        self.totalLastStock = self.totalLastStock + lastStock
        self.totalSales = self.totalSales + itemPrice * (lastStock - currentStock)
    
    def getLabel(self):
        return self.label
    
    def getTotalCurrentStock(self):
        return self.totalCurrentStock
    
    def getTotalLastStock(self):
        return self.totalLastStock
    
    def getTotalSales(self):
        return self.totalSales
    
    def getSoldPct(self):
        return (self.totalLastStock - self.totalCurrentStock) / self.totalLastStock
    

def main():
    print("Welcome to the Vending Status Checker!")
    print()
    inventoryFileNames = ["REID_1F_20171004.json", "REID_2F_20171004.json", "REID_3F_20171004.json"]
    itemNameToInventoryItem = {}
    vendingMachineDictionary = {}
    
    for inventoryFileName in inventoryFileNames: 
        inventoryFile = open(inventoryFileName,'r')
        
        inventoryData = json.loads(inventoryFile.read())
        
        contents = inventoryData['contents']
        vendingMachineLabel = inventoryData['machine_label']
        vendingMachine = vendingMachineDictionary.get(vendingMachineLabel, MachineStatus(vendingMachineLabel))

        for row in contents:
            for slot in row['slots']:
                itemName = slot['item_name']
                inventoryItem = itemNameToInventoryItem.get( itemName, InventoryItem( itemName ) )
                
                inventoryItem.addToStocked( slot['last_stock'] )
                inventoryItem.addToInStock( slot['current_stock'] )
                inventoryItem.incrementSlots();
                vendingMachine.updateStatus( slot['current_stock'], slot['last_stock'], slot['item_price'])
                                                                    
                itemNameToInventoryItem[itemName] = inventoryItem
                
        vendingMachineDictionary[vendingMachineLabel] = vendingMachine

    sortChoice = ''
    inventoryItemsList = list( itemNameToInventoryItem.values() )
    reportChoice = ''
    
    while reportChoice != 'q':
        reportChoice = input("Would you like to display the (m)achine report, (i)nventory report, or (q)uit? ")
        print()
        if reportChoice.lower() == 'q':
            break
        elif reportChoice.lower() == 'i':
            sortChoice = input('Sort by (n)ame, (p)ct sold, or (s)tocking need')
            print()
            if sortChoice == 'n':
                inventoryItemsList.sort( key=InventoryItem.getName )
            elif sortChoice == 'p':
                inventoryItemsList.sort( key=InventoryItem.getSoldPct )
                inventoryItemsList.reverse()
            elif sortChoice == 's':
                inventoryItemsList.sort( key=InventoryItem.getStockNeed )
                inventoryItemsList.reverse()
            if sortChoice.lower() in ['n','p','s']:
                print( 'Item Name            Sold     % Sold     In Stock Stock needs')
                for item in inventoryItemsList:
                    print( '{:20} {:8} {:8.2f}% {:8} {:8}'.format( item.getName(), item.getNumberSold(), item.getSoldPct() * 100, item.getNumberInStock(), item.getStockNeed()))
            else:
                print("Invalid inventory sort option selected.")
        elif reportChoice.lower() == 'm':
            print( 'Label           Pct Sold   Sales Total')
            for vMachine in vendingMachineDictionary.values():
                print( '{:11} {:10.2f} %    ${:8.2f}'.format(vMachine.getLabel(), vMachine.getSoldPct() * 100, vMachine.getTotalSales()))
        else:
            print("Invalid report option selected.")
        print()
    print("Thanks for using the vending status program!")
    
main()