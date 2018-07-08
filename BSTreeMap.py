# Name: Zulipiye Yusupujiang
# Course Name: Advanced Technology for Language Technologist
# Data: Jan.22, 2016
# Assignment 3
# Question 3
# I got the idea from the text book PS, and also discussed with Fatomato about some solutions.

class BSNode:
	def __init__(self,key,val,left=None,right=None,parent=None):
		self.key = key
		self.payload = val
		self.rightChild = right
		self.leftChild = left
		self.parent=parent
	
	def hasLeftChild(self):
		return self.leftChild

	def hasRightChild(self):
		return self.rightChild
   
class BSTreeMap: # associate keys with values as dictionaries; 
	def __init__ (self):
		self.root = None
	
	def put(self,key,val):
        	if self.root:
            		self._put(key,val,self.root)
        	else:
            		self.root = BSNode(key,val)
			

	def _put(self,key,val,currentNode):
		if key < currentNode.key:
			if currentNode.hasLeftChild():
				self._put(key,val,currentNode.leftChild)
			else:
				currentNode.leftChild = BSNode(key,val,parent=currentNode)
		else:
			if currentNode.hasRightChild():
				self._put(key,val,currentNode.rightChild)
			else:
				currentNode.rightChild = BSNode(key,val,parent=currentNode)

	
	def get(self,key, value= None):
		mylist = []  #create an empty list to collect the list of values
		newNode = BSNode(key, value)
		if self.root == None : # if the tree is  empty 
			self.root = newNode
			return 
		temp = self.root
		while temp is not None:
			if temp.key == key:
				mylist += [temp.payload]
				temp = temp.rightChild
			else:
				if temp.key > key :
					temp = temp.rightChild
				else:
					temp = temp.leftChild
		return mylist


posmap = BSTreeMap()
posmap.put('duck','verb')
posmap.put('duck','noun')
print(posmap.get('duck')) 


    
