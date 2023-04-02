'''
Decorators I need.
'''

from functools import wraps


def try_except(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            ok = func(*args, **kwargs)
            return ok
        except Exception as err:
            return f'Error: {str(err)}'
    return wrapper
