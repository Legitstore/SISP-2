from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
# from .forms import LoginForm
# , MyPasswordResetForm, MyPasswordChangeForm, MySetPasswordForm

urlpatterns = [
    path('', views.loginPage, name='login'),
    path('logout/', auth_view.LogoutView.as_view(next_page='login'), name='logout'),
    # path('register/', views.registerPage, name='register'),
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)