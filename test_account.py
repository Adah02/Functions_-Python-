#import unittest
from unittest import TestCase
import account

class TestAccount(TestCase):

  def test_set_new_account_name(self):
    new_name = "James Tauri"
    check = account.set_account_name(new_name)
    expected = "James Tauri"
    self.assertEqual(check, expected)

  def test_set_new_account_number(self):
    check = account.set_account_number(2553627162)
    expected = 2553627162;
    self.assertEqual(check, expected)

  def test_make_deposit_to_account(self):
    check = account.deposit_funds(200, 500)
    expected = 700;
    self.assertEqual(check, expected)

  def test_make_transfer_from_account(self):
    check = account.transfer_funds(700, 500)
    expected = 200;
    self.assertEqual(check, expected)

  def test_make_withdraw_from_account(self):
    check = account.withdraw_funds(1000, 600)
    expected = 400;
    self.assertEqual(check, expected)

  def test_bank_account_search(self):
    accounts = [['Justin Odu', 8147736633, '08147736633'],['Jihadeen Olu', 8147936738, '08147936738']];
    search = 8147736633
    check = account.search_for_account(accounts, search)
    expected = accounts[0];
    self.assertEqual(check, expected);





