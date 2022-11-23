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


import random, string

def create_account_no():
    '''
    creates a rendom 4 digit alphanumeric account number for 
    '''
    
    number = ''.join(random.choices(string.ascii_letters.upper() + string.digits, k=4))
    return number

