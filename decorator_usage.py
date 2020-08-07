def new_decorator(func):
    def _wrapper(*args, **kwargs):
        print ("args are ", args)
        print ("Kwargs are ", kwargs)
        func()
        print("End")
    return _wrapper

@new_decorator
def a_stand_alone_func(*args, **kwargs):
    print("Hello I am in the stand alone func")

a_stand_alone_func(1,2,3,4,5,name="adada")