def build_last(pattern):
	#don't forget to fill unexisting character of the text with -1
	last = {}
	length = len(pattern)
	for i in range(length):
		last[pattern[i]] = i

	return last

def boyer_moore(pattern, text):

	last = build_last(pattern)
	for i in text:
		if i not in last:
			last[i] = -1

	matching_position = []

	n = len(pattern)
	m = len(text)
	if n > m:
		return -1

	start = 0
	while start <= (m-n):
		j = n-1

		while (j >= 0) and (pattern[j] == text[j+start]):
			j -= 1

		if j < 0:
			matching_position.append(start)
			if (start+n) < m:
				start += n - last[text[start+n]]
			else:
				start += 1
		else:
			start += max(1, j - last[text[start + j]])

	return matching_position