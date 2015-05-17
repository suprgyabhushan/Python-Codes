#!/usr/bin/python

import string

class Dictionary:
	def __init__(self, words):
		self.root = dict()
		for word in words:
			current_dict = self.root
			for letter in word:	    	
				current_dict = current_dict.setdefault(letter, {})
			
		
  	

	def find_prefix(self, word):
		current_dict = self.root
		print current_dict
		for letter in word:
			if letter in current_dict:
				#current_dict = current_dict[letter]
				return True
			else:
				return False



if __name__ == "__main__":
	#students=['BACK', 'BAN', 'BAT', 'BIN','BINARY','BANTER','BRACKET','BRAG']
	dictionary = Dictionary("test1.txt")
	def t1():
		print dictionary.find_prefix("UR")
	t1()

