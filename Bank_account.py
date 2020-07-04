# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 17:46:17 2019

@author: petru
"""
class BankAccount(object):
  balance = 0 
  def __init__(self, name):
    self.name = name 
  
  def __repr__(self):# method to make sure that whatever name user types will be attributed to the object 
    return "%s's account. Balance: $%.2f" %(self.name, self.balance)# this code line states who's account beongs to.

  def show_balance(self):# method used to print just the balance 
    print("Balance: $%.2f" % self.balance)
  
  def deposit(self, amount):#method used for deposit the cash
    if amount <= 0:# condition by checking the deposit greater then 0 value 
      print("The amount %s is not considered" % amount)
    else:
      print("The deposited added is: $%s" % amount)
      self.balance += amount 
      self.show_balance()
    
  def withdraw(self, amount):
    if amount > self.balance:
      print("The amount $%s exceeds cash deposit " % amount)
      return 
    else:
      print("Withdrawing $%2.2f " % amount)
      self.balance -= amount
      self.show_balance()

my_account = BankAccount("Petru Apachitei")#create the object and pass an instance
print(my_account)
my_account.show_balance()
my_account.deposit(34987)
my_account.withdraw(2300)
print(my_account) 
    
