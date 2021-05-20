import random

def merge(lst,l,m,r):
    n1 = m - l + 1
    n2 = r - m
    L, R = [0 for i in range(n1)], [0 for i in range(n2)]
    for i in range(n1):
        L[i] = lst[l + i]
    for j in range(n2):
        R[j] = lst[m + 1 + j]
    i, j, k = 0, 0, l
    while(i < n1 and j < n2):
        if L[i] < R[j]:
            lst[k] = L[i]
            i+=1
        else:
            lst[k] = R[j]
            j+=1
        k+=1
    while(i < n1):
        lst[k] = L[i]
        k+=1
        i+=1
    while(j < n2):
        lst[k] = R[j]
        k+=1
        j+=1

def mergeSort(lst, l, r):
    if l < r:
        m = (l + r)//2
        mergeSort(lst, l, m)
        mergeSort(lst, m+1,r)
        merge(lst,l,m,r)

if __name__ == "__main__":
    n = int(input("Size of the list: "))
    lst = [random.randint(1,100) for i in range(n)]
    print(lst)
    mergeSort(lst, 0, n-1)
    print(lst)