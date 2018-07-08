# Course Name: Advanced Programming for Language Technologist
# Data: Jan.14, 2016
# Assignment 3


def shellSort(alist):
    sublistcount = len(alist)//2 
    while sublistcount > 0:

      for startposition in range(sublistcount):
        gapInsertionSort(alist,startposition,sublistcount)

      print("After increments of size",sublistcount,
                                   "The list is",alist)  #get the partially sorted lists after each increment 

      sublistcount = sublistcount // 2

def gapInsertionSort(alist,start,gap):  
    for i in range(start+gap,len(alist),gap):

        currentvalue = alist[i]
        position = i

        while position>=gap and alist[position-gap]>currentvalue:
            alist[position]=alist[position-gap]
            position = position-gap

        alist[position]=currentvalue
        
alist = [55,27,23,77,82,92,13,7,25]
shellSort(alist)
print(alist)
