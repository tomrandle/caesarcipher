

inputText = "the quick brown fox jumps over the lazy dog"
upperInputText = inputText.upper()

letterFrequencies = [0] * 26


for index, ch in enumerate(upperInputText):

	currentAsciiCharacter =  ord(ch)

	if (90 - 26) < currentAsciiCharacter <= 90 : #Only count letters
		letterFrequencies[currentAsciiCharacter - 90] += 1 


print letterFrequencies



