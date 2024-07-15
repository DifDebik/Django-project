from django.urls import path

from products.views import (product_detail_view,
                            product_create_view,
                            render_initial_data,
                            dynamic_lookup_view,
                            product_delete_view,
                            product_list_view,
                            )

app_name = 'products'

urlpatterns = [
    path('product/', product_detail_view, name='detail'),
    path('create/', product_create_view, name='create'),
    path('initial/', render_initial_data, name='initial'),
    path('dynamic/<int:my_id>/', dynamic_lookup_view, name='dynamic'),
    path('dynamic/<int:my_id>/delete/', product_delete_view, name='delete'),
    path('list/', product_list_view, name='list'),

]