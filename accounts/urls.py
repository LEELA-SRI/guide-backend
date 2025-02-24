
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('register', views.register, name='register'), 
    # For Faculties to register their account     
    path('guides-register', views.guides_register, name='guides-register'),

    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    
    # for password reset
    path("password-reset/", views.password_reset, name="password-reset"),
    path("password-reset/done/", views.password_reset_done,
         name="password-reset-done"),
    path("reset/<uidb64>/<token>/", views.password_reset_confirm, name="password-reset-confirm"
         ),

]
urlpatterns += staticfiles_urlpatterns()
