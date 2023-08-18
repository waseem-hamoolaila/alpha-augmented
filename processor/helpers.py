from .packages import packages


def get_package_from_list(identifier):
    return next(filter(lambda obj: obj.identifier == identifier, packages), None)
