# code to generate the list if required
from Queue import *
from autoTransliterate.langs_filter import *

class NonAlphabetException(Exception):
	"""
	raised when buffer contains non-alphabet value
	"""
	def __init__(self, value, pos):
		"""
		value   : non-alphabet value captured
		pos     : position index in the buffer
		"""
		self.value = value
		self.pos = pos

	def __str__(self):
		return 'Exception at: '+ str(self.pos) + ' non-alphabet ' + (self.value) + ' caught'

def generate(buff):
	""" 
	function to generate the list from buffer
	
	raises  : NonAlphabetException if buffer contains non-alphabet literals
	return  : list containing possible groups
	"""
	# convert to lower case
	print 'buffer is', buff
	buff = buff.lower()
	# queue for breadth first match :P
	q = Queue()
	q.put(([], buff))

	splits = []
	while not q.empty():
		a = q.get()
		NonAlpha = True
		# dict.keys() generates list of keys of dict
		for x in mapping.keys():
			# thanks to the awesome library
			if a[1].startswith(x):
				NonAlpha = False

				na0 = (a[0])[:]
				na0.append(x)
				na1 = (a[1])[len(x):]
				# match till string get exhausted
				if na1 != '':
					q.put((na0, na1))
				else:
					splits.append(na0)

		if NonAlpha is True:
			raise NonAlphabetException((a[1])[0], len(buff)-len(a[1]))

	print 'splits in list_generator', splits

	splits = filter(splits)

	finalList = []
	for s0 in splits:
		t0 = s0[0]
		for t1 in s0[1:]:
			t2 = []
			for u0 in t0:
				for u1 in t1:
					t2.append(u0+u1)
			t0[:] = t2[:]
		finalList += t0

	del buff

	return finalList

