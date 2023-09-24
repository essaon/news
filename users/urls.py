from django.urls import path
from . import views

urlpatterns = [
    path('logout/', views.logout_view.as_view(), name = 'logout'),
    path('login/', views.login_view.as_view(), name = 'login'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('password_change/', views.CustomPasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', views.CustomChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', views.CustomPassResetView.as_view(), name = 'password_reset'),
    path('password_reset/done/', views.CustomPassResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset/confirm/<uidb64>/<token>/', views.CustomPassResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/complete/', views.CustomPassResetCompleteView.as_view(), name = 'password_reset_complete'),
]
