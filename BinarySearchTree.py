

class BSTree: # Binary Search Tree
    
    def __init__(self):
        self.root = None
                
    def depth(self):
        if self.root == None:
            return 0
        else:
            return self.root.depth() # BSNode depth as assignment
            
    def __str__(self): 
        if self.root == None:
            return "EmptyBSTree"
        else:
            return self.root.__str__()


    def insert(self, value):
        if self.root == None:
            self.root= BSNode(value)
        else:
            self.root.insert(value)

    def sort(self):
        if self.root != None:
            return self.root.sort
        else:
            return "EmptyBSTree"


class BSNode: # Binary Search Tree Node

    def __init__(self,val):
        self.left = None
        self.right = None
        self.value = val
                
    def __str__(self): 
        return self.strIndent('')

    def insert(self, newVal):
        
        if newVal < self.value:
            if self.left == None:
                self.left= BSNode(newVal)
            else:
                self.left.insert(newVal)
               
        elif newVal > self.value:
            if self.right == None:
                self.right= BSNode(newVal)
            else:
                self.right.insert(newVal)
            
     
    def calculate_depth(self):
        # if both subtrees are empty trees; 
        if self.left == None and self.right== None:
            return 1
        
        # if the left subtree is empty, but the right subtree is not empty;
        elif self.left == None:
            return self.right.calculate_depth()+ 1
        
        # if the right subtree is empty, but the left subtree is not empty;
        elif self.right == None: 
            return self.left.calculate_depth()+ 1
        
        # if neither subtree is empty
        
        return max(self.left.calculate_depth(), self.right.calculate_depth()) +1


    def sort_value(self):
        sorted_values = []
        if self.left:
            sorted_values.extend(self.left.sort_value())
        sorted_values.append(self.value)
        if self.right:
            sorted_values.extend(self.right.sort_value())
        return sorted_values
           
    
    def strIndent(self,ind):
        """Makes text-based print of tree"""
        outputString = ''
        if self.left == None and self.right != None:
            outputString = outputString  + ind + '  [none]\n' 
        if self.left != None:
            outputString = outputString + self.left.strIndent(ind + '  ')
        outputString = outputString + ind + self.value + '\n'
        if self.right == None and self.left != None:
            outputString = outputString  + ind + '  [none]\n' 
        if self.right != None:
            outputString = outputString  + self.right.strIndent(ind + '  ')
        return outputString


def treeSort(alist):
    treeSort= BSTree()
    for item in alist:
        treeSort.insert(item)
    return treeSort.sort_value()



tree = BSTree()
tree.root= BSNode(27)
for i in [14,23,12,56,92]:
    tree.root.insert(i)


print(tree.root.sort_value())
print(tree.root.calculate_depth())


        
