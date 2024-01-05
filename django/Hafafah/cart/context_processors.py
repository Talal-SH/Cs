from .cart import Cart

# create context prossesors to our cart woork on globally

def cart(request):
    # return the default data from our cart 
    return {'cart': Cart(request)}