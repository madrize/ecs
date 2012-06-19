from django.shortcuts import render_to_response, get_object_or_404
from cart import *
from forms import AddToCartForm
from django.http import HttpResponseRedirect
from product.models import Product
from django.template import RequestContext
from models import CartItem
from django.contrib.auth.decorators import login_required

@login_required
def add_to_cart(request,
                failed_url="/",
                cart_url="/shopping-cart/"):
    """
    Adds an item to cart
    """
    
    if request.method == "POST":
        # form posted, get form info
        data = request.POST.copy()
        quantity = data.get('quantity','')
        product_slug = data.get('product_slug','')
        p = get_object_or_404(Product,slug=product_slug)
        # add item to cart
        try:
            item = CartItem.objects.get(item=p)
        except:
            item = None
        # if this product isnt already in the cart...
        if item is None:
            # create new Cart Item object
            item = CartItem(owner=request.user, item=p, quantity=quantity)
            item.save()
        else:
            # increase the quantity
            item.quantity = item.quantity + int(quantity)
            item.save()
    else:
        # form isnt valid
        return HttpResponseRedirect(failed_url)
    
    # done !
    # redirect to user's cart
    return HttpResponseRedirect(cart_url)


@login_required
def show_cart( request,
                template="cart/show.html"):
    """
    View function for displaying user's shopping cart
    """
    # if form is submitted (using the 'remove' button)
    # remove the selected item from user's cart
    if request.method == 'POST':
        pid = request.POST.get('item_id','')
        # delete the cart item
        p = CartItem.objects.get(id=pid)
        p.delete()
    
    # display the cart after the change
    try:
        cart_items = CartItem.objects.filter(owner=request.user)
    except:
        cart_items = None
    
    return render_to_response ( template,
                                {'items':cart_items},
                                context_instance=RequestContext(request))
