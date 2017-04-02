from django.conf.urls import url



from . import views

urlpatterns = [
    url(r'^$', views.products_list, name='products_list'),
    url(r'^product/(?P<pk>[0-9]+)/$', views.product_by_id, name='product_by_id'),
    url(r'^login', views.login, name='login'),
    url(r'^basket', views.basket, name='basket'),
]

# login_required