from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import CrearUsuario, LoginUsuario
from .forms import LoginForm
from core import views as core_views

# Aca van todas las rutas de las cuentas
urlpatterns = [
    path('', LoginView.as_view(template_name='accounts/login.html', authentication_form=LoginForm), name='login'),
	path('home/', core_views.home, name='home'),
    path('signup/', CrearUsuario.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]