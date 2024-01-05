class Cart():
    def __init__(self, request):
        self.session = request.session
        
        # get the current session key if it exists
        cart = self.session.get('session_key') # if there is a session key to the user get it and assign it to this variable , so now its a session ?
        
        # if the user is new, no ssion key so we need to create one( if the 'coockie' is not there) 
        
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {} 
            
            
        # make sure this cart is global ( to all pages of the sites makes it available to know what the user doing with the cart accross the website)
        self.cart = cart