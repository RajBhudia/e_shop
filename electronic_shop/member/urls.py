from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.login_view, name="login"),
    path('customer/', views.customer, name="customer"),
    path('logout/', views.logout_view, name="logout"),
    path('product_admin/', views.product_admin, name="product_admin1"),
    path('try1/', views.trail, name='trails')
]