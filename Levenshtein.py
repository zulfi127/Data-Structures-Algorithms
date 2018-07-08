
# Name: Zulipiye Yusupujiang
# Course Name: Advanced Technology for Language Technologist
# Data: Jan 06, 2016
# Assignment 2
# Question 4a

#  I can print out the table with two strings and numbers,but I could not able to add the letters such as i,d,s,m in the table with the following solution. So got help from Richard, and wrote the another different code for printing a table with those letters( so please look at my second code for this question 4b)




class LevenshteinTable:

    def __init__(self, s1, s2):
        self.s1 = s1
        self.s2 = s2
        self.table = [[0 for _ in range(len(self.s1)+1)] for _ in range(len(self.s2)+1)]
        
        for j in range(len(self.s2)+1):
            self.table[j][0] = j
        for i in range(len(self.s1)+1):
            self.table[0][i] = i
            
    def distance(self):
        if self.s1==self.s2:
            return 0
        for j in range(len(self.s2)):
            for i in range(len(self.s1)):
                if self.s2[j]== self.s1[i]:
                    cost = 0
                else:
                    cost = 1
                    
                self.table[j+1][i+1] = min (self.table[j][i+1]+ 1,
                                            self.table[j+1][i]+ 1,
                                            self.table[j][i] + cost,)
        return self.table[-1][-1]


    def get_table(self):
        if self.s1 == self.s2:
            return self.table

        if self.s1 == '':
            for j in range(1,len(self.table)): # 7 0123456
                for i in range(len(self.table[0])): # 1 0
                    self.table[j][i][0] = j
                    self.table[j][i][1] = 'i'
            return self.table

        if self.s2 == '':
            for j in range(len(self.table)): # 1 0
                for i in range(1, len(self.table[0])): # 9 012345678
                    self.table[j][i][0] = i
                    self.table[j][i][1] = 'd'
            return self.table

        else:
            for j in range(1,len(self.table)): # 7 0123456
                for i in range(1, len(self.table[0])): # 9 012345678
                    self.table[0][i][0] = i
                    self.table[0][i][1] = 'd'
                    self.table[j][0][0] = j
                    self.table[j][0][1] = 'i'


            for j in range(len(self.table)-1): # 7 0123456
                for i in range(len(self.table[0])-1): # 9 012345678
                    if self.s1[i]==self.s2[j]:
                        self.table[j+1][i+1][0] = min(self.table[j][i][0],self.table[j+1][i][0],self.table[j][i+1][0])
                        self.table[j + 1][i + 1][1] = 'm'


                    if self.s1[i] != self.s2[j]:
                        corner = self.table[j][i]
                        left = self.table[j + 1][i]
                        up = self.table[j][i + 1]
                        if min(corner[0],left[0],up[0]) == corner[0]:
                            self.table[j + 1][i + 1][0] = corner[0] + 1
                            self.table[j + 1][i + 1][1] = 's'
                        elif min(corner[0], left[0], up[0]) == up[0]:
                            self.table[j + 1][i + 1][0] = up[0] +1
                            self.table[j + 1][i + 1][1] = 'i'
                        elif min(corner[0], left[0], up[0]) == left[0]:
                            self.table[j + 1][i + 1][0] = left[0] +1
                            self.table[j + 1][i + 1][1] = 'd'

            return self.table

    
    def __repr__(self):
        
        self.table[0].insert(0, '')
     
        
        for j,line in zip(range(len(self.s2)), range(1,len( self.table))):
       
           
            self.table[line].insert(0, self.s2[j])

        self.table.insert(0, list('  ')+ list(self.s1))
                    
        for line in self.table:
            for cell in line:
                print (cell, end="\t")
            print()


          
        return " ".format(self.table)

        
lt = LevenshteinTable('Saturday', 'Sunday')
lt2= LevenshteinTable('impopul', 'popu')
lt3= LevenshteinTable('abb', 'ab')
print(lt.distance())
print(lt.table)
print(lt)


print('\n')
print(lt2.distance())
print(lt2)
print(lt3)
