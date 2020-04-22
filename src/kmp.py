def prefix_function(pattern):
	length = len(pattern)
	prefix = [0 for i in range(length)]
	for i in range(1,length):
		j = prefix[i-1]
		while (j>0 and pattern[i]!=pattern[j]):
			j = prefix[j-1]
		if pattern[i] == pattern[j]:
			j += 1
		prefix[i] = j
	return prefix

def kmp(pattern, text):
	#Change null_char to character not appearing in the text
	NULL_CHAR = '#'
	n = len(pattern)
	m = len(text)
	meta_text = pattern + NULL_CHAR + text

	prefix_meta = prefix_function(meta_text)
	matching_position = []

	for i in range(n+1, len(prefix_meta)):
		if prefix_meta[i] == n:
			matching_position.append(i-2*n)

	return matching_position