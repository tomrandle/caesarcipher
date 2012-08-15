clearText = 'Prince Andrew, seeing that his father insisted, began- at first reluctantly, but gradually with more and more animation, and from habit changing unconsciously from Russian to French as he went on- to explain the plan of operation for the coming campaign. He explained how an army, ninety thousand strong, was to threaten Prussia so as to bring her out of her neutrality and draw her into the war; how part of that army was to join some Swedish forces at Stralsund; how two hundred and twenty thousand Austrians, with a hundred thousand Russians, were to operate in Italy and on the Rhine; how fifty' 
cipherText = ""

key = 2 #Caesar shift offset
textBlockSize = 5 #How to group letters
lettersRemoved = 0

upperclearText = clearText.upper()

for index, ch in enumerate(upperclearText):

	clearAsciiCharacter =  ord(ch)

	if (90 - 26) < clearAsciiCharacter <= 90 :
		cipherAsciiCharacter = clearAsciiCharacter + key

		if cipherAsciiCharacter > 90:
			cipherAsciiCharacter -= 26
		
		cipherCharacter = chr(cipherAsciiCharacter)

		if (index - lettersRemoved) % textBlockSize == textBlockSize - 1:
			cipherCharacter +=" "

	else:
		cipherCharacter = ""
		lettersRemoved += 1

	cipherText += cipherCharacter

print "*" * 20
print "CLEAR TEXT"
print "*" * 20
print upperclearText
print "*" * 20
print "CIPHER TEXT"
print "*" * 20
print cipherText