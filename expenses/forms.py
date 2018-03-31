from django import forms

from .models import Expense

AMOUNT_LESS_THAN_ZERO = "The amount must be greater than zero"


class ExpenseHomeForm(forms.ModelForm):
    amount = forms.DecimalField(max_digits=10, decimal_places=2)
    short_description = forms.CharField(min_length=3, max_length=150)

    def clean_amount(self):
        amount = self.cleaned_data['amount']
        if amount <= 0:
            raise forms.ValidationError(AMOUNT_LESS_THAN_ZERO)
        return amount

    class Meta:
        model = Expense
        fields = ('amount', 'short_description',)
        error_messages = {
            'amount': {
                'required': 'Amount is required',
            },
        }

