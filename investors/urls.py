from django.urls import path

from . import views

app_name = 'investors'

urlpatterns = [
    path('', views.InvestorsList.as_view(), name='investors_list'),
    path('<int:user_id>', views.InvestorsInfo.as_view(), name='view_investor'),
    path('<int:uid>/create', views.create_investor, name="create_investor"),
    path('<int:uid>/update', views.update_investor_info, name="update_investor"),
    path('<int:uid>/invest', views.invest, name="invest"),
]