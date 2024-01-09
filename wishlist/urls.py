from django.urls import path
from .views import wishlist_view, wishlist_add_view, wishlist_del_view

app_name = 'wishlist'

urlpatterns = [
    path('', wishlist_view, name="wishlist_view"),
    path('remove/<str:id_product>', wishlist_del_view, name="remove_from_wishlist"),
    path('add/<str:id_product>', wishlist_add_view, name="wishlist_add_view")

]