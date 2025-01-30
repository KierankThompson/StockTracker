import os
import csv
import configparser
from datetime import datetime

def is_valid_date(date_string):
    try:
        datetime.strptime(date_string, '%Y-%m-%d')
        return True
    except ValueError:
        return False
    
def get_current_date():
    return datetime.today().strftime('%Y-%m-%d')

def ask_YN_question(prompt):
    var_Str = ""
    while var_Str := var_Str.lower().strip() not in ("y", "n", "yes", "no"):
        var_Str = input(prompt)
    if var_Str in ("y","yes"):
        return 'Yes'
    else:
        return 'No'


def initialize():

    #Set up stock tracker
    if not os.path.exists("stocks.csv"):
        with open("stocks.csv", 'w', newline='') as csvfile:
            fieldnames = ["symbol", "amount", "date purchased", "initial price", "current price", "margin percent"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
        print("Portfolio data file created")

    if not os.path.exists("transactions.csv"):
        with open("transactions.csv", 'w', newline='') as csvfile:
            fieldnames = ["symbol", "amount", "date purchased", "price", "total", "type", "actual date", "margin percent"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
        print("Transaction history file created")

    

    #Set up ini file
    if not os.path.exists("properties.ini"):
        config = configparser.ConfigParser()
        print("Setting up ini file:\n")
        config["Properties"] = {}
        
        
        tbill_Str = ask_YN_question("Convert cash to t-bills? (y/n) ")
        config["Properties"]["Convert_T-Bills"] = tbill_Str
        
        margin_per = ""
        while not (margin_per := margin_per.lower().replace("%","").strip()).isnumeric():
            margin_per = input("What is the maximum margin in percent? ")
        config["Properties"]["Max_Margin"] = margin_per

        startingCash = ""
        while not (startingCash := startingCash.strip()).isnumeric():
            startingCash = input("What is your starting cash? ")
        config["Properties"]["Starting_Cash"] = startingCash

        cashDate = ""
        print("\nPlease enter the date of the starting cash in YYYY-MM-DD format or cur/current for the current date.")
        while cashDate := cashDate.lower().strip() not in ("cur","current") and not is_valid_date(cashDate.strip()):
            cashDate = input("What is the date of the starting cash? ")
        if cashDate in ("cur","current"):
            config["Properties"]["Start_Date"] = get_current_date()
        else:
            config["Properties"]["Start_Date"] = cashDate
        
    
        config["Transaction"] = {}
        print("\nPlease enter the default transaction cost in basis points. You will also be asked if you want the transaction cost to be prompted for each transaction.")
        basisPoints = ""
        while not (basisPoints := basisPoints.strip()).isnumeric():
            basisPoints = input("How many basis points are the default cost of each transaction? ")
        
        config["Transaction"]["Default_Cost"] = basisPoints
        promptTransaction = ask_YN_question("Do you want to be prompted for each transaction? (y/n) ")
        config["Transaction"]["Prompted"] = promptTransaction


        with open('properties.ini', 'w') as configfile:
            config.write(configfile)
        
        print("Ini file created")