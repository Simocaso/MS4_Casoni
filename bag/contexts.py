from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):

    bag_products = []
    total = 0
    subtotal = 0
    product_count = 0
    delivery = 9.99
    bag = request.session.get('bag', {})

    for product_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=product_id)
        total += quantity * product.price
        subtotal = quantity * product.price
        product_count += quantity
        bag_products.append({
            'product_id': product_id,
            'quantity': quantity,
            'product': product,
        })

    context = {
        'bag_products': bag_products,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
    }

    return context
