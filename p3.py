def KMPSearch(pat, txt):
	'''
 	KMPSearch finds a pattern (pat) within large texts (txt).
 	'''
	M = len(pat)
	N = len(txt)

	# create lps[] that will hold the longest prefix suffix
	# values for pattern
	lps = [0]*M
	j = 0 # index for pat[]

	# Preprocess the pattern (calculate lps[] array)
	computeLPSArray(pat, M, lps)

	i = 0 # index for txt[]
	found=[]
	while (N - i) >= (M - j):
		if pat[j] == txt[i]:
			i += 1
			j += 1

		if j == M:
			#print("Found pattern at index " + str(i-j))
			found.append(i-j)
			j = lps[j-1]

		# mismatch after j matches
		elif i < N and pat[j] != txt[i]:
			# Do not match lps[0..lps[j-1]] characters,
			# they will match anyway
			if j != 0:
				j = lps[j-1]
			else:
				i += 1
	return found


# computeLPSArray is used to compute the LPS array
def computeLPSArray(pat, M, lps):
	len = 0 # length of the previous longest prefix suffix

	lps[0] = 0 # lps[0] is always 0
	i = 1

	# the loop calculates lps[i] for i = 1 to M-1
	while i < M:
		if pat[i] == pat[len]:
			len += 1
			lps[i] = len
			i += 1
		else:
			# This is tricky. Consider the example.
			# AAACAAAA and i = 7. The idea is similar
			# to search step.
			if len != 0:
				len = lps[len-1]

				# Also, note that we do not increment i here
			else:
				lps[i] = 0
				i += 1
#pattern_search searches the pattern over a string of text
def pattern_search(pat,txt):
	a = KMPSearch(pat, txt)  #O(2n) en el peor caso
	if len(a)!=2:
		return False
	if a[0]==0 and a[1]==len(txt)-len(pat) and pat!=txt:
		return True
	else:
		return False


def find_substrings(txt):
	'''
 	find_substrings find the substrings inside a given string of text
 	'''
	subcadenas = []
	for x in txt:
		if len(subcadenas)!=0:
			subcadenas.append(subcadenas[-1]+x)
		else:
			subcadenas.append(x)
	'''Como se quiere la subcadena que sea prefijo
	entonces se consideran las subcadenas desde 0 a n unicamente,
	si la subcadena no incluye el elemento 0 no seria prefija'''
	p_s = []
	for x in set(subcadenas): #O(1)
		p = pattern_search(x,txt) #O(n)
		if p==True:
			p_s.append(x)

	maximum,substring = 0,""
	for x in p_s: #O(n)
		if len(x) > maximum:
			substring = x 
			maximum = len(x)
	return(substring)

txt = input("Introduce a string: ")
sub = find_substrings(txt)
print("The maximum substring that is prefix, suffix and different to",txt,"is '",sub,"'")

