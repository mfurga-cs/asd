def alloc(n): 
    return [randint(0, 1000000000) for i in range(n)]

def count(a,b, k):
    n = len(a)
    A = [0 for _ in range(k)]
    B = [0 for _ in range(k)]
    while i < n:
        A[a[i]] += 1 
        B[b[i]] += 1
        i += 1
    for j in range(k):
        if A[j] != A[j]:
            return False
    return True


def anagram(A, B, k):
    n = len(A)
    T = alloc(k)

    for i in range(n):
        T[A[i]] = 0
        T[B[i]] = 0
    

    # j = 0
    # for i in range(n):
    #     if T[A[i]] == 0:
    #         T[A[i]] = 1
    #         I[j] = A[i]
    #         j += 1
    #     else:
            

    for i in range(n):
        T[A[i]] += 1
        T[B[i]] -= 1
    
    for i in range(n):
        if T[A[i]] != 0:
            return False

    
    return True