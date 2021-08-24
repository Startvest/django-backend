from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('registration/', include('dj_rest_auth.registration.urls')),
    path('create_user_type/<int:uid>', views.create_user_type),
    path('get_user_type/<int:uid>', views.get_user_type, name='view_user_type'),
]