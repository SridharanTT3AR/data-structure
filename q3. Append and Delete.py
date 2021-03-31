def appendAndDelete(s, t, k):
    s = list(s)
    t = list(t)
    length = len(t)
    ls = len(s)
    if (k>=2*length):
        return "Yes"
    
    for deleting_index in range(length):
        if(ls<=deleting_index):
            break
        elif(s[deleting_index]!=t[deleting_index]):
            break
        
    deletion = length - (deleting_index)
    insertion = ls - (deleting_index)
    result = k - (deletion + insertion)
    if ( result%2==0 and result>=0 ):
        return "Yes"
    return "No"
