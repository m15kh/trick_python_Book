def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper


def uppercase1(func):
    def wrapper():
        return func()
    return wrapper