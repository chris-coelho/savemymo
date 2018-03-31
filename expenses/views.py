from django.shortcuts import render, redirect

from .forms import ExpenseHomeForm
from .models import Expense


def home_page(request):
    form = ExpenseHomeForm()
    latest_expenses = Expense.get_latest_expenses()
    return render(request, 'home.html', {'form': form,
                                         'latest_expenses': latest_expenses})


def new_expense(request):
    form = ExpenseHomeForm(data=request.POST)
    latest_expenses = Expense.get_latest_expenses()

    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request, 'home.html', {'form': form,
                                         'latest_expenses': latest_expenses})
