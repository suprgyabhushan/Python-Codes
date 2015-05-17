#!/usr/bin/python

import string


class Dictionary:
	global words_list
	words_list=[]
	global _end
 	_end = '_end_'
	def __init__(self, fileName):
		self.words=[]
		self.root=dict()
		fin = open(fileName, 'r')
		while(True):
			line = fin.readline()
			if(line == ''):
				break
			else:
				self.words.append(string.strip(line))
		words_list=self.words
		for word in words_list:
			current_dict=self.root
			for letter in word:
				current_dict=current_dict.setdefault(letter,{})
			current_dict = current_dict.setdefault(_end, _end)


	def __str__(self):
		s = ""
		for w in self.root:
			s += w +"\n" 
		return s	
	
				
	def findPrefix(self, word):
		current_dict=self.root
		print current_dict
		a=0
		for letter in word:
			if letter in current_dict:
				current_dict = current_dict[letter]
			else:
				a=1
		if(a==0):
			return True
		elif(a==1):
			return False
		
		
	


if __name__ == "__main__":
	dictionary=Dictionary("test1.txt")
	print dictionary
	#wordslist=[]
	#dictionary.give(wordslist)
	#def t1():
	#	print dictionary.findPrefix("Zur")
	#	print dictionary.findPrefix("zbcd")
	#t1()
	
	
	
