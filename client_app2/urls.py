from django.urls import path
from . import views

urlpatterns = [
path("new-order/<cust_id>/", views.new_order, name="new_order"),
    path("save-order/", views.save_order, name="save_order"),
    path("all-orders", views.all_orders, name="all_orders"),
    path("order-status/<order_id>/", views.update_order_status, name="update_order_status"),
    path("export-orders-csv/", views.export_orders_csv, name="export_orders_csv"),
    path("ongoing-orders/", views.ongoing_orders, name="ongoing_orders"),
    path("stock/", views.stock, name="stock"),
    path("add-stock/", views.add_stock, name="add_stock"),
    path("save-stock/", views.save_stock, name="save_stock"),
    path("edit-stock/<stock_id>/", views.edit_stock, name="edit_stock"),
    path("update-stock/<stock_id>/", views.update_stock, name="update_stock"),
    path("delete-stock/<stock_id>/", views.delete_stock, name="delete_stock"),
    path("used-stock/<stock_id>/", views.used_stock, name="used_stock"),
    path("save-used-stock/<stock_id>/", views.save_used_stock, name="save_used_stock"),


]
