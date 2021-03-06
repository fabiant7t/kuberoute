"""Utility functions"""


def safeget(d, *keys, default_value=None):
    """Get values from nested dictionaries.

    Return None if a key is not available"""
    for key in keys:
        try:
            d = d[key]
        except KeyError:
            return default_value
    return d


def dictionary_is_subset(subset, superset):
    try:
        for key, value in subset.items():
            if superset[key] != value:
                return False
    except KeyError:
        return False
    return True


def check_condition(obj, condition_type):
    conditions = safeget(obj, 'status', 'conditions')
    for condition in conditions:
        if condition['type'] == condition_type:
            return condition
    return None
