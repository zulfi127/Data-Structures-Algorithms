# Course Name: Advanced Programming for Language Technologist
# Data: Jan.14, 2016
# Assignment 3

def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,pL,pR):
	if pL<pR:

		splitpoint = partition(alist,pL,pR)

		quickSortHelper(alist,pL,splitpoint-1)
		quickSortHelper(alist,splitpoint+1,pR)


def partition(alist,pL,pR): # we use "partion" function to move items that are on the wrong side with respect to the pivot value while also converging on the split point.

	pivotvalue = alist[pL] # use the first item in the list as the pivot.

	leftmark = pL+1 # left mark is the first item in the remaining part of the list;
	rightmark = pR # right mark is the last item in the ramaining part of the list.

	done = False
	while not done:

		while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
			leftmark = leftmark + 1

		while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
			rightmark = rightmark -1

		if rightmark < leftmark: # now the position of the rightmark is the split point.
			done = True # now we can exchange the pivot value with the content of the split point and the pivot value is now in place.
# every item left to the split point is less than the pivot value; every item right to the split point is larger than the pivot value.
		print ("Partion Process", alist)
		if rightmark >= leftmark:
			temp = alist[leftmark]
			alist[leftmark] = alist[rightmark]
			alist[rightmark] = temp
			
		
	temp = alist[pL]
	alist[pL] = alist[rightmark]
	alist[rightmark] = temp
	
	return rightmark

alist = [55,27,23,77,82,92,13,7,25]
quickSort(alist)
print(alist)

