import functools
from datetime import datetime




def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('call %s():'  % func.__name__)
        return func(*args, **kwargs)
    return wrapper


# @log
# def now():
#     print(datetime.now())

# now()

def log2(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print('%s %s():' %(text, func.__name__))
            return func(*args, **kwargs)
        return wrapper
    return decorator


@log2('execute')
def now():
    print(datetime.now())

now()