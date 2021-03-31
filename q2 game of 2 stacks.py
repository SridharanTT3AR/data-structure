def twoStacks(maxSum, a, b):
    total_elements = value = j= i=0
    
    while(i<len(a)):
        if(value+a[i]>maxSum):
            break
        value+=a[i]
        total_elements += 1
        i+=1
    
    
    while (j<len(b) and i>=0):
        value+=b[j]
        j+=1
        while(i>0 and value>maxSum):
            i-=1
            value-=a[i]
            
            
        if(value<=maxSum and i+j>total_elements):
            total_elements = i+j
    return total_elements
