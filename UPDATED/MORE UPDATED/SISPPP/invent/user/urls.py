from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import  MyPasswordResetForm,  MySetPasswordForm
# from .forms import LoginForm
# , MyPasswordResetForm, MyPasswordChangeForm, MySetPasswordForm

urlpatterns = [
    path('', views.loginPage, name='login'),
    path('logout/', auth_view.LogoutView.as_view(next_page='login'), name='logout'),
    # path('register/', views.registerPage, name='register'),
    # FORGET PASSWORD 
    path('password-reset', auth_view.PasswordResetView.as_view(template_name='user/password_reset.html', form_class=MyPasswordResetForm), name='password_reset'),

    path('password_reset/done', auth_view.PasswordResetDoneView.as_view(template_name='user/password_reset_done.html'), name='password_reset_done'),

    path('password-rest-confirm/<uidb64>/<token>/',auth_view.PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html', form_class=MySetPasswordForm), name='password_reset_confirm'),

    path('password-reset-complete', auth_view.PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'), name='password_reset_complete'),
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)