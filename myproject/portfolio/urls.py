from django.urls import path

from . import views
from  portfolio. views import UserCreateView
from django.contrib.auth.views import LoginView,LogoutView,PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView,PasswordChangeView,PasswordChangeDoneView




urlpatterns = [
	path('', views.home, name='home'),
	path('signup',UserCreateView.as_view(template_name="registration/registration_form.html",),name='signup'),
	path('login/',LoginView.as_view(),name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password-reset/',PasswordResetView.as_view(template_name="registration/password_reset_form.html",email_template_name="registration/password_reset_email.html"), name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name="registration/password_reset_done.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name="registration/password_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('password-change/', PasswordChangeView.as_view(template_name="registration/password_change.html"), name='password_change'),
    path('password-change/done/',PasswordChangeDoneView.as_view(template_name="registration/password_change_done.html"), name='password_change_done'),
	path('enter-details/', views.Portfolio_detail, name='Portfolio_detail'),
	path(r'^(?P<username>[\w.@+-]+)/(?P<pk>[0-9]+)/$', views.Portfolio_display, name='Portfolio_display'),
	path('your-portfolios/', views.View_all, name="View_all"),
	path(r'^(?P<username>[\w.@+-]+)/(?P<pk>[0-9]+)/edit/$', views.editform, name="editform"),
	path(r'^privacy-policy/$', views.privacypolicy, name="privacypolicy"),
]