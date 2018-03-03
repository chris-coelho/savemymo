from django.shortcuts import render, redirect
from expenses.models import Expense


def home_page(request):
    latest_expenses = Expense.get_latest_expenses()
    return render(request, 'home.html', {'latest_expenses': latest_expenses})


def new_expense(request):
    Expense.objects.create(amount=request.POST['amount'],
                           short_description=request.POST['short_description'])
    return redirect('/')
