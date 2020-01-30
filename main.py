import hashlib



def openWordList():
	wl = open('/usr/share/dict/words', 'r')
	wordlist = wl.readlines()
	wl.close()
	return wordlist

"""
Input: a digit from 0-9, wordlist from /usr/share/dict/words
Output: a list of seven letter words with the given special number appended at the end
"""
def hasher(word):
	return hashlib.sha256(word).hexdigest()
#def firstRuleWord(specialNum, wordlist):
	

def main():
	wordlist = openWordList()
	print("lkajsdfl")
	hashed = hashlib.sha256()
	print(hasher("taco"))
	
	



main()
