def foo1(value):
    if value:
        return value
    else:
        return None
def foo2(value):
    """Bare return statement implies `return None`"""
    if value:
        return value
    else:
        return
def foo3(value):
    """Missing return statement implies `return None`"""
    if value:
        return value