def remove_suffix(suffix, string):
    """Removes suffix for string if present. If not, returns string as is

    Example: remove_suffix(".com", "example.com") => "example"
    """
    if string.endswith(suffix):
        ls = len(suffix)
        return string[:-ls]
    else:
        return string
