import time
def time_calculation(func):
    def wrapper(*args,**kwargs):
        s=time.perf_counter()
        e=time.perf_counter()
        print(f'time estimation for {func.__name__} is {e-s}')
        return func
    return wrapper()