from django.urls import path, include

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('registration/', include('dj_rest_auth.registration.urls'))
]


# 92586d94c3382b5ec174ad2f740490c3fc62dc9d