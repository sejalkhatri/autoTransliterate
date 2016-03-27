import json
import sys
mapping = json.load(open('autoTransliterate/mapping.json'))

vowels = ['a', 'aa', 'ai', 'au', 'e', 'ee', 'hri', 'hru', 'i', 'o', 'oo', 'ri', 'ru', 'u']
consonents = ['b', 'bh', 'c', 'ch', 'chh', 'd', 'dh', 'f', 'g', 'gh', 'h', 'j'	, 'jh', 'k', 'kh', 'l', 'm', 'n', 'p', 'ph', 'q', 'r', 's', 'sh', 't', 'th', 'v', 'w', 'x', 'y', 'z']

def filter(splits):
	# splits is a list of partitions so effectively is list of list of consonents union vowels defined above
	# example splits for 'shahana' is: [[u'sh', u'a', u'h', u'a', u'n', u'a'], [u's', u'h', u'a', u'h', u'a', u'n', u'a']] 
	a1 = []
	print 'splits are', splits

	for s0 in splits:
		rep_flag = True
		for i1, s1 in enumerate(s0):
			if (s0[i1-1] == 's' and s1 == 'h') or (s0[i1-1] == 't' and s1 == 'h') or (s0[i1-1] == 'c' and s1 == 'h') or (s0[i1-1] == 'k' and s1 == 'h'):
				rep_flag = False
				break
		if rep_flag == False:
			splits.remove(s0)

	print 'splits after', splits

	for s0 in splits:
		# s0 is a particular partitions from the splits
		# so s0 can be [u'sh', u'a', u'h', u'a', u'n', u'a'] for 'shahana'
		prev_vow = []
		prev_cons = []
		# prev_cons and prev_vowels are going to be temporary lists containing 	list of possible mappings
		# of previously occured vowel/consonent (descibed above) in the order of occurence
		# example: for ['s', 'h', ...] prev_cons was: [[u'\u0938', u'\u0938\u094d'], [u'\u0939']]
		a0 = []
		iterator = 0

		if s0[0] in vowels:
			if len(mapping[s0[0]]) == 2:
				prev_vow.append([(mapping[s0[0]])[0]])
			else: prev_vow.append([(mapping[s0[0]])[0], (mapping[s0[0]])[2]])	
			iterator = 1

		for i1, s1 in enumerate(s0[iterator:]):
				#try:
				if s1 in vowels and len(prev_cons) != 0:
					for s2 in prev_cons[-1]:
						if s2[-1] == u'\u094d':
							print 'removing', s2, 'from', prev_cons[-1]
							prev_cons[-1].remove(s2)
					a0 += prev_cons
					prev_cons = []
					if len(mapping[s1]) == 2:
						prev_vow.append([(mapping[s1])[1]])
					else: prev_vow.append([(mapping[s1])[1], (mapping[s1])[3]])

				elif s1 in consonents and len(prev_vow) != 0:
					a0 += prev_vow
					prev_vow = []
					if s1 in ['m', 'n']:
						if (i1 == 1 and s0[0] in vowels) or (s0[i1-1] in vowels and s0[i1-2] in consonents):
							prev_cons.append(mapping[s1][:])
						else: prev_cons.append((mapping[s1])[:-1])
					else: prev_cons.append(mapping[s1][:])

				elif s1 in vowels and len(prev_vow) != 0:
					if len(mapping[s1]) == 2:
						prev_vow.append([(mapping[s1])[0]])
					else: prev_vow.append([(mapping[s1])[0], (mapping[s1])[2]])

				else:
					if s1 in ['m', 'n']:
						prev_cons.append(mapping[s1][:-1])
					else: prev_cons.append(mapping[s1][:])
				#except IndexError, ie:
				#	print 'IndexError at',s1


		if prev_vow != []:
			a0 += prev_vow

		elif prev_cons != []:
			for s2 in prev_cons[-1]:
				if s2[-1] == u'\u094d':
					prev_cons[-1].remove(s2)
			a0 += prev_cons

		a1.append(a0)

	return a1
