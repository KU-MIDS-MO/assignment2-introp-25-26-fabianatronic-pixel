def has_adjacent_duplicate(L):
    if len(L)<2:
        return False
    previous=0
    for number in L:
        if number==previous:
            return True
        previous=number
    return False
    
        