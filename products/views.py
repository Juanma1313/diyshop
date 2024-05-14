from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from django.http import HttpResponseRedirect

from .models import Thing, Category, Instructions
#from .forms import ProductForm


def all_products(request):
    """ A view to show all products, including sorting and search queries """
    #products = Thing.objects.filter(status=1, parent__isnull=True).order_by('-created_on')
    # Select all the publiched products that are root or have instructions
    products = Thing.objects.filter(Q(status=1, parent__isnull=True) | Q(status=1, instructions__isnull=False) ).distinct()
    #print(str(products.query))

    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'title':      #title:  to sort by title in lower case
                sortkey = 'lower_title'
                products = products.annotate(lower_title=Lower('title'))
            elif sortkey == 'category': # category: to sort by category name
                sortkey = 'category__name'
            elif sortkey == 'date':     # date: to sort by created_on
                sortkey = 'created_on'
            elif sortkey == 'rating':   # rating: to sort by rating
                sortkey = 'rating'
            elif sortkey == 'price':    # price: to sort by price
                sortkey = 'price'
            else:   #  Unrecogniced sort option 
                messages.error(request, ("Sort option not available"))
                return redirect(reverse('products'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'price' in request.GET:
            price = request.GET['price']
            try:    # Verify price value
                price=str(float(price))
            except:
                messages.error(request, ("price not valid"))
                return redirect(reverse('products'))
            if price=='0.0':
                products = products.filter(Q(price=price) | Q(price=None))
            else:
                products = products.filter(price=price)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, ("You didn't enter any search criteria!"))
                return redirect(reverse('products'))

            queries = Q(title__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    ''' Provides with the details for the selected thing.
    it also creates a dictionary is_component_thing that indicates if there are
    nested instructions in any of the Thing's Components'''

    product = get_object_or_404(Thing, pk=product_id)
    instructions = product.instructions.order_by("title")
    components = product.components.filter(status=1).order_by("title")
    liked = False
    if product.likes.filter(id=request.user.id).exists():
        liked = True
    is_component_thing = {}
    for i in components:
        is_component_thing[i.id] = Instructions.objects.filter(thing=i.id).exists()

    context = {
        'product': product,
        'components': components,
        'instructions': instructions,
        'is_component_thing': is_component_thing,
        'liked': liked

    }

    return render(request, 'products/product_detail.html', context)

def productlike(request, product_id):
    ''' This view allows for adding/removing a user Like to/from a Thing.
    If the user like already exists it removes it otherwise it adds it '''
    if request.POST:        
        product = get_object_or_404(Thing, pk=product_id)
        if product.likes.filter(id=request.user.id).exists():
            product.likes.remove(request.user)
        else:
            product.likes.add(request.user)

        return redirect(reverse('product_detail', args=[product_id]))
