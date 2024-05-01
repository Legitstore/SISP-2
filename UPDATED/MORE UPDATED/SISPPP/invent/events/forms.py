from django import forms
from .models import Product, Order
from django.contrib.auth.forms import  PasswordChangeForm

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [ 'name', 'unityprice', 'quantity']


        widgets = {
            
            'name': forms.Select(attrs={'class': 'form-select'}),
            'unityprice': forms.Select(attrs={'class': 'form-select'}),
            # 'quantity': forms.IntegerField(attrs={'class': 'form-control'}),

        }

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        
        self.fields['name'].widget.attrs['class'] = 'form-select'
        self.fields['unityprice'].widget.attrs['class'] = 'form-select'
        self.fields['quantity'].widget.attrs['class'] = 'form-control'

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product', 'price', 'sellingprice', 'order_quantity']


    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)

        self.fields['product'].widget.attrs['class'] = 'form-select'
        self.fields['price'].widget.attrs['class'] = 'form-select'
        self.fields['sellingprice'].widget.attrs['class'] = 'form-control'
        self.fields['order_quantity'].widget.attrs['class'] = 'form-control'


class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Old Password', widget=forms.PasswordInput(attrs={'autofocus':'True', 'autocomplete':'current-password', 'class':'form-control'}))

    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(attrs={'autofocus':'True', 'autocomplete':'current-password', 'class':'form-control'}))

    new_password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'autofocus':'True', 'autocomplete':'current-password', 'class':'form-control'}))