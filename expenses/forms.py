from django import forms
from .models import Expense

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['date', 'category', 'amount', 'description', 'payment_mode', 'merchant_name', 'location', 'notes', 'created_by']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 3}),
            'notes': forms.Textarea(attrs={'rows': 2}),
            'amount': forms.NumberInput(attrs={'step': '0.01'}),
            'payment_mode': forms.Select(choices=[
                ('Cash', 'Cash'),
                ('Card', 'Card'),
                ('UPI', 'UPI'),
                ('Other', 'Other'),
            ]),
        }
