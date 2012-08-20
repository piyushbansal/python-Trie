#!/usr/bin/env python
b=[]                              # A container that would hold suggestions 


class Trie():

    def __init__(self):
        self.root = {}
	self.val=0               # To store count of each character's occurance in a particular path
	self.depth=0             # depth of each character in a particular path

#--------------------------------------------------------------------------------------#
#            Internal Function that returns bool true if key exists in the trie        #
#		and false otherwise , along with the count , it occurs                 # 

    def __contains__(self, word):
	word=word+'$'
        curr_node = self.root
	no=len(word)
        for char in word:
	    no-=1
            try:
		if no==0:
		      return [True,curr_node[word[-1]].val]
                curr_node = curr_node[char].root
            except KeyError:
                return [False,0]
	if None in curr_node:
	       return [True,curr_node[word[-1]].val]
	else :
	       return [False,0]

#----------------------------------------------------------------------------------------#
#         Internal Function to insert a word into the trie 			         #

    def __add__(self, word):
	word=word+'$'
        curr_node = self.root
	no=len(word)
	counter=0
        for char in word:
		counter+=1
		try:
			curr_node[char].val+=1
			curr_node[char].depth=counter
			curr_node = curr_node[char].root
	   	except KeyError:
			curr_node[char] = Trie()
                	curr_node[char].val+=1
			curr_node[char].depth=counter
                	curr_node = curr_node[char].root
        curr_node[None] = word

#---------------------------------------------------------------------------------------#

    def update(self, words):
#              A Function to update tree with multiple words at once                    #
        for word in words:
            self.add(word)

   
#---------------------------------------------------------------------------------------#
#           Internal Function to print trie in indented form (calls ptrie)              #

    def __ptrie__(self):
	    temp = self.root.keys()
	    temp.sort()
	    for i in temp :
		    if(i!=None):
			    indent=self.root[i].depth
			    print '| '*indent+i
			    curr_node=self.root[i]
			    if(len(curr_node.root)!=0):
				    curr_node.__ptrie__()

#---------------------------------------------------------------------------------------#
# 			Internal functions for remove operation                         #

    def __reduces__(self, word):
	word=word+'$'
        curr_node = self.root
        for char in word:
		try:
			if(curr_node[char].val>0):
				curr_node[char].val-=1
			curr_node = curr_node[char].root
	   	except KeyError:
			return -1
        curr_node[None] = word 


    def __initdel__(self,key):
	self.__deletes__(key+'$')


    def __deletes__(self,key):
	head = key[0]
	if head in self.root:
		try:
	    		node=self.root[head]
	    	except KeyError:
	    		return 'Not Found'
	if len(key)>1:
		remains=key[1:]
	    	node.__deletes__(remains)
	if node.val==0 :
		del self.root[head]

#----------------------------------------------------------------------------------------------#
#                Internal Functions for obtaining suggestions                                  #

    a=[]
    def __collectsuggestions__(self,word):
	    for char in self.root.keys():
		    if self.root[char].root.has_key('$') :
		    	    self.a.append(word+char)
		#	    print self.a
		    if char !=None and char !='$':
		    	    self.root[char].__collectsuggestions__(word+char)
	    return self.a

    def __suggests__(self,key,x=''):
	    global b
	    head=key[0]
	    x=x+head
	    if head in self.root:
			    curr_node=self.root[head]
			    if len(key)>1:
		    		    curr_node.__suggests__(key[1:],x)
			    else :
				  b=curr_node.__collectsuggestions__(x)

#--------------------------------------------------------------------------------------------#
#                      Functions intended to be called by user                               #

    def insert(self,word):
	    self.__add__(word)
	    print str(self.__contains__(word)[1])


    def remove(self,word):
	    if self.__contains__(word)[0]:
	    	self.__reduces__(word)
	    	self.__initdel__(word)
		print self.__contains__(word)[1]
	    else :
		print -1


    def ptrie(self):
	    print 'root'
	    self.__ptrie__()


    def search(self,word):
	counter=0
	global b
	length=len(b)
	a= self.__contains__(word)
	if a[0]:
		print 'true'+' '+str(a[1])
	else :
		self.__suggests__(word)
		print 'false',
		for word in b:
			print word +' '+str(self.__contains__(word)[1]),
		print ''

#--------------------------------------------------------------------------------------------------#

if __name__=="__main__":
	t=Trie()
	testcases=input()
	while testcases:
		testcases-=1
		string=raw_input()
		if len(string)>1:
			command=string.split()
			if command[0]=='insert':
				t.insert(command[1])
			if command[0]=='search':
				t.search(command[1])
			if command[0]=='remove':
				t.remove(command[1])
			if command[0]=='ptrie':
				t.ptrie()


