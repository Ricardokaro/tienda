

# Django
from django.urls import path, include

# Django REST Framework
from rest_framework.routers import DefaultRouter

#Views
from .views import stores as store_views
from .views import products as product_views
from .views import shopping as purchase_views
from .views import sales as sale_views

router = DefaultRouter()
router.register(r'stores', store_views.StoreViewSet, basename='store')
router.register(r'stores/(?P<store_id>[0-9]+)/products', product_views.AllProductStoreViewSet, basename='product')
router.register(
    r'sales', 
    sale_views.SaleViewSet, 
    basename='sale'
)

router.register(r'products', product_views.AllProductViewSet, basename='product')
router.register(r'shopping', purchase_views.ShoppingViewSet, basename='shopping')
#router.register(r'shopping', purchase_views.ClientPurchaseViewSet, basename='shopping')



urlpatterns = [
    path("", include(router.urls))
]