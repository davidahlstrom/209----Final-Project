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



from tkinter import *
from david_ahlstrom_CLASS import Saving, Checking, Account, Bank
from david_ahlstrom_UTILITY import create_account_no

#Builds frame
class MyFrame(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.bank = Bank()
        self.welcome()

    #clears the previous frame
    def clear_frame(self):
        for widget in self.winfo_children():
            widget.destroy()

    #Exits the application
    def exit_application(self):
        root.destroy()

    #Logs the user out
    def logout(self):
        del self.account
        self.welcome()

    #Displays welcome and provides buttons for new user, existing user, exiting the application     
    def welcome(self):
        self.clear_frame()
        
        welcome_label = Label(self, text = 'Welcome to 209 Banking!')
        welcome_label.grid(row=0,column=0)

        self.existing_user_btn = Button(self, text = 'Existing User', command = self.existing_account_widget)
        self.existing_user_btn.grid(row=1,column=0)

        self.new_user_btn = Button(self, text = 'New User', command = self.new_account_widget)
        self.new_user_btn.grid(row=2,column=0)

        self.exit_btn = Button(self, text = 'Exit Application', command = self.exit_application)
        self.exit_btn.grid(row=3,column=0)

    #Contains labels and entries for user information for a new account   
    def new_account_widget(self):
        
        self.clear_frame()

        #Asks for name, address, account type, username, and pin
        label_fname = Label(self, text = "First name: ")
        self.entry_fname = Entry(self, width=15)

        label_lname = Label(self, text = "Last name: ")
        self.entry_lname = Entry(self, width=15)

        label_address_line1 = Label(self, text = "Address Line 1: ")
        self.entry_address_line1 = Entry(self, width=15)

        label_address_line2 = Label(self, text = "Address Line 2: ")
        self.entry_address_line2 = Entry(self, width=15)

        label_account_type = Label(self, text = "Account Type: ")
        self.entry_account_type = Entry(self, width=15)

        label_username = Label(self, text = "Username: ")
        self.entry_username = Entry(self, width=15)

        label_pin = Label(self, text = "Pin: ")
        self.entry_pin = Entry(self, width=15)

        #Layout
        label_fname.grid(row=0,column=0)
        self.entry_fname.grid(row=0,column=1)

        label_lname.grid(row=1,column=0)
        self.entry_lname.grid(row=1,column=1)

        label_address_line1.grid(row=2,column=0)
        self.entry_address_line1.grid(row=2,column=1)

        label_address_line2.grid(row=3,column=0)
        self.entry_address_line2.grid(row=3,column=1)

        label_account_type.grid(row=4,column=0)
        self.entry_account_type.grid(row=4,column=1)

        label_username.grid(row=5,column=0)
        self.entry_username.grid(row=5,column=1)

        label_pin.grid(row=6,column=0)
        self.entry_pin.grid(row=6,column=1)

        #Buttons for creating account and accessing the main menu
        create_account_btn = Button(self, text = 'Create Account', command = self.create_account_button_click)
        create_account_btn.grid(row=7,column=0)

        main_menu_btn = Button(self, text = 'Main Menu', command = self.welcome)
        main_menu_btn.grid(row=7,column=1)
         

    #Create account object
    def create_account_button_click(self):

        #Gets the new account information
        cfname = self.entry_fname.get()
        clname = self.entry_lname.get()
        caddress_line1 = self.entry_address_line1.get()
        caddress_line2 = self.entry_address_line2.get()
        caccount_type = self.entry_account_type.get()
        cusername = self.entry_username.get()
        cpin = self.entry_pin.get()

        self.clear_frame()

        #Provides user with unique account number
        label_accountno = Label(self, text = "Your account no: ")
        self.accountno  = StringVar(self, '') #create StringVar object
        label_final_accountno  = Label(self, \
                                       textvariable=self.accountno) #associate self.result with this label


        s = create_account_no()

        #setting the self.result label
        self.accountno.set(s)

        #creating saving object
        if caccount_type.lower() == 'saving': 
            account = Saving(accountno = s, acctype = caccount_type, fname = cfname, lname = clname, line1 = caddress_line1, line2 = caddress_line2, username = cusername, pin = cpin)

        #create checking object
        elif caccount_type.lower() == 'checking':
            account = Checking(accountno = s, acctype = caccount_type, fname = cfname, lname = clname, line1 = caddress_line1, line2 = caddress_line2, username = cusername, pin = cpin)

        #for printing purpose, not for user
        self.bank.display()

        #Displays text to login again, provides access to existing account widget
        self.button_next  = Button(self, text = "Please Login Again", command=self.existing_account_widget)
        label_accountno.grid(column=0, columnspan = 2)
        label_final_accountno.grid(column=0, columnspan = 2)
        self.button_next.grid(column = 0, columnspan = 2 )
 

    #Widget for existing accounts
    def existing_account_widget(self):

        self.clear_frame()

        #Asks for username and pin
        label_exist_username = Label(self, text = "Username: ")
        self.entry_exist_username = Entry(self, width=15)

        label_exist_pin = Label(self, text = "Pin: ")
        self.entry_exist_pin = Entry(self, width=15)
        
        #Layout
        label_exist_username.grid(row=0,column=0)
        self.entry_exist_username.grid(row=0,column=1)

        label_exist_pin.grid(row=1,column=0)
        self.entry_exist_pin.grid(row=1,column=1)

        #Buttons for login and main menu
        login_btn = Button(self, text = 'Login', command = self.login_button_click)
        login_btn.grid(row=2,column=1)

        main_menu_btn = Button(self, text = 'Main Menu', command = self.welcome)
        main_menu_btn.grid(row=3,column=1)
        

    def login_button_click(self):

        #get username
        username = self.entry_exist_username.get()

        #get pin
        pin = self.entry_exist_pin.get()
        
        #check if usernmae and pin is valid using login_validity method
        if (self.bank.login_validity(username, pin)):

            #call load_account and returns account object
            self.account = self.bank.load_account(username, pin)
            
            #call self.existing_user_options()
            self.existing_user_options()

        #if invalid ask again
        else:
            self.existing_account_widget()
            
    #Provides interface with buttons for various options for existing users
    def existing_user_options(self):
        self.clear_frame()
        
        self.deposit_button = Button(self, text = "Deposit", \
                                      command=self.deposit_interface)
        self.deposit_button.grid()

        self.withdraw_button = Button(self, text = "Withdraw", \
                                      command=self.withdraw_interface)
        self.withdraw_button.grid()

        self.summary_button = Button(self, text = "Account Summary", \
                                      command=self.summary_interface)
        self.summary_button.grid()

        self.logout_button = Button(self, text = "Logout", \
                                      command=self.logout)
        self.logout_button.grid()

        self.exit_button  = Button(self, text = "Exit Application", \
                                      command=self.exit_application)
        self.exit_button.grid()

    #asks for user account number, sends to summary function
    def summary_interface(self):
        
        self.clear_frame()

        #Asks for account number
        label_account_number = Label(self, text = "Account Number: ")
        self.entry_account_number = Entry(self, width=15)

        label_account_number.grid(row=0,column=0)
        self.entry_account_number.grid(row=0,column=1)

        #Buttons for user options and next, which sends to summary
        options_btn = Button(self, text = 'Options', command = self.existing_user_options)
        options_btn.grid(row=7,column=0)

        next_btn = Button(self, text = 'Next', command = self.summary)
        next_btn.grid(row=7,column=1)
        
    #Provides information regarding the user account determined by their account number
    def summary(self):

        #Obtains account no from user
        accno = self.entry_account_number.get()
        name, address, acctype, balance = self.account.summary(accno)
        
        self.clear_frame()
        info_label = Label(self, text = "Account Information")

        #Display user information
        name_label = Label(self, text = name)
        address_label = Label(self, text = address)
        acctype_label = Label(self, text = acctype)
        balance_label = Label(self, text = balance)

        info_label.pack()
        name_label.pack()
        address_label.pack()
        acctype_label.pack()
        balance_label.pack()
        
        self.button_options  = Button(self, text = "Options", \
                                            command=self.existing_user_options)
        self.button_options.pack()

    #Allows user to enter deposit amount
    def deposit_interface(self):
        
        self.clear_frame()

        #Asks for deposit amount
        label_deposit = Label(self, text = "Amount to deposit: ")
        self.entry_deposit = Entry(self, width=15)

        #Asks for account number
        label_accno = Label(self, text = "Account Number: ")
        self.entry_accno = Entry(self, width=15)

        label_deposit.grid(row=0,column=0)
        self.entry_deposit.grid(row=0,column=1)

        label_accno.grid(row=1,column=0)
        self.entry_accno.grid(row=1,column=1)

        #Buttons for options and next, which sends to deposit
        options_btn = Button(self, text = 'Options', command = self.existing_user_options)
        options_btn.grid(row=7,column=0)

        next_btn = Button(self, text = 'Next', command = self.deposit)
        next_btn.grid(row=7,column=1)

    #Deposits amount determined by deposit_interface
    def deposit(self):

        #Get deposit amount and account number
        amount_to_deposit = self.entry_deposit.get()
        accno_to_deposit = self.entry_accno.get()

        #Calls deposit and deposits user entry
        self.account.deposit(amount_to_deposit, accno_to_deposit)
        self.check_balance(accno_to_deposit)

    #Allows user to enter withdraw amount
    def withdraw_interface(self):
        
        self.clear_frame()

        #Asks for withdraw amount
        label_withdraw = Label(self, text = "Amount to withdraw: ")
        self.entry_withdraw = Entry(self, width=15)

        #Asks for account number
        label_accno = Label(self, text = "Account Number: ")
        self.entry_accno = Entry(self, width=15)

        label_withdraw.grid(row=0,column=0)
        self.entry_withdraw.grid(row=0,column=1)

        label_accno.grid(row=1,column=0)
        self.entry_accno.grid(row=1,column=1)

        #Buttons for options and next, which sends to withdraw
        options_btn = Button(self, text = 'Options', command = self.existing_user_options)
        options_btn.grid(row=7,column=0)

        next_btn = Button(self, text = 'Next', command = self.withdraw)
        next_btn.grid(row=7,column=1)

    #Withdraws amount determined by withdraw_interface
    def withdraw(self):

        #Get withdraw amount and account number
        amount_to_withdraw = self.entry_withdraw.get()
        accno_to_withdraw = self.entry_accno.get()

        #Calls withdraw and withdraws user entry
        self.account.withdraw(amount_to_withdraw, accno_to_withdraw)
        self.check_balance(accno_to_withdraw)


    #Checks the balance of the user account
    def check_balance(self, accno):

        self.clear_frame()

        #Calls get_balance and displays current balance
        label_balance = Label(self, text = 'Current balance: ' + \
                              str(self.account.get_balance(accno)))
        label_balance.grid()

        #Options button to return to existing_user_options menu
        self.options_button  = Button(self, text = "Options", \
                                            command=self.existing_user_options)
        self.options_button.grid()


             
#driver
root = Tk()
frame = MyFrame(root)
frame.pack()
root.mainloop()
