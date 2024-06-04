
from django.urls import path
from .views import CreateCategoryView, CategoryListView, CreateSupplierView, SupplierListView, SupplierDetailView, CategoryDetailView, CreatePharmaceuticalView, PharmaceuticalListView, PharmaceuticalOfCategoryListView, PharmaceuticalDetailView

urlpatterns = [
    path('category/add/', CreateCategoryView.as_view()),
    path('supplier/add/', CreateSupplierView.as_view()),
    path('category/all/', CategoryListView.as_view()),
    path('supplier/all/', SupplierListView.as_view()),
    path('supplier/<int:id>/', SupplierDetailView.as_view()),
    path('category/<int:id>/', CategoryDetailView.as_view()),
    path('pharmaceutical/add/', CreatePharmaceuticalView.as_view()),
    path('pharmaceutical/all/', PharmaceuticalListView.as_view()),
    path('pharmaceutical/category/<str:category_id>/', PharmaceuticalOfCategoryListView.as_view()),
    path('pharmaceutical/<int:id>/', PharmaceuticalDetailView.as_view()),
]