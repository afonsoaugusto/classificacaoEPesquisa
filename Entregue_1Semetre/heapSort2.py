def opt_heapsort(s):                               
    sl = len(s)                                    

    def swap(pi, ci):                              
        if s[pi] < s[ci]:                          
            s[pi], s[ci] = s[ci], s[pi]            

    def sift(pi, unsorted):                        
        i_gt = lambda a, b: a if s[a] > s[b] else b
        while pi*2+2 < unsorted:                   
            gtci = i_gt(pi*2+1, pi*2+2)            
            swap(pi, gtci)                         
            pi = gtci                              
    # heapify                                      
    for i in range((sl/2)-1, -1, -1):              
        sift(i, sl)                                
    # sort                                         
    for i in range(sl-1, 0, -1):                   
        swap(i, 0)                                 
        sift(0, i)   
