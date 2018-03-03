from datetime import datetime

from django.test import TestCase
from expenses.models import Expense
from savemymo.utils import pretty_date


class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')

        self.assertTemplateUsed(response, 'home.html')


class NewExpenseTest(TestCase):

    def test_add_new_expense_and_check_if_appear_in_latest_expenses_list(self):
        self.client.post('/expenses/new', data={'amount': 10,
                                                'short_description': 'Luz',
                                                })
        new_expense = Expense.objects.first()
        register_date = datetime.utcnow()  # Just set for tests propose because the model save now as default

        self.assertEqual(Expense.objects.count(), 1)
        self.assertEqual(new_expense.amount, 10)
        self.assertEqual(new_expense.short_description, 'Luz')
        self.assertEqual(new_expense.register_date.day, register_date.day)
        self.assertEqual(new_expense.register_date.hour, register_date.hour)
        self.assertEqual(new_expense.register_date.minute, register_date.minute)
        self.assertEqual(pretty_date(new_expense.register_date), pretty_date(register_date))

