from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Thing


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = get_object_or_404(Thing, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    variant = None
    if 'product_variant' in request.POST:
        variant = request.POST['product_variant']
    bag = request.session.get('bag', {})    # gets bag from sesion or create one

    if variant:
        if item_id in list(bag.keys()):
            if variant in bag[item_id]['items_by_variant'].keys():
                bag[item_id]['items_by_variant'][variant] += quantity
                messages.success(request,
                                 (f'Updated variant {variant.upper()} '
                                  f'{product.title} quantity to '
                                  f'{bag[item_id]["items_by_variant"][variant]}'))
            else:
                bag[item_id]['items_by_variant'][variant] = quantity
                messages.success(request,
                                 (f'Added variant {variant.upper()} '
                                  f'{product.title} to your bag'))
        else:
            bag[item_id] = {'items_by_variant': {variant: quantity}}
            messages.success(request,
                             (f'Added variant {variant.upper()} '
                              f'{product.title} to your bag'))
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(request,
                             (f'Updated {product.title} '
                              f'quantity to {bag[item_id]}'))
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {product.title} to your bag')
    request.session['bag'] = bag    # Update sesion's bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Thing, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    variant = None
    if 'product_variant' in request.POST:
        variant = request.POST['product_variant']
    bag = request.session.get('bag', {})

    if variant:
        if quantity > 0:
            bag[item_id]['items_by_variant'][variant] = quantity
            messages.success(request,
                             (f'Updated variant {variant.upper()} '
                              f'{product.title} quantity to '
                              f'{bag[item_id]["items_by_variant"][variant]}'))
        else:
            del bag[item_id]['items_by_variant'][variant]
            if not bag[item_id]['items_by_variant']:
                bag.pop(item_id)
            messages.success(request,
                             (f'Removed variant {variant.upper()} '
                              f'{product.title} from your bag'))
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(request,
                             (f'Updated {product.title} '
                              f'quantity to {bag[item_id]}'))
        else:
            bag.pop(item_id)
            messages.success(request,
                             (f'Removed {product.title} '
                              f'from your bag'))

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        product = get_object_or_404(Thing, pk=item_id)
        variant = None
        if 'product_variant' in request.POST:
            variant = request.POST['product_variant']
        bag = request.session.get('bag', {})

        if variant:
            del bag[item_id]['items_by_variant'][variant]
            if not bag[item_id]['items_by_variant']:
                bag.pop(item_id)
            messages.success(request,
                             (f'Removed variant {variant.upper()} '
                              f'{product.title} from your bag'))
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.title} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
