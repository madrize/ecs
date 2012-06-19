from django.conf.urls.defaults import patterns, include, url
import ecs
from django.contrib import admin
from registration.views import mylogin,register,mylogout
from cart.views import show_cart,add_to_cart
from search.views import search
from reviews.views import get_review, post_review, get_product_reviews

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ecs.views.home', name='home'),
    # url(r'^ecs/', include('ecs.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$',mylogin),
    url(r'^register/$',register),
    url(r'^logout/$',mylogout),
    url(r'^shopping-cart/$',show_cart),
    url(r'^add-to-cart/$',add_to_cart),
    url(r'^search/$',search),
    url(r'^review/([-\w]+)/$',get_review),
    url(r'^post-review/',post_review),
    url(r'^reviews/([-\w]+)/',get_product_reviews)
)

urlpatterns += patterns('ecs.product.views',
    url(r'^categories/$',
        view='get_category_list',
        name='get_category_list'
    ),
    
    url(r'^category/([-\w]+)/$',
        view='get_products_for_category',
        name='get-products-for-category'
    ),
    
    url(r'^product/([-\w]+)/$',
        view='get_product_details',
        name='get-product-details'
    ),
    
    url(r'^tag/([-\w]+)/$',
        view='get_tag',
        name='get-tag'
    ),
    
    url(r'^tags/$',
        view='tag_cloud',
        name='tag-cloud'
    ),
)