from django.urls import path
from .import views

urlpatterns = [
    path('home', views.index, name='index'),
    path('staff', views.staff, name='staff'),
    path('product', views.product, name='product'),
    path('order', views.order, name='order'),
    path('staffpage/<str:pk>', views.staffpage, name='staffpage'),
    path('delete/<str:pk>/', views.deletepro, name='delete'),
    path('update/<str:pk>/', views.updatepro, name='update'),
    path('staffdetail/<int:pk>', views.staff_detail, name='staff-detail'),
]