def set_account_name(set_name):
  account_name = set_name
  return account_name

def set_account_number(set_acc_number):
  set_number = str(set_acc_number)
  if set_number.isdigit():
    number_length = len(set_number)
    if number_length == 10: 
      account_number = set_acc_number
      return account_number
    else:
      return "invalid"
  else:
    return "invalid"

  
def deposit_funds(balance, deposit_amount):
  if deposit_amount > 0:
    balance += deposit_amount
  return balance

def transfer_funds(balance, transfer_amount):
  if transfer_amount > 0 and transfer_amount <= balance:
    balance -= transfer_amount
  return balance

def withdraw_funds(balance, withdraw_amount):
  if withdraw_amount <= balance and withdraw_amount > 0:
    balance -= withdraw_amount
  return balance


balance = 5000;
deposit_amount = 500;
transfer_amount = 1500
withdraw_amount = 2400
set_name  = "Emma Adah"
set_acc_number = 8160509785
print('Your account name is',set_account_name(set_name))
print('Your account number is',set_account_number(set_acc_number))
print('Your balance after deposit is',deposit_funds(balance, deposit_amount))
print('Your balance after transfer is',transfer_funds(balance, transfer_amount))
print('Your balance after withdrawal is',withdraw_funds(balance, withdraw_amount))





