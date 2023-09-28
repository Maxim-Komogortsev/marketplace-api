from django.urls import path
from .views import ProductViev

urlpatterns = [
    path('', ProductViev.as_view(), name="post"),
    path('<str:prod_name>', ProductViev.as_view(), name="get")
]
