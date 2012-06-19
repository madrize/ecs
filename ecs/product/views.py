from django.shortcuts import render_to_response,get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect,Http404
from product.models import Category, Product, Tag
from reviews.models import Review
from forms import AddToCartForm

def get_category_list(request,
                      template="catalog/get_categories.html"):
    """ Returns the list of categories """
    try:
        cats = Category.objects.all()
    except:
        raise Http404
    
    return render_to_response(template,
                              {"categories":cats},
                              context_instance=RequestContext(request))

def get_products_for_category(request,
                              slug,
                              template="catalog/get_products.html"):
    """ Returns a list of products for a chosen category """
    try:
        products = Product.objects.filter(categories__slug=slug)
    except:
        raise Http404
    
    return render_to_response(template,
                              {"products":products},
                              context_instance=RequestContext(request))

def get_product_details(request,
                        slug,
                        template="catalog/get_product.html"):
    """ Returns the info about a product """
    product = get_object_or_404(Product,slug=slug)
    # get the reviews for this product
    reviews = Review.objects.filter(product__slug=slug)
    # 'add to cart' button
    form = AddToCartForm()
    return render_to_response(template,
                              {"product":product,"form":form, "reviews":reviews},
                              context_instance=RequestContext(request))


def get_tag(request,
            slug,
            template="catalog/get_tag.html"):
    """ Returns the products that belongs to the tag """
    tag = get_object_or_404(Tag,slug=slug)
    try:
        products = Product.objects.filter(tags__slug=slug)
    except:
        raise Http404
    
    return render_to_response(template,
                              {"products":products,"tag":tag},
                              context_instance=RequestContext(request))

def tag_cloud(request,
              template="catalog/tags.html"):
    """ Returns a list of tags """
    try:
        tags = Tag.objects.all()
    except:
        raise Http404
    
    return render_to_response(template,
                              {"tags":tags},
                              context_instance=RequestContext(request))

def get_similar_products(request):
    pass

