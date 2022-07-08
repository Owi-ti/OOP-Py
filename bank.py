from datetime import datetime

class Account:
    
    def __init__(self,name,number) :
          self.name=name
          self.number=number
          self.deposits=[]
          self.withdrawals=[]
          self.balance=0
          self.transaction_charge=100
          self.all_statement=[]
          self.loan_balance=0


    def deposit(self,amount):
     self.date=datetime.now().strftime("%c")
     empty_dict={"Date":self.date,"amount":amount,"narration":"deposit"}
     if amount <= 0:
         return f"Deposit amount must be greater than zero"
     else:    
         self.balance+=amount 
         self.deposits.append(amount)

         self.all_statement.append(empty_dict)
         print(empty_dict)
        
           
   
    def withdraw(self,amount):
        self.date=datetime.now().strftime("%c")
        empty_dict={"Date":self.date,"amount":amount,"narration":"withdrawal"}
        transaction_charge=100
        if amount + self.transaction_charge > self.balance: 
             return  f"Insufficient amount" 
        elif amount<=0:
             return  f"Amount must be greater than zero"
        else:
           self.balance-=amount
           self.balance-=transaction_charge
           self.withdrawals.append(amount)
           print(empty_dict)
        
    
    def deposits_statement(self):
        for amount in self.deposits:
           print (f"Dear Esther, You have deposited Ksh.{amount}" )


    def withdrawals_statement(self):
       for amount in self.withdrawals:
           print (f"Dear Esther, You have withdrawn Ksh.{amount}" )
    
    
    def  get_balance(self):
        return f"Dear Esther,your current balance is Ksh.{self.balance}"


    def full_statement(self):
        for n in self.all_statement: 
            time= n["Date"]
            narration= n["narration"]
            amount= n["amount"] 
            print(f"{time}.........{narration}........{amount}")
            # statement =self.deposite + self.withdrawals
            # fro statement in statement:
            # statement.sort(key=labda:statement:statement['date'],reverse=True)
            # date= statement['date'].strftime(%d:%m:%y)
            # narration=statement['narration']
            # amount-statement['amount']
            #  print(f"{time}.........{narration}........{amount}")


    def borrow(self,amount):
        number_deposit= len(self.deposits)
        sum_deposit= sum(self.deposits)
        total=1/3*sum_deposit
        amount+=(amount)*0.03
        if number_deposit <10:
            print(f"You should make alteast 10 deposits")

        elif amount<=100:
            print(f"Loan borrowed must be more than 100")

        elif amount>=total:
            print(f"You are not qualified for loan higher than{self.deposits//3}")
            # total=(sum[deposit[amoun] for deposit in self.deposit])     
            # amount>total*1/3:
            # return "amount must be lass than {total*1/3}"

        elif self.loan_balance > 0:
            print(f"Failed,You hava an outstanding balance loan of{self.loan_balance}")    

        else:
             self.loan_balance+=amount
             return f"Your loan balance is {self.loan_balance}"

             
    def loan_repayment(self,amount):
        if amount< self.loan_balance:
             self.loan_balance-=amount
             return f"You have paid {amount}, your outstanding loan balance is {self.loan_balance}"
        elif amount==self.loan_balance:
            return f"You have  successfully setttled your loan balance"
        else:
            overpayment= amount-self.loan_balance
            self.balance+=overpayment
            return f"You loan is successfully settled, your current amount is  {self.balance}"


    def transfer(self,amount,account):
        if amount > self.balance:
            return f"You balance is insufficient"
        elif amount <=0:
            return f"Enter correct amount"
        elif isinstance(account,Account):
            self.balance-=amount
            account.deposit(amount)
            return f"You have successfully sent {amount}, your current balance is {self.balance}"
            # elif insatnce(Account,account)




