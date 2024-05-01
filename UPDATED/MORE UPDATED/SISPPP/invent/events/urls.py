from django.urls import path
from .import views
from django.contrib.auth import views as auth_view
from .forms import MyPasswordChangeForm

urlpatterns = [
    path('home', views.index, name='index'),
    path('staff', views.staff, name='staff'),
    path('product', views.product, name='product'),
    path('order', views.order, name='order'),
    path('history', views.history, name='history'),
    path('staffpage/<str:pk>', views.staffpage, name='staffpage'),
    path('delete/<str:pk>/', views.deletepro, name='delete'),
    path('deleteord/<str:pk>/', views.deleteorder, name='deleteord'),
    path('update/<str:pk>/', views.updatepro, name='update'),
    path('updateord/<str:pk>/', views.updateorder, name='updateord'),
    path('staffdetail/<int:pk>', views.staff_detail, name='staff-detail'),

    # path('search', views.search, name='search'),
    # TO CHANGE PASSWORD 
    path('passwordchange/', auth_view.PasswordChangeView.as_view(template_name='change/changepassword.html', form_class=MyPasswordChangeForm, success_url='passwordchangedone'), name='passwordchange'),
    path('passwordchangedone/', auth_view.PasswordChangeDoneView.as_view(template_name='change/passwordchangedone.html'), name='passwordchangedone'),
]