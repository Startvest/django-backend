from django.urls import path, include
from .views import UserRegisterView

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('registration/', UserRegisterView.as_view(), name='registration')
]


# 92586d94c3382b5ec174ad2f740490c3fc62dc9d