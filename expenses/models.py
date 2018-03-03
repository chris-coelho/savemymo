import uuid
from django.db import models
from django.utils import timezone

from savemymo.utils import pretty_date


class Expense(models.Model):
    id = models.CharField(max_length=32,
                          default=uuid.uuid4().hex,
                          null=False,
                          primary_key=True)
    amount = models.DecimalField(max_digits=12,
                                 decimal_places=2,
                                 null=False)
    short_description = models.CharField(max_length=255,
                                         null=False)
    register_date = models.DateTimeField(default=timezone.now,
                                         null=False)

    @staticmethod
    def get_latest_expenses():
        expenses = Expense.objects.all()
        latest_expenses = []
        for expense in expenses:
            expense.pretty_date = pretty_date(expense.register_date)
            latest_expenses.append(expense)
        return latest_expenses
