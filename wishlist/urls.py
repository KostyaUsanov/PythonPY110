from django.urls import path
from .views import wishlist_view, wishlist_add_view, wishlist_del_view, wishlist_remove_view, wishlist_json, \
    wishlist_add_json, wishlist_del_json

app_name = 'wishlist'

urlpatterns = [
    path('', wishlist_view, name="wishlist_view"),
    path('del/<str:id_product>', wishlist_del_view, name="wishlist_del_view"),
    path('add/<str:id_product>', wishlist_add_view, name="wishlist_add_view"),
    path('remove/<str:id_product>', wishlist_remove_view, name="wishlist_remove_view"),
    path('api/', wishlist_json, name="wishlist_json"),
    path('api/del/<str:id_product>', wishlist_del_json, name="wishlist_del_json"),
    path('api/add/<str:id_product>', wishlist_add_json, name="wishlist_add_json"),


]