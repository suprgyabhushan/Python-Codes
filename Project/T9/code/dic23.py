#!/usr/bin/python

import string
import tree2 as T

class Dictionary:
	
	
	def __init__(self, fileName):
		self.words=[]
		#self.root=dict()
		fin = open(fileName, 'r')
		while(True):
			line = fin.readline()
			if(line == ''):
				break
			else:
				self.words.append(string.strip(line))
	def suffix(self):
		for word in self.words:
			par=T.makeTree(word[0],[],None)
			for i in range(1,len(word)):
				T.addSubtree(word[i],word[i+1])
					
			
					
			#for letter in word:
			#	current_dict=current_dict.get(letter,{})
	'''def printsuffix(self):
		current_dict=self.root
		return current_dict			
	def findPrefix(self, word):
		current_dict=self.root
		
		a=0
		for letter in word:
			if letter in current_dict:
				current_dict = current_dict[letter]
			else:
				a=1
		if(a==0):
			return True
		elif(a==1):
			return False'''
		
		
	


if __name__ == "__main__":
	dictionary=Dictionary("test1.txt")
	print dictionary.suffix()
	'''def t1():
		print dictionary.findPrefix("Zur")
		print dictionary.findPrefix("zbcd")
		print dictionary.findPrefix("abea")
	t1()'''
	
	
	
