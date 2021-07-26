from django.urls import path
from . import views

app_name = 'startups'

urlpatterns = [
    path('', views.StartupsList.as_view(), name='startups_list'),
    path('<int:user_id>', views.StartupsInfo.as_view(), name='view_startup'),
    path('<int:uid>/create', views.create_startup, name="create_startup"),
    path('<int:uid>/update', views.update_startup_info, name="update_startup"),
    path('<int:uid>/withtdraw', views.withdraw, name="withdraw"),
]