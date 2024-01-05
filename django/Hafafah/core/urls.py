from django.urls import path
from core import views


app_name = 'core'

urlpatterns = [
    path("", views.index, name='index' ),
    path("about/", views.about, name='about' ),
    path("products/", views.products, name='products'),
    path("product/<int:pk>", views.product, name='product'),
    path("login/", views.login_user, name='login'),
    path("logout/", views.logout_user, name='logout'),
    path("register/", views.register_user, name='register'),
]
