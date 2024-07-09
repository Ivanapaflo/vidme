from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("", views.fetchVideo, name= 'home'),
    path("<movie_id>", views.navigate, name= 'Nav'),
    path("login/", views.ulogin, name="login"),
    path("logout/", views.ulogout, name="logout"),
    path("register/", views.register, name="register"),

    path("change_password/", auth_views.PasswordResetView.as_view(template_name="change_password.html"), name="change_password"),
    path("password_reset_done/", auth_views.PasswordResetDoneView.as_view(template_name="change_password_requested.html"), name="password_reset_done"),
    path("password_reset_confirm/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name="reset_pas.html"), name="password_reset_confirm"),
    path("password_reset_complete/", auth_views.PasswordResetCompleteView.as_view(template_name="change_password_successful.html"), name="password_reset_complete"),

]