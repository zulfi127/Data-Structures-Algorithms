# Name: Zulipiye Yusupujiang
# Course Name: Advanced Technology for Language Technologist
# Data: Jan.14, 2016
# Assignment 3
# Question 1
# I got the idea from the book PS, and disscussed about some solutions with Mary.

class Tree:
    def __init__(self,ldef):
        """Create tree from list as bracketed representation"""
        self.subtrees = []   
        if isinstance(ldef, str):
            # single string is a leaf
            self.symbol = ldef
        else:
            # list read [symbol,subtree0,subtree1,...]
            self.symbol = ldef[0]
            for st in ldef[1:]:
                self.addSubtree(Tree(st))
    
    def addSubtree(self,subtree):
        """Add a subtree to the right"""
        self.subtrees.append(subtree)
        
        
    def leaf(self):
        """test leaf-hood"""
        return self.subtrees == []

    def __str__(self): 
        return self.strIndent('')

 
    def strIndent(self,ind):
        """Makes text-based print of tree"""
        outputString = ind + self.symbol
        if len(self.subtrees) == 1 and self.subtrees[0].leaf():
            return outputString + ' ' + self.subtrees[0].symbol # for pos-word cases
        for st in self.subtrees:
            outputString = outputString + '\n' + st.strIndent(ind + '  ')
        return outputString

    def get_leaf_nodes(self): # retrieves the value of leaf in a tree.
        if self.leaf():
            return [self.symbol]
        else:
            leaves= []
            for st in self.subtrees:
                #add the leaf nodes to the list:
                leaves= leaves+st.get_leaf_nodes()
        return leaves

    def largest_number_subtrees(self): # return the number of largest number of subtrees.
        if self.subtrees==[]:
            return 0
        else:
            largest= len(self.subtrees)
            for st in self.subtrees:
                if st.subtrees != []:
                    largest= max(largest, st.largest_number_subtrees())
        return largest
        

        
tree= ['S', ['NP', ['PROPN',' Pierre' ],['PROPN',' Vinken' ]],['VP', ['VERB',' saw'],['NP', ['NP', ['DET', 'the'],['NOUN', 'man']],['PP', ['ADP', 'with'],['NP', ['DET', 'the'],['NOUN', 'club']]]]],['PUNCT', '.' ]]


my_tree= Tree(tree)

print(my_tree.largest_number_subtrees())
print('\n')
print(my_tree)
print('\n')
print(my_tree.get_leaf_nodes())



