#### Class 08
#### Some old and some new data types and tricks 

#pip install pandas
#pip install numpy
#pip install matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

## Pandas ----------------------------------------------------

## like a normal list
x = pd.Series([10, 100, 12, 5])
x[0]

## now columns and rows
## input can be lots of things
dt = { 'A' : 1.2, 'B' : [1,2,3], "C" : "hi"}
df_dictionary = pd.DataFrame(dt, columns = ["A", "B", "C"])
df_dictionary
df_dictionary.dtypes


l = [[1,2,3], [3,4,5], [7,8,9]]
df_lists = pd.DataFrame(l, columns = ["A", "B", "C"])
df_lists.index ## row names
df_lists.rename(index = {0:"One", 1:"Two", 2:"Three"})

ar = np.random.randn(6,4)
df_array = pd.DataFrame(ar, columns = ["A", "B", "C", "D"])



## helpful commands

df_array.head()
df_array.head(2)
df_array.tail()

df.columns

df.describe()

df.sort_values(by = "A")



## indexing

df["A"] ## column A

df["A"][0] ## column then row

df[0:4] ## first 4 rows

df.loc[:,["C"]] ## uses labels

df.loc[1:3:,["C"]]

df.at[1,"A"]

df.iloc[1:2, 1:2] ## uses integer positions

df.iloc[1:2, 1:2]

## a lot more.....



## Tuples ----------------------------------------------------


## Tuples are immutable

my_tuple = (1,'b',3,'d',5,'b')
my_tuple[1] = {'b':2}
my_tuple[0] ## element at index  0
my_tuple.index('b') ## Gives the index of 'b' - only the first occurence!
my_tuple.count('b') ## Gives the number of times 'b' occurs


## Lists ----------------------------------------------------


my_square_list=[]
for i in range(0,10):
	my_square_list.append(i**2)

## one line loop!
my_square_list = [i**2 for i in range(0,10)]

## map is like apply in R
## lambda creates an anonymous function
my_square_list = map((lambda x: x**2), range(0,10))

## another way
def sqr(x): return x**2

map(sqr, range(0,10))

## zip makes list of item-wise tuples
zipped = zip(my_list, my_square_list, map(lambda x: x**3, range(0,10)))
unzipped = zip(*zipped)

## filter
## returns elements only for which condition is True
filter(lambda x: x == 1, [1,2,3])

filter(lambda x: x < 0, range(-5, 5))


## .index and .count methods work the same as above

x = [3,6,1,2,8,3,5,7]

x.reverse() 
x[2]
x.sort() 
x.append(10)
x.extend(my_square_list)
x.insert(1,'+')
x.remove('+')  #Removes the first occurence '+'
x.remove(3)

## enumerate

import string

y = [3,1,2,5,2]
enumerate(y)
list(enumerate(y))

letters = list(string.lowercase)

## each item is a tuple
for item in enumerate(letters):
	print item

## iterate with elements of tuple
for number, letter in enumerate(letters):
	print "%s is the letter with index %s" %(letter,number)

## more generally, iterate like this with any tuple
for a, b, c in [(1, 2, 3)]:
	print a
	print b
	print c



## Dictionary ----------------------------------------------------

d = dict(zip(letters,range(1,27)))

d['a']
d.keys() #Don't expect order!
d.values() 
d.items()

for key, value in d.items():
	if value == 1:
		print key

for k, v in d.items():
	print "%s is the letter number %s" %(letter, number)

newletter = {'A': 27}
d.update(newletter)

new_a_value = {'a':'first'}
d.update(new_a_value)
d['z'] = 'last'



## Tree ----------------------------------------------------
## Our own data structure!

class Node():
	def __init__(self, value = None):
		self.value = value
		self.parent = None
		self.children = [None, None]			
		
	def __repr__(self):
		return "Node object with value %s" %(self.value)
		
	def __str__(self):
		if self.children != (None,None):
			return "Node value: %s \n left child: \n %s \n right child: \n %s" %(self.value,self.children[0],self.children[1])
		else: return "Node value: %s" %self.value	
	
class Tree():
	def __init__(self, root=None):
		self.root = root
		self.branches = [[root]]
		
	def add_branch(self, node, children):
		node.children = children
		for branch in self.branches:
			if branch[-1] == node:
				newbranch = branch + [children[0]]
				newbranch2 = branch + [children[1]]
				self.branches.append(newbranch)
				self.branches.append(newbranch2)
				self.branches.remove(branch)

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

mytree = Tree(node1)
mytree.branches
mytree.add_branch(node1,[node2,node3])
mytree.add_branch(node2,[node4,node5])




