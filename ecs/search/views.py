from django.shortcuts import render_to_response
from product.models import Product
from django.template import RequestContext
from forms import SearchForm
from django.http import HttpResponseRedirect
from datetime import datetime,timedelta

def search(request,
           template="search/search.html"):
    if request.method == "POST":
        # user has to wait 30 seconds after each search
        # check if session is set
        lst = request.session.get('last_search_time','')
        if not lst is '':
            # if it is, compare the times
            if (datetime.now() - request.session['last_search_time']) < timedelta(seconds=30):
                return HttpResponseRedirect("/search/")
        form = SearchForm(request.POST)
        value = request.POST.get('search_key','')
        category = request.POST.get('categories','')
        # search for the product
        if category == '':
            ps = Product.objects.filter(slug__icontains=value)
        else:
            ps = Product.objects.filter(categories=category,slug__icontains=value)
        # set session
        request.session['last_search_time'] = datetime.now()
    else:
        form = SearchForm()
        ps = None
    
    return render_to_response(template,
                              {'results':ps, 'form':form},
                              context_instance=RequestContext(request))
