# IMPORTS
from datetime import datetime
import os
import time
# VARIABLES
# Stocks in order are Brake Pads, Tyres, Engines, Spark Plugs, Ignition Coils, Batteries, Radiators, Timing Belt, Water Pump, Fuel Cap, Oxygen Sensor, Gearbox
Stocks = [5,5,5,5,5,5,5,5,5,5,5,5]
Loop = True
ServiceRequest = "Brake Pads"
HourlyRate = 50
TaxRate = 1.2
RepairList = ("Brake Pads, Tyres, Engines, Spark Plugs, Ignition Coils, Batteries, Radiators, Timing Belt, Water Pump, Fuel Cap, Oxygen Sensor, Gearbox, Full Service, Interim")
RepairType = ""
Name = ""
# DEFINE TIME BASED OFF SYSTEM
Date = datetime.today().strftime('%Y-%m-%d')
# CLASS FOR ALL STOCK FUNCTIONS
class Stock:
    # FUNCTION TO REMOVE STOCK MANUALLY
    def Remove():
        RemoveStock = input("Remove which Stock? ")
        if RemoveStock.lower() == "brake pads":
            Stocks[0] = Stocks[0] - 1
        elif RemoveStock.lower() == "tyres":
            Stocks[1] = Stocks[1] - 1
        elif RemoveStock.lower() == "engines":
            Stocks[2] = Stocks[2] - 1
        elif RemoveStock.lower() == "spark plugs":
            Stocks[3] = Stocks[3] - 1
        elif RemoveStock.lower() == "ignition coils":
            Stocks[4] = Stocks[4] - 1
        elif RemoveStock.lower() == "batteries":
            Stocks[5] = Stocks[5] - 1
        elif RemoveStock.lower() == "radiators":
            Stocks[6] = Stocks[6] - 1
        elif RemoveStock.lower() == "timing belt":
            Stocks[7] = Stocks[7] - 1
        elif RemoveStock.lower() == "water pump":
            Stocks[8] = Stocks[8] - 1
        elif RemoveStock.lower() == "fuel cap":
            Stocks[9] = Stocks[9] - 1
        elif RemoveStock.lower() == "oxygen sensor":
            Stocks[10] = Stocks[10] - 1
        elif RemoveStock.lower() == "gearbox":
            Stocks[11] = Stocks[11] - 1
    # FUNCTION TO CHECK STOCK LEVELS
    def Check():
        CheckStock = input("Check which Stock? ")
        if CheckStock.lower() == "brake pads":
            print(str(Stocks[0]) +" "+ str(CheckStock))
        elif CheckStock.lower() == "tyres":
            print(str(Stocks[1]) +" "+ str(CheckStock))
        elif CheckStock.lower() == "engines":
            print(str(Stocks[2]) +" "+ str(CheckStock))
        elif CheckStock.lower() == "spark plugs":
            print(str(Stocks[3]) +" "+ str(CheckStock))
        elif CheckStock.lower() == "ignition coils":
            print(str(Stocks[4]) +" "+ str(CheckStock))
        elif CheckStock.lower() == "batteries":
            print(str(Stocks[5]) +" "+ str(CheckStock))
        elif CheckStock.lower() == "radiators":
            print(str(Stocks[6]) +" "+ str(CheckStock))
        elif CheckStock.lower() == "timing belt":
            print(str(Stocks[7]) +" "+ str(CheckStock))
        elif CheckStock.lower() == "water pump":
            print(str(Stocks[8]) +" "+ str(CheckStock))
        elif CheckStock.lower() == "fuel cap":
            print(str(Stocks[9]) +" "+ str(CheckStock))
        elif CheckStock.lower() == "oxygen sensor":
            print(str(Stocks[10]) +" "+ str(CheckStock))
        elif CheckStock.lower() == "gearbox":
            print(f"{Stocks[11]} {str(CheckStock)}")
    # FUNCTION TO ADD STOCK MANUALLY
    def Add():
        BuyStock = input("Which Stock do you need to buy?")
        if BuyStock.lower() == "brake pads":
            Stocks[0] = Stocks[0] + 1
        elif BuyStock.lower() == "tyres":
            Stocks[1] = Stocks[1] + 1
        elif BuyStock.lower() == "engines":
            Stocks[2] = Stocks[2] + 1
        elif BuyStock.lower() == "spark plugs":
            Stocks[3] = Stocks[3] + 1
        elif BuyStock.lower() == "ignition coils":
            Stocks[4] = Stocks[4] + 1
        elif BuyStock.lower() == "batteries":
            Stocks[5] = Stocks[5] + 1
        elif BuyStock.lower() == "radiators":
            Stocks[6] = Stocks[6] + 1
        elif BuyStock.lower() == "timing belt":
            Stocks[7] = Stocks[7] + 1
        elif BuyStock.lower() == "water pump":
            Stocks[8] = Stocks[8] + 1
        elif BuyStock.lower() == "fuel cap":
            Stocks[9] = Stocks[9] + 1
        elif BuyStock.lower() == "oxygen sensor":
            Stocks[10] = Stocks[10] + 1
        elif BuyStock.lower() == "gearbox":
            Stocks[11] = Stocks[11] + 1
