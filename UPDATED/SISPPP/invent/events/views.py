from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Product, Order
from .forms import ProductForm, OrderForm
from django.contrib import messages
from user.forms import CustomerRegistrationForm

# Create your views here.

@login_required(login_url='login')
def index(request):
    orders = Order.objects.all()
    product = Product.objects.all()
    orders_count = orders.count()
    product_count = product.count()
    workers_count = User.objects.all().count()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff = request.user 
            instance.save()
            return redirect('index')
    else:
        form = OrderForm()
    context = {'orders': orders, 'form': form, 'product': product,
               'orders_count': orders_count,
               'product_count': product_count,
               'workers_count': workers_count,
            }
    return render(request, 'events/index.html', context)


@login_required(login_url='login')
def staff(request):
    if request.user.is_superuser == False:
        return redirect('index')
    else:
        workers = User.objects.all()
        workers_count = workers.count()
        product_count = Product.objects.all().count()
        orders_count = Order.objects.all().count()
        form = CustomerRegistrationForm()
        if request.method == 'POST':
            form = CustomerRegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' +  user )
                return redirect('staff')
            
        context = {'workers': workers, 'workers_count': workers_count, 
                'product_count': product_count,
                'orders_count': orders_count,
                'form': form,
                }
        return render(request, 'events/staff.html', context)




@login_required(login_url='login')
def product(request):
    if request.user.is_superuser == False:
        return redirect('index')
    else:
        items = Product.objects.all()
        workers_count = User.objects.all().count()
        product_count = items.count()
        orders_count = Order.objects.all().count()
    
        if request.method == 'POST':
            form = ProductForm(request.POST)
            if form.is_valid():
                form.save()
                product_name = form.cleaned_data.get('name')
                messages.success(request, f'{product_name} has been added')
                return redirect('product')
        else:
            form = ProductForm()
        context = {'items': items, 'form': form, 
                'workers_count': workers_count,
                'product_count': product_count,
                'orders_count': orders_count,
                }
        return render(request, 'events/product.html', context)


@login_required(login_url='login')
def order(request):
    if request.user.is_superuser == False:
        return redirect('index')
    else:
        orders = Order.objects.all()
        orders_count = orders.count()
        workers_count = User.objects.all().count()
        product_count = Product.objects.all().count()
        context = {'orders': orders, 'workers_count': workers_count,
                'product_count': product_count, 'orders_count': orders_count,
                }
        return render(request, 'events/order.html', context)



def history(request):
    if request.user.is_superuser == False:
        return redirect('index')
    else:
        items = Product.objects.all()
        orders = Order.objects.all()
        context = {'items': items, 'orders': orders}
        return render(request, 'events/history.html', context)

@login_required(login_url='login')
def staffpage(request, pk):
    workers = User.objects.get(id=pk)
    context = {'workers': workers}
    return render(request, 'events/staffpage.html', context)


@login_required(login_url='login')
def deletepro(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('product')
    context = {'item':item}
    return render(request, 'events/delete.html', context)

@login_required(login_url='login')
def deletepro(request, pk):
    orders = Order.objects.get(id=pk)
    if request.method == 'POST':
        orders.delete()
        return redirect('product')
    context = {'orders':orders}
    return render(request, 'events/deleteorder.html', context)


@login_required(login_url='login')
def updatepro(request, pk):
    item = Product.objects.get(id=pk)
    orders = Order.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=item)
        form = OrderForm(request.POST, instance=orders)
        if form.is_valid():
            form.save()
            return redirect('product')
    else:
        form = ProductForm(instance=item)
    context = {'form': form, 'orders': orders}
    return render(request, 'events/update.html', context)

@login_required(login_url='login')
def updatepro(request, pk):
    orders = Order.objects.get(id=pk)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=orders)
        if form.is_valid():
            form.save()
            return redirect('order')
    else:
        form = OrderForm(instance=orders)
    context = {'form': form, 'orders': orders}
    return render(request, 'events/updateorder.html', context)


@login_required(login_url='login')
def staff_detail(request, pk):
    workers = User.objects.get(id=pk)
    context = {'workers': workers}
    return render(request, 'events/staffdetail.html', context)
