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
print('Your balance after deposit is ',deposit_funds(balance, deposit_amount))
print('Your balance after transfer is ',transfer_funds(balance, transfer_amount))
print('Your balance after withdrawal is ',withdraw_funds(balance, withdraw_amount))





