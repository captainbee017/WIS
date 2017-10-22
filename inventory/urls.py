from django.conf.urls import url

from inventory.views import InventoryOverview, InventoryAddView, InventoryUpdateView, InventoryDeleteView, \
    OutofStockItems, ItemCategoryListView, ItemCategoryUpdateView, ItemCategoryDeleteView, ItemListView

urlpatterns = [
    url(r'^$', InventoryOverview.as_view(), name='inventory_overview'),
    url(r'^add-items/$', InventoryAddView.as_view(), name='inventory_add'),

    url(r'^edit-item/(?P<pk>\d+)/$', InventoryUpdateView.as_view(), name='inventory_edit'),
    url(r'^delete-item/(?P<pk>\d+)/$', InventoryDeleteView.as_view(), name='inventory_delete'),

    url(r'^out-of-stock-items/$', OutofStockItems.as_view(), name='out_of_stock'),

    url(r'^categories/$', ItemCategoryListView.as_view(), name='category_list'),
    url(r'^category/edit/(?P<pk>\d+)/$', ItemCategoryUpdateView.as_view(), name='category_update'),
    url(r'^category/delete/(?P<pk>\d+)/$', ItemCategoryDeleteView.as_view(), name='category_delete'),

    url(r'^item-list/(?P<cat_id>\d+)/$', ItemListView.as_view(), name='item_list_category'),
    url(r'^item-list/$', ItemListView.as_view(), name='item_list'),
]