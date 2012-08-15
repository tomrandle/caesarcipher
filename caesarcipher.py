

rawtext = 'Prince Andrew, seeing that his father insisted, began- at first reluctantly, but gradually with more and more animation, and from habit changing unconsciously from Russian to French as he went on- to explain the plan of operation for the coming campaign. He explained how an army, ninety thousand strong, was to threaten Prussia so as to bring her out of her neutrality and draw her into the war; how part of that army was to join some Swedish forces at Stralsund; how two hundred and twenty thousand Austrians, with a hundred thousand Russians, were to operate in Italy and on the Rhine; how fifty' 

uppertext = rawtext.upper()
print uppertext

key = 2
codedMessage = ""
textblocksize = 5

for index, ch in enumerate(uppertext):

	asciicharacter =  ord(ch)

	if (90 - 26) < asciicharacter <= 90 :
		asciicodedcharacter = asciicharacter + key

		if asciicodedcharacter > 90:
			asciicodedcharacter -= 26

		codedcharacter = chr(asciicodedcharacter)

	else:
		codedcharacter = "" 

	
	if index % textblocksize == 0:
		codedcharacter += " "
	
	codedMessage += codedcharacter

print "The coded message is:", codedMessage