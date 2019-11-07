def remove_suffix(suffix, string):
    if string.endswith(suffix):
        ls = len(suffix)
        return string[:-ls]
    else:
        return string
