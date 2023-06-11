import string

def get_fixation(word):
	fixfact = 1.6
	stripped = word.translate(str.maketrans("","", string.punctuation))
	fixation = int(len(stripped)/fixfact)
	if fixation == 0: fixation = 1
	return fixation


def bionify_word(word):
	if 'http' in word:
		bionic_word = word

	elif '-' in word:
		l = len(word.split("-"))

		if l <= 2:
			part_a, part_b = word.split('-')
				
			part_a_fixation = get_fixation(part_a)
			part_a = f"<b>{part_a[:part_a_fixation]}</b>{part_a[part_a_fixation:]}"
			
			part_b_fixation = get_fixation(part_b)		
			part_b = f"<b>{part_b[:part_b_fixation]}</b>{part_b[part_b_fixation:]}"
			bionic_word = f"{part_a}-{part_b}"
		
		else: bionic_word = word
		
	else:
		fixation = get_fixation(word)
			
		bionic_word = f"<b>{word[:fixation]}</b>{word[fixation:]}"
	
	return bionic_word


def bionic_main(str):
	newstr = ""

	data = str.split()
		
	for word in data:
		bw = bionify_word(word)
		newstr += bw + " "
	
	return newstr 
