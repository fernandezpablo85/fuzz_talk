def max_product(ns):
    """Given a list of numbers, return the maximum product possible between two.

    Example: [10, 2, 3, 4] => 4 * 10 => 40
    """
    if len(ns) < 2:
        return None

    sorted_ns = sorted(ns)
    largest, second_largest = sorted_ns[-2:]
    return largest * second_largest
