#!/usr/bin/env python3
import pickle

account_details = {"balance": 0.00, "loans": 0.00}

def main():
    print("Welcome to Next Financial Banking.")
    print("Current banking status:")
    getDetails()
    
    while True:
        command = input()
        processCommand(command)
    
def getDetails():
    try:
        file = open("bank_status.pickle", "rb")
    except FileNotFoundError:
        file = open("bank_status.pickle", "wb")
        pickle.dump(account_details, file)
        file.close()
        getDetails()
        
    new_dets = pickle.load(file)
    file.close()

    balance = new_dets["balance"]
    loans = new_dets["loans"]
    
    account_details["balance"] = float(balance)
    account_details["loans"] = float(loans)
    
    balance = account_details["balance"]
    loans = account_details["loans"]
    
    print("\tTotal balance: {} \tTotal bank loans: {}".format(balance, loans))
    
def processCommand(command):
    if command.lower() == "help":
        showCommands()
    elif command.lower() == "deposit":
        amount = input("Amount to deposit: ")
        deposit(amount)
    elif command.lower() == "withdraw":
        amount = input("Amount to withdraw: ")
        withdraw(amount)
    elif command.lower() == "quit":
        print("Thank you for choosing Next Financial. Goodbye")
        SystemExit()
    else:
        print(command + " is not a command.")
        
def showCommands():
    print("Commands: deposit, withdraw, quit")
    
def save():
    file = open("bank_status.pickle", "wb")
    
    account_details["balance"] = truncate(float(account_details["balance"]), 2)
    account_details["loans"] = truncate(float(account_details["loans"]), 2)
    
    pickle.dump(account_details, file)
    file.close()
    
    print("Process complete!")
    
    getDetails()
    
def deposit(amount):
    try:
        amount = float(amount)
    except:
        print("Error. Your deposits must be floats.")
        return
    
    if account_details["loans"] > 0:
        if amount >= account_details["loans"]:
            amount -= account_details["loans"]
            account_details["loans"] = 0
            account_details["balance"] += amount
        else:
            account_details["loans"] -= amount
    else:
        account_details["balance"] += amount
        
    save()
        

def withdraw(amount):
    try:
        amount = float(amount)
    except:
        print("Error. Your withdraws must be floats.")
        return
    
    if (amount > account_details["balance"]):
        loan(amount - account_details["balance"])
    else:
        account_details["balance"] -= float(amount)
        
    save()

def loan(amount):
    account_details["balance"] = 0.00
    account_details["loans"] += amount
    
    save()
    
def truncate(f, n):
    s = "{}".format(f)
    if "e" in s or "E" in s:
        return "{0:.{1}f}".format(f, n)
    i, p, d = s.partition(".")
    return ".".join([i, (d+"0"*n)[:n]])
    
main()