

class NameShortError(ValueError):
    pass



def validate(name):
    if len(name) <10:
        raise NameShortError(name)


class BaseValidationError(ValueError):
    pass

try:
    validate(name)
except BaseValidationError as err:
    handle_validation_error(err)