# CLASS FOR ALL CUSTOMER ACTIONS AND INPUTS
class Customer:
    # GET DETAILS FOR INVOICE FROM CUSTOMER
    def GetDetails():
        CustomerName = input("What is your name? ")
        CustomerVehicleMake = input("What is your name? ")
    # FUNCTION TO FIGURE OUT THE REPAIR TYPE
    def RepairFind():
        print(RepairList)
        RepairType = input("What repair is needed")
    # FUNCTION TO DO THE REPAIR
    def DoRepair():
        if RepairType.lower() == "brake pads":
            UseNum = input("How many are needed? ")
            Stocks[0] = Stocks[0] - (1 * UseNum)
            Cost = Cost + (UseNum * 30)
            LabourTime = LabourTime + (UseNum * 0.25)
        elif RepairType.lower() == "tyres":
            UseNum = input("How many are needed? ")
            Stocks[0] = Stocks[0] - (1 * UseNum)
            Cost = Cost + (UseNum * 50)
            LabourTime = LabourTime + (UseNum * 1)
        elif RepairType.lower() == "engine":
            Stocks[0] = Stocks[0] - 1
            Cost = Cost + (4000)
            LabourTime = LabourTime + (11)
        elif RepairType.lower() == "spark plugs":
            UseNum = input("How many are needed? ")
            Stocks[0] = Stocks[0] - (1 * UseNum)
            Cost = Cost + (UseNum * 20)
            LabourTime = LabourTime + (UseNum * 0.25) 
        elif RepairType.lower() == "ignition coils":
            Stocks[0] = Stocks[0] - 1
            Cost = Cost + (175)
            LabourTime = LabourTime + (0.25)
        elif RepairType.lower() == "batteries":
            Stocks[0] = Stocks[0] - 1
            Cost = Cost + (70)
            LabourTime = LabourTime + (1)
        elif RepairType.lower() == "radiators":
            Stocks[0] = Stocks[0] - 1
            Cost = Cost + (200)
            LabourTime = LabourTime + (3)
        elif RepairType.lower() == "timing belt":
            Stocks[0] = Stocks[0] - 1
            Cost = Cost + (100)
            LabourTime = LabourTime + (6)
        elif RepairType.lower() == "water pump":
            Stocks[0] = Stocks[0] - 1
            Cost = Cost + (250)
            LabourTime = LabourTime + (2)
        elif RepairType.lower() == "fuel cap":
            Stocks[0] = Stocks[0] - 1
            Cost = Cost + (20)
            LabourTime = LabourTime + (0.25)
        elif RepairType.lower() == "oxygen sensor":
            Stocks[0] = Stocks[0] - 1
            Cost = Cost + (300)
            LabourTime = LabourTime + (1)
        elif RepairType.lower() == "gearbox":
            Stocks[0] = Stocks[0] - 1
            Cost = Cost + (1500)
            LabourTime = LabourTime + (10)
# ENTER LOOP
while Loop == True:
    os.system('cls' if os.name == 'nt' else 'clear')
    MenuAction = input("1. Stock \n2. Repair\n3. Service\n4. Exit\n")
    if MenuAction == "1":
        StockAct = Stock
        os.system('cls' if os.name == 'nt' else 'clear')
        MenuAction = input("1. Check \n2. Remove\n3. Add\n")
        if MenuAction == "1":
            Stock.Check()
            time.sleep(3)
        elif MenuAction == "2":
            Stock.Remove()
        elif MenuAction == "3":
            Stock.Add()
    elif MenuAction == "2":
            print("WIP")
    elif MenuAction == "3":
            print("WIP")
    elif MenuAction == "4":
            print("WIP")
    for i in range(len(Stocks)):
        if Stocks[i] > 1:
            Loop = False
'''END NOTES
STILL NEED TO MAKE CLASS FOR SERVICES
NEED TO ADD MENU FUNCTIONS 2,3 AND 4
INVOICE MAKER
MAKE CUSTOMER ENTER DETAILS'''