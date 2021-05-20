import random

def bubble_sort(lst):
	n = len(lst)
	for k in range(n):
		i = 0
		j = i+1
		while(i < n and j < n):
			if lst[i] > lst[j]:
				temp = lst[j]
				lst[j] = lst[i]
				lst[i] = temp
			i+=1
			j+=1
	return lst
if __name__=="__main__":
	n = int(input("Size of the list: "))
	lst = [random.randint(1,100) for i in range(n)]
	print(lst)
	lst_sort = bubble_sort(lst)
	print(lst_sort)