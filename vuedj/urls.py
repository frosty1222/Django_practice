from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static
# define the urls
app_name = 'vuedj'
urlpatterns = [
    path('',views.index,name="index"),
    path('products', views.products, name="products"),
    path('product_detail/<int:id>/', views.product_detail,name="product_detail"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
