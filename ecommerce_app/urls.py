
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product/<int:product_id>/<slug:product_slug>/',
        views.show_product, name='product_detail'),
    path('cart/', views.show_cart, name='show_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('contact/',views.contact, name='contact' ),
    path('reviews/',views.reviews, name='reviews' ),
    path('about/',views.about, name='about' ),
    path('products/',views.products, name='products' ),
    path('process-payment/', views.process_payment, name='process_payment'),
    path('payment-done/', views.payment_done, name='payment_done'),
    path('payment-cancelled/', views.payment_canceled, name='payment_cancelled'),
]