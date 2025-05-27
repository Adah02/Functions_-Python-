import to_do_list_manager;
from unittest import TestCase;

class test_for_to_do_list_manager(TestCase):

  def test_add_a_task(self):
    list = ['buy books']
    add = 'buy phone'
    check = to_do_list_manager.add_a_task(list, add)
    expected = ['buy books', 'buy phone']
    self.assertEqual(check, expected)

  def view_task(self):
    list = ['buy books', 'buy phone', ]
    search = 'buy phone';
    check = to_do_list_manager.view_task(list, search)
    expected = ['buy books', 'buy phone']
    self.assertEqual(check, expected)