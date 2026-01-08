from django.shortcuts import render, redirect, get_object_or_404
from .models import Expense
from .forms import *
from django.http import JsonResponse, HttpResponse
from django.db.models import Sum
import openpyxl

# Created the view for Expenses Insert and Update by Gayathri S on 08/01/2026
def ExpenseInsertUpdateView(request):
    expense = None
    if request.method == 'POST':
        expense_id = request.POST.get('expense_id')
        if expense_id:
            expense = get_object_or_404(Expense, expense_id=expense_id)
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('ExpenseInsertUpdateView')
    else:
        expense_id = request.GET.get('expense_id')
        if expense_id:
            expense = get_object_or_404(Expense, expense_id=expense_id)
        form = ExpenseForm(instance=expense)
    expenses = Expense.objects.all()
    category_summary = (Expense.objects.values('category').annotate(total_amount=Sum('amount')).order_by('category'))
    return render(request, 'expense_form.html', {'form': form, 'expense': expense, 'expenses': expenses, 'category_summary': category_summary, 'expense_id': expense_id})


# Created the view for Delete Expenses by Gayathri S on 08/01/2026
def DeleteExpenseView(request):
    if request.method == 'POST':
        expense_id = request.POST.get('expense_id')
        expense = Expense.objects.get(expense_id=expense_id).delete()
        return JsonResponse({'status': 'success'})
    

# Created the view for Download Excel Expenses by Gayathri S on 08/01/2026
def ExpenseExcelDownload(request):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Expenses"
    headers = ['Date', 'Category', 'Amount', 'Payment Mode', 'Merchant', 'Location', 'Description', 'Created By', 'Notes']
    ws.append(headers)

    expenses = Expense.objects.all()
    for exp in expenses:
        ws.append([
            exp.date.strftime('%d-%m-%Y') if exp.date else '', exp.category, float(exp.amount) if exp.amount else 0, exp.payment_mode, exp.merchant_name, exp.location, exp.description, exp.created_by, exp.notes])

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=Expenses.xlsx'
    wb.save(response)
    return response