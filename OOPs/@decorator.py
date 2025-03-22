# Decorator: function that extends the behavior of base class
#            without changing its actual code

def add_sprinkles(func):
    def wrapper(*args,**kwargs):
        print("** You added sprinkles **")
        func(*args,**kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args,**kwargs):
        print("** You added Fudge **")
        func(*args,**kwargs)
    return wrapper

@add_sprinkles
@add_fudge      # decorator
def get_ice_cream(flavour):
    print(f"Here is your {flavour} Ice cream🍨")

get_ice_cream("Vanilla")