from django.urls import path
from . import views
from . views import ProductViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('product',ProductViewSet)

urlpatterns = [
    # path('import-data/',views.import_dummy_data,name="imported data"),
    path('data-count/',views.num_product,name='count of product'),
]+router.urls