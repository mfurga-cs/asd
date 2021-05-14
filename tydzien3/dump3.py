
def zad(A,k):
    B=[0]*k
    x=0
    y=len(A)
    i=0
    j=0
    kol=0
    while j<len(A):    
        if kol==k:
            if j-i<y-x: 
                x=i
                y=j
            B[A[i]]-=1
            i+=1
            if B[A[i]]==0: kol-=1
        else:
            B[A[j]]+=1
            j+=1
            if B[A[j]]==1: kol+=1


