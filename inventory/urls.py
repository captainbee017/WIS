from django.conf.urls import url

from inventory.views import InventoryOverview, InventoryAddView, InventoryUpdateView, InventoryDeleteView, \
    OutofStockItems

urlpatterns = [
    url(r'^$', InventoryOverview.as_view(), name='inventory_overview'),
    url(r'^add-items/$', InventoryAddView.as_view(), name='inventory_add'),

    url(r'^edit-item/(?P<pk>\d+)/$', InventoryUpdateView.as_view(), name='inventory_edit'),
    url(r'^delete-item/(?P<pk>\d+)/$', InventoryDeleteView.as_view(), name='inventory_delete'),

    url(r'^out-of-stock-items/$', OutofStockItems.as_view(), name='out_of_stock'),
]