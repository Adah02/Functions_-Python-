import to_do_list_manager;
from unittest import TestCase;

class test_for_to_do_list_manager(TestCase):

  def test_add_a_task(self):
    list = ['buy books']
    add = 'buy phone'
    check = to_do_list_manager.add_a_task(list, add)
    expected = ['buy books', 'buy phone']
    self.assertEqual(check, expected)

  def test_to_view_tasks_in_to_do_list_manager(self):
    search = ['buy books', 'buy phone', ]
    list = list;
    check = to_do_list_manager.view_tasks(list, search)
    expected = ['buy books', 'buy phone']
    self.assertEqual(check, expected)

  def test_to_mark_item_in_to_do_list_manager(self):
    list = ['buy books', 'fix phone', 'pay fees']
    delete = 'pay fees';
    check = to_do_list_manager.delete_a_task(delete, list)
    expected = ['buy books', 'fix phone']
    self.assertEqual(check, expected)