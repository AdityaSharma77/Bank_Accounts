#Importing datetime and random libraries to be used for issuing Card Number and and its expiry date. 
import datetime
import random

"""
Basic Account allows user to deposit, withdraw, get to know balance left in their account and close the account. 
Basic Account holders can also be issued card associated to their account.  
"""
#Defining Basic Account and its respecitve variables and methods.
class BasicAccount():   
#Defining an inital value of 0 to account number so that it can be incremented with each account creation.
    acNum =0         
#Initializing variables name and starting balance while creating an account. We also increment the value of acNum.
    def __init__(self, acName, openingBalance):
        if openingBalance>0:
            self.name = acName
            self.balance = float(openingBalance)
            BasicAccount.acNum+=1
            self.acNum = BasicAccount.acNum
        else:
            print('Cannot open an accunt with a negative balance')

#string function to show that account has been created with certain opening balance as per the customer requirment.                       
    def __str__(self):
        return "Hi {self.name} your Basic Account with opening balance of {self.balance} has been opened".format(self=self)

#deposit funtion, to add balance to the account. The value from user is only considered if it is a postive integer. 
#It prints an error message if amount is negative. 
    def deposit(self, amount):
        if amount >0:
            self.amount = float(amount)
            self.balance += self.amount
            print("£",self.amount ,"has been deposited in your account. Your total balance is £",self.balance)
        else:
            print("Cannot deposit money in negative.")

#Creating a withdraw function and taking the amount to be withdrawn from the user. 
    def withdraw(self, amount):
        if amount >0:
            self.amount = float(amount)
            if self.amount > self.getAvailableBalance():
#getAvailableBalance funciton is different for Basic and Premium since Premium has overdraft limit as well.
#The withdraw functino would generate error message if amountrequested goes over balance or balance and overdraft limit.
                print("Can not withdraw £ ", self.amount)
            else:
                self.balance -=self.amount
                if self.balance<0:
                    print(self.name ,"has withdrawn £",self.amount, ".New Balance is -£",(-1*self.balance))
#Multiplying -1 with self.balance and -£ top have the putput in a specific format. For example -£250 and not £-250. 
                    overdraft = True
                else:
                    print(self.name ,"has withdrawn £",self.amount, ".New Balance is £",self.balance)
        else:
            print("Cannot withdraw negative amount")
            
#Returns balance left in the account. For basic account it is simply the balance after withdraw, if any.                 
    def getAvailableBalance(self):
        return self.balance

#Works the same way as getAvailableBalance for Basic Account sincee they dont have any overdraft .  
    def getBalance(self):
       return self.balance 

#Printing balance for the specifc account number   
    def printBalance(self):
        print("Current balance in",self.name,"account is £",self.balance)

#This funtion returns name of teh account holder
    def getName(self):
        return self.name

#getAcNum funciton returns account number as a string     
    def getAcNum(self):
        return (str(self.acNum))

#A method to issue new card to a customer. Utilizes both the libraries imported earlier.    
#Expiry of the card is 3 years since the day of issue. This is done using datetime library.    
    def issueNewCard(self):
        card = datetime.datetime.now()
#Using only the last 2 numbers of the year to be included in the tuple of cardExp. 
        cardYear = str(card.year)[-2:]
        self.cardExp = (card.month,int(cardYear)+3)
#Generating a random number of 16 digits for card with numbers ranging from 0 to 9.
        self.cardNum = ''.join([str(random.randint(0,9))for i in range (0,16)])
        print("New Card Issued. Your card with card number", self.cardNum,"will expire on ", self.cardExp)

#Defining Close Account Function. If there is any balance left while close account is requested it will withdraw and then close the account.
#If balance is zero, the account is closed with a print message.        
    def closeAccount(self):
        if self.balance>0:
            print("You have £", self.balance," left in your account. Withdarwing it before closing your account.")
            self.withdraw(self.balance)    
            print("Account closed.")
            return True
        elif self.balance==0:
            print("Closing your account. Thank you for banking with us.")
            return True

"""
Premium account holders are allowed to deposit, withdraw,get to know balance left in their account and close the account.
Additoinaly Premium Account holders are allowed to have an overdraft. The limit is defined for the same. 
The balance and closing of account takes into consideration any overdraft that is available.  
"""

#Defining Premium Account. It inherits all variables and methods from Basic Account except for OverrdraftLimit.
class PremiumAccount(BasicAccount):
#Initializing overdraft as False since currently no account is created. Depending on the balance it would change to True or not.
    overdraft = False

#Definfing the extra overdraft limit variable during initialization and inheriting the rest from Basic Account. 
    def __init__(self, acName, openingBalance,initialOverdraft):
        super().__init__(acName, openingBalance)
        self.overdraftlimit = initialOverdraft

#String method to show the account has been opened with certain opening balance and overdraft limit.               
    def __str__(self):
        return "Hi {self.name}, your Premium Account with an opening balance of £ {self.balance} and overdraft limit of £ {self.overdraftimit} has been opened."  

#setOverdraftLimit funtion to change the overdraft limit associated to any Premium account while initializing. 
    def setOverdraftLimit(self,newlimit):
        self.overdraftlimit = newlimit
        print("Your overdraft limit is £", self.overdraftlimit)

#This method gives available balance taking into account any overdraft that is available.
    def getAvailableBalance(self):
        return self.balance + self.overdraftlimit

#getBalance funtion only returns value of the balance and doesn't consider any overdraft.
    def getBalance(self):
        return self.balance

#printBalance funtion used to print balance. If the account has overdraft it shows how much of it is available.
# If the account is not overdrawn, it just prints value of self.balance.        
    def printBalance(self):
        if self.balance>0:
            print("Your balance is £",self.balance ,"and current avaialble overdraft is £",self.overdraftlimit+self.balance)
        elif self.balance<0:
#Multiplying -1 with self.balance and -£ to have the output in a specific format. For example -£250 and not £-250.
            print("Your have used all your balance and are on an overdraft of -£",(-1*self.balance) ,".Your remaining available overdraft is £",self.overdraftlimit+self.balance)

#If the account has been overdrawn close account method prints an error message stating the same and that account cannot be closed at the moment.
    def closeAccount(self):
        if self.balance <0:
#Multiplying -1 with self.balance and -£ to have the output in a specific format. For example -£250 and not £-250.
            print("You have an overdraft of -£",(-1*self.balance),"pending. Unable to close the account.")
            return False
        elif self.balance >0:
#If account is not overdrawn and balance is left, it just withdraws the amount and closes the account.
            print("You have overall balance of £",self.balance,"in your account. Withdrawing it before closing the account.")
            self.withdraw(self.balance)
            print("Account Closed.")
            return True

