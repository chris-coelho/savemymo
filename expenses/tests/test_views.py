from datetime import datetime

from decimal import Decimal
from django.test import TestCase
from expenses.models import Expense
from savemymo.utils import pretty_date
from expenses import forms


class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')

        self.assertTemplateUsed(response, 'home.html')


class NewExpenseTest(TestCase):

    def test_amount_less_than_zero(self):
        response = self.client.post('/expenses/new', data={'amount': 0,
                                                           'short_description': 'Pharmacy',
                                                           })

        self.assertContains(response, forms.AMOUNT_LESS_THAN_ZERO)

    def test_POST_a_valid_expense(self):
        response = self.client.post('/expenses/new', data={'amount': 150.15,
                                                           'short_description': 'Mall',
                                                           })
        new_expense = Expense.objects.first()
        register_date = datetime.utcnow()  # Just set for tests propose because the model save now as default

        self.assertEqual(Expense.objects.count(), 1)
        self.assertEqual(new_expense.amount, Decimal('150.15'))
        self.assertEqual(new_expense.short_description, 'Mall')
        self.assertEqual(new_expense.register_date.day, register_date.day)
        self.assertEqual(new_expense.register_date.hour, register_date.hour)
        self.assertEqual(new_expense.register_date.minute, register_date.minute)
        self.assertEqual(pretty_date(new_expense.register_date), pretty_date(register_date))
        self.assertRedirects(response, '/')

    def test_if_appears_the_new_expense_in_latest_expenses_list(self):
        self.client.post('/expenses/new', data={'amount': 10.32,
                                                'short_description': 'Pharmacy',
                                                })
        response = self.client.get('/')

        self.assertContains(response, '10.32')
        self.assertContains(response, 'Pharmacy')
