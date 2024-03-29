from . models import Cart,Cart_Item
from .views import _cart_id

def counter(request):
    item_count=0
    if 'admin' in request.path:
        return  {}
    else:
        try:
            cart=Cart.objects.filter(cart_id=_cart_id(request))
            car_items=Cart_Item.objects.all().filter(cart=cart[:1])
            for cart_item in car_items:
                item_count += cart_item.quantity
        except Cart.DoesNotExist:
            item_count =0
    return dict(item_count=item_count)
