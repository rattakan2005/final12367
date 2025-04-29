from django.urls import path
from bookstore import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.index, name='index'),
    path('about/',views.about),
    path('form/',views.add_book,name="add_book"),
    path('index', views.index, name='index'),
    path('checkout', views.checkout, name='checkout'),
    path('cart_view/',views.cart_view, name='cart_view'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'), 
    path('search/',views.search, name='search'),
    path('edit/<int:pk>/',views.edit, name='edit'),
    path('delete/<int:pk>/',views.delete, name = 'delete'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
    # path('submit-payment', views.submit_payment, name='submit_payment'),

]