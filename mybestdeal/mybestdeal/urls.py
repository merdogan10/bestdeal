from django.conf.urls import url
from django.contrib import admin
from bestdeal import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.index,name='index'),
    url(r'^search$',views.search_view,name='search'),
    url(r'^contact/$',views.contact_view,name='contact'),
    url(r'^privacy/$',views.privacy_view,name='privacy'),
    url(r'^terms/$',views.terms_view,name='terms'),
    url(r'^(?P<category_name>[A-Za-z &]+)/(?P<sub_category_name>[A-Za-z &]+)/(?P<product_id>[0-9]+)/$',views.detail,name='detail'),
    url(r'^(?P<category_name>[A-Za-z &]+)/$',views.category_items,name='category_items'),
    url(r'^(?P<category_name>[A-Za-z &]+)/(?P<sub_category_name>[A-Za-z &]+)/$',views.category_sub_category_items,name='category_sub_category_items'),
]
