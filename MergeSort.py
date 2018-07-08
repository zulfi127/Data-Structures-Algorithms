# Name: Zulipiye Yusupujiang
# Course Name: Advanced Programming for Language Technologist
# Data: Jan.14, 2016
# Assignment 3
# Question 5

def mergeSort(alist):
	print("Splitting", alist)
	if len(alist)>1: # if the list has more than one item.
		mid = len(alist)//2
		leftHalf = alist[:mid] # use the slice operation to get the left halves;
		rightHalf = alist[mid:] # use the slice operation to get the right halves.

		mergeSort(leftHalf) # invoke the left half
		mergeSort(rightHalf)# invoke the right half

		i= 0
		j= 0
		k= 0

		# Merge the two smaller sorted list into one larger sorted list;
		# Merge operation places the items back into the original list (alist) one at a time by repeatedly taking the smallest item from the sorted lists.
		while i < len(leftHalf) and j < len(rightHalf):
			if leftHalf[i] < rightHalf[j]:
				alist[k]= leftHalf[i]
				i= i+1
			else:
				alist[k]= rightHalf[j]
				j= j+1
			k=k+1

		while i < len(leftHalf):
			alist[k]= leftHalf[i]
			i= i+1
			k=k+1

		while j < len(rightHalf):
			alist[k]= rightHalf[j]
			j=j+1
			k=k+1
	print("Merging", alist)

alist = [27,55,23,77,82,92,13,25,7]
mergeSort(alist)
print(alist)
