from django.urls import path
from products import views

app_name = 'products'

urlpatterns = [
    path('save-deposit-products/', views.save_deposit_products, name='save_deposit_products'),
    path('save-deposit-options/', views.save_deposit_options, name='save_deposit_options'),
    path('deposit-products/', views.deposit_products, name='deposit_products'),
    path('deposit-options/', views.deposit_options, name='deposit_options'),
    path('deposit-products/<int:pk>/', views.deposit_products_detail, name='deposit_products_detail'),
    path('deposit-product-options/<str:fin_prdt_cd>/', views.deposit_product_options, name='deposit_product_options'),
    path('deposit-products/top-rate/', views.top_rate, name='top_rate'),
    path('<int:product_pk>/subscription/', views.subscription, name='product_subscription'),
    path('subscribed-products/', views.subscribed_products, name='subscribed_products'),
]