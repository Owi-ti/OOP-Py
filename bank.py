class Account:
    
    def __init__(self,balance) :
          self.balance= balance
          
    def deposit(self,amount):
        self.balance +=amount
        return self.balance
              
    def withdraw(self,amount):
        self.balance -=amount
        return self.balance
