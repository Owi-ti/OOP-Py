class Account:
    
    def __init__(self,name,number) :
          self.name=name
          self.number=number
          self.deposits=[]
          self.withdrawals=[]
          self.balance=0
          self.transaction_charge=100

    def deposit(self,amount):
     if amount <= 0:
         return f"Deposit amount must be greater than zero"
     else:    
         self.balance+=amount 
         self.deposits.append(amount)

         print(self.deposits)
         return f"hello {self.name} you have desposited Ksh{amount} your new balance is Ksh{self.balance}" 
    
           
    def withdraw(self,amount):
        transaction_charge=100
        if amount > self.balance: 
             return  f"Insufficient amount" 
        elif amount<=0:
             return  f"Amount must be greater than zero"
        else:
           self.balance-=amount
           self.balance-=transaction_charge
           self.withdrawals.append(amount)
           print(self.withdrawals)
           return f"hello {self.name} you have withdrawn Ksh{amount} your new balance is Ksh{self.balance}"        
    
    def deposits_statement(self):
        for amount in self.deposits:
           print (f"Hello, You have  deposited Ksh {amount}" )

    def withdrawals_statement(self):
       for amount in self.withdrawals:
           print (f"Hello, You have  withdrawn Ksh {amount}" )
    
    def  get_balance(self):
        return f"your current balance is {self.balance}"

