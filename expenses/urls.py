from django.urls import path
from . import views

# Created the urls for Expenses by Gayathri S on 07/01/2026
urlpatterns = [
    path('', views.ExpenseInsertUpdateView, name='ExpenseInsertUpdateView'),
    path('DeleteExpenseView/', views.DeleteExpenseView, name='DeleteExpenseView'),
    path('ExpenseExcelDownload/', views.ExpenseExcelDownload, name='ExpenseExcelDownload'),
]
