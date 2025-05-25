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
  elif withdraw_amount > balance:
    higher_amount_withdraw_response = 'Withdrawal amount is greater than your balance';
    return higher_amount_withdraw_response;
  else:
    lower_amount_withdraw_response ='Withdrawal amount is lower than minimum' 
    return lower_amount_withdraw_response;

def search_for_account(accounts, search_item):
  for items in range(len(accounts)):
    for item in accounts[items]:
      if item == search_item:
        customers_account = accounts[items];
        return customers_account;
  else:
    response = 'No account with such detail';
    return response;
        
accounts = [["Emma Adah", 8160509785, '08160509785'],["Jason Uba", 9052969013, '09052969013'],["Dan Abah", 9157898543, '09157898543'],["Annie Uba", 7076564433, '07076564433'],["Annie Uba", 7076564433, '']];

search_item = 8160509785;

print(search_for_account(accounts, search_item))

set_name = "Emma Adah";
set_acc_number = 8160509785;
balance = 5000;
deposit_amount = 500;
transfer_amount = 1500;
withdraw_amount = 0;


print('Your account name is',set_account_name(set_name))
print('Your account number is',set_account_number(set_acc_number))
print('Your balance after deposit is',deposit_funds(balance, deposit_amount))
print('Your balance after transfer is',transfer_funds(balance, transfer_amount))
print('Withdrawal response: ',withdraw_funds(balance, withdraw_amount))



