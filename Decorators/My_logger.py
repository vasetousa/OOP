def my_logger(func):
    import logging
    import functools
    logging.basicConfig(filename=f'{func.__name__}.log', level=logging.INFO)

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f'Ran with args {args} and kwargs {kwargs}')
        return func(*args, **kwargs)

    return wrapper


@my_logger
def display_info(name, age):
    print(f'Display_info ran with arguments {name}, {age}')


display_info("John", 25)
