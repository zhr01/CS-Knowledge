def lis(A):
    d =[0 for _ in range(len(A))]
    max_len = d[0] = 1
    for k in range(1, len(A)):
        tmp = []
        for i in range(k):
            if A[k] > A[i]:
                tmp.append(d[i] + 1)
        d[k] = 1 if len(tmp) == 0 else max(tmp)
        if d[k] > max_len: max_len = d[k]
    return max_len

A = [5,6,1,2,8,3,4]
print(lis(A))
