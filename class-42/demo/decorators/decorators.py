from functools import wraps

def lowerize(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        original_value = func(*args, **kwargs)
        return original_value.lower()
    return wrapper

def camelize(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        original_value = func(*args, **kwargs)
        return original_value.title()
    return wrapper
