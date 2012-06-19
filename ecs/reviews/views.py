from models import Review
from forms import ReviewForm
from django.shortcuts import render_to_response,get_object_or_404
from django.template import RequestContext
from product.models import Product
from django.template.defaultfilters import slugify
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

@login_required
def post_review(request,
                template="reviews/post_review.html"):
    """
    View used to post a new review
    """
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        # get values
        s = request.GET.get('s','')
        t = request.POST['title']
        c = request.POST['content']
        r = request.POST['rating']
        # get product
        item = get_object_or_404(Product,slug=s)
        # new review
        rev = Review(title=t,content=c,product=item,sender=request.user,slug=slugify(t))
        rev.save()
        # add rating for the product
        item.votes = item.votes + 1
        item.total_rating = item.total_rating + int(r)
        item.save()
        # done!
        return HttpResponseRedirect("/")
    else:
        form = ReviewForm()
    
    return render_to_response ( template,
                                {'form':form},
                                context_instance=RequestContext(request))

def get_review( request,
                slug,
                template="reviews/get_review.html"):
    """
    Returns the specified review
    """
    review = get_object_or_404(Review,slug=slug)
    
    return render_to_response ( template,
                                {"review":review},
                                context_instance=RequestContext(request))

def get_product_reviews(request,
                        slug,
                        template="reviews/get_product_reviews.html"):
    """ Returns a list of reviews for a product """
    item = get_object_or_404(Product, slug=slug)
    try:
        reviews = Review.objects.filter(product__slug=slug)
    except:
        reviews = None

    return render_to_response(template,
                              {"reviews":reviews,"product":item},
                              context_instance=RequestContext(request))
