def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b) :
        # When the sequences being passed are not the same length.
        raise ValueError("Strands must be of equal length.")
    index = 0
    distance = 0
    while index < len(strand_a) :
        if strand_a[index] != strand_b[index] :
            distance += 1
        index += 1
    return distance
