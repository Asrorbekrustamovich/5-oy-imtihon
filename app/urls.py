from django.urls import path
from . import views

urlpatterns = [
    path('Product_imageCreateLIst/', views.Product_imageCreateLIst.as_view()),
    path('Product_imageUpdateDelete/<int:pk>/', views.Product_imageUpdateDelete.as_view()),
    path('CategoryCreateList/', views.CategoryCreateList.as_view()),
    path('CategoryUpdateDelete/<int:pk>', views.CategoryUpdateDelete.as_view()),
    path('SellerCreateList/', views.SellerCreateList.as_view()),
    path('SellerUpdateDelete/<int:pk>/', views.SellerUpdateDelete.as_view()),
    path('ProductsCreateList/', views.ProductsCreateList.as_view()),
    path('ProductsUpdateDelete/<int:pk>/', views.ProductsUpdateDelete.as_view()),
    path('Get_selled_proudcts_count_and_all_products_count_and_benefit_for_one_seller/<seller_id>/', views.Get_selled_proudcts_count_and_all_products_count_and_benefit_for_one_seller.as_view()),
]
