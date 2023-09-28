
class Bankaccount:
  def __init__(self,acc_num,date_of_open,balance,customer_name):
    self.acc_num=acc_num
    self.date_of_open=date_of_open
    self.balance=balance
    self.customer_name=customer_name
  def deposit(self,amount):
    self. balance += amount
    print(f"${amount} has been deposited in your account ")
  def withdraw(self,amount):
    if amount > self.balance:
      print("insufficient balance ")
    else:
      self.balance -= amount
      print(f"${amount} has been withdraw from your account ")
  def check_balance(self):
      print(f"current balance is ${self.balance}.")
  def print_customer_details(self):
      print("Name=",self.customer_name)
      print("account number=",self. acc_num)
      print("date of opening=",self. date_of_open)
      print(f"balance: ${self.balance} \n")

acc_no1=Bankaccount(123455,"01.12.2005",1000,"Krishma ")
print("customer details")
acc_no1.print_customer_details()
print("=========================")
acc_no1.deposit(100)
acc_no1.check_balance()
acc_no1.withdraw(200)