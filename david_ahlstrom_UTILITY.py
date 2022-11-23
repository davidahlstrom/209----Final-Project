import random, string

def create_account_no():
    '''
    creates a rendom 4 digit alphanumeric account number for 
    '''
    
    number = ''.join(random.choices(string.ascii_letters.upper() + string.digits, k=4))
    return number

