def swap_ends(L, k):
    n=len(L)
    if n==0 or k<=0 or k>n//2:
        return L.copy(),0
        
    new_list = []
    new_list.extend(L[-k:])
    new_list.extend(L[k:n-k])
    new_list.extend(L[:k])
    return new_list, k

    

    
    

