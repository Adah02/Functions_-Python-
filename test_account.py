#import unittest
from unittest import TestCase
import account

class TestAccount(TestCase):

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