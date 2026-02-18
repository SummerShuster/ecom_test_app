from .cart import Cart

#create context processor so cart will work on all pages
def cart(request):
    return {'cart': Cart(request)}


