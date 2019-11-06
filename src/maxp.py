def max_product(ns):
    if len(ns) < 2:
        return None

    sorted_ns = sorted(ns)
    largest, second_largest = sorted_ns[-2:]
    return largest * second_largest
