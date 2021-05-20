def insertion_sort(lst):
    n = len(lst)
    for i in range(1,n):
        j = i-1
        c_val = lst[i]
        while c_val < lst[j] and j>=0:
            lst[j+1] = lst[j]
            j-=1
        lst[j+1] = c_val

if __name__ == '__main__':
    lst = [7,3,2,9,8]
    insertion_sort(lst)
    print(lst)