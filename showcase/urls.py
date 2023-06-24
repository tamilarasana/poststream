from unicodedata import name
from unittest.mock import patch
from django.urls import path
from .views import *
app_name = "SuperApp"

urlpatterns = [
    # CATEGORY - ITEM LIST - ITEM DESCRIPTION - related
    path('get_category/', getCategory, name="categories"),
    path('get_itemlist/<int:key>', getItemList, name="itemlists"),
    path('get_dist_itemdesc/<int:key>', getItemDescDist, name="disct itemdesc"),
    path('get_itemdesc/<int:key>', getItemDesc, name="itemdesc"),
    path('get_color_itemdesc/', getColorItemDesc, name="coloritemdesc"),
    # Search
    path('search_item/', search_item, name="search_item")
]