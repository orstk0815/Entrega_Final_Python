from django.urls import path
from .views import usuario_index, signin, sign_out, signup, cambiar_foto

urlpatterns = [
    path('usuario/<int:user_id>', usuario_index, name='usuario_index'),
    path('signup/', signup, name='signup'),
    path('accounts/login/', signin, name='signin'),
    path('sign_out/', sign_out, name='signout'),
    path('cambiar_foto/<int:perfil_id>/', cambiar_foto, name='cambiar_foto'),
]
