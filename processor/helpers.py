from .packages import packages


def get_package_from_list(identifier):
    """
    Returns the packages instance... used only for demonstrating

    Args:
        - identifier (any): package identifier

    Returns:
        - package (Package) instance if found, None otherwise
    """
    return next(filter(lambda obj: obj.identifier == identifier, packages), None)
