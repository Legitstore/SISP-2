from django import forms
from .models import Product, Order


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