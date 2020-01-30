import hashlib

def main():
	wordlist = openWordList()
	print("lkajsdfl")
	l1 =["taco","blue","yess"]
	l2 = secondRuleWord("*~!#", l1)
	print(l2)
	flist = firstRuleWord(wordlist)
	for word in flist:
		print(word)

def openWordList():
	wl = open('/usr/share/dict/words', 'r')
	wordlist = wl.readlines()
	wl.close()
	for i in range(len(wordlist)):
		wordlist[i] = wordlist[i].decode('utf-8')
		wordlist[i] = wordlist[i].replace('\r', '').replace('\n', '')
		wordlist[i] = wordlist[i].title()
		#print(len(wordlist[i]))
	return wordlist

"""
input: a string(word) to be hashed
output: the sha256 hexidecimal hash of word  
"""
def hasher(word):
	return hashlib.sha256(word).hexdigest()
	
	
	

"""
Input: a digit from 0-9, wordlist from /usr/share/dict/words
Output: a list of seven letter words with the given special number appended at the end
"""
def firstRuleWord(wordlist):
	newlist = []
	for j in range(10):
		for i in range(len(wordlist)):
			#print(wordlist[i] + " " + str(len(wordlist[i])))
			if(len(wordlist[i]) == 7):
				newlist.append(wordlist[i] + str(j))
	return newlist
			

"""
input:	specialchars: a string of all the special chars added to a word
	wordlist: a list of 4 letters of words to append to each special character
output: the list of all the words with the special characters prepended
"""
def secondRuleWord(specialChars, wordlist):

	newlist = []
	for word in range(len(wordlist)):
		for char in specialChars:
			newlist.append(str(wordlist[word]) + str(word))
		# end character loop
	# end word loop	
	return newlist
	


main()
