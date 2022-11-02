from .import views
from django.urls import path,include

app_name='ecomapp'
urlpatterns = [

    path('',views.allProdCat,name='allProdCat'),
    path('<slug:c_slug>/',views.allProdCat,name='Products_by_Category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.proDetail,name='ProdCatdetail')
]