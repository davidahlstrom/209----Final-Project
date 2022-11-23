# -------------------------------------------------------------------------------
# Final Project: Banking Application
# Name: David Ahlstrom
# Python Version:  3.7.8
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
#                       violates the ethical guidelines as set forth by the
#                       instructor and the class syllabus.
#-------------------------------------------------------------------------------
# References: Slides and example code in weekly content
#-------------------------------------------------------------------------------
# Comments to grader: N/A
#-------------------------------------------------------------------------------
# Code:
#-------------------------------------------------------------------------------


class Bank(object):

    #holds all the accounts
    accountList=[]

    #for printing purposes only, not for user
    def display(self):
        ''' displays all the account in the accountList - not for user'''
        for account in Bank.accountList:
            print ("*********************")
            for k,v in account.options.items():
                print ('{}: {}'.format(k,v))
            print ("*********************")

    #checks for the correct login
    def login_validity(self, username, pin):
        ''' checks login validity using the given username and pin
        GUI file calls this method'''
        for account in Bank.accountList:
            if username == account['username'] and pin == account['pin']:
                return True
        return False

    #loads current account
    def load_account(self,username, pin):
        ''' loads an account if given username and pin matches
        call from GUI files'''
        for account in Bank.accountList:
            if username == account['username'] and pin == account['pin']:

                #returns account object
                return account

        #no object found   
        return None 
    
    
        
class Account(object):
    default_options = {'accountno':None,'acctype': None, \
               'balance': 0, 'fname': None, 'lname': None, 'line1':None, \
                       'line2': None, 'username': None, 'pin': None}
    def __init__(self, **kwargs):
        self.options = Account.default_options.copy() #current object is self.options

        #update self.options with kwargs
        self.options.update(kwargs)

        #append self to accountList
        Bank.accountList.append(self)

    #get an item by key
    def __getitem__(self, key):
        return self.options[key]

    #set an item by key
    def __setitem__(self, key, new_value):
        self.options[key] = new_value

    #returns balance
    def get_balance(self, accno):
        if accno == self['accountno'] :
            return self['balance']

    #deposits amount_to_deposit to current user
    def deposit(self, amount_to_deposit, accno):
        if accno == self['accountno']:
            self['balance'] = self['balance'] + float(amount_to_deposit)
            return self['balance']

    #returns full name, address, account type and current balance
    def summary(self, accno):
        if accno == self['accountno']:
            name = self['fname'] + ' ' + self['lname']
            address = self['line1'] + ' ' + self['line2']
            return (name,address,self['acctype'],self['balance'])



       
class Saving(Account):
    #flat rate to subtract from saving account
    withdraw_charge = 2.53 

    #withdraws amount_to_withdraw from current user, as well as withdraw_charge
    def withdraw(self, amount_to_withdraw, accno):
        if accno == self['accountno']:
            self['balance'] = self['balance'] - float(amount_to_withdraw) - self.withdraw_charge
            return self['balance']

class Checking(Account):
    #flat rate to subtract from checking account
    withdraw_charge = 1.00

    #withdraws amount_to_withdraw from current user, as well as withdraw_charge
    def withdraw(self, amount_to_withdraw, accno):
        if accno == self['accountno']:
            self['balance'] = self['balance'] - float(amount_to_withdraw) - self.withdraw_charge
            return self['balance']

