import xml.etree.ElementTree as Et
import codecs
import os.path

def search(search_string):
	ret_dict = {}

	for word in root.findall('word'):
		if word.attrib['name'] == search_string:
			for trans in word.findall('transliteration'):
				ret_dict[trans.text] = int(trans.attrib['freq'])

	return sorted(ret_dict.keys(), key = lambda x: ret_dict[x], reverse=True)

def update_string(word, trans):
	kf = False              		# key found

	for key in root.findall('word'):
		if key.attrib['name'] == word:
			kf = True 
			kfvn = False  			# key found value not

			for val in key.findall('transliteration'):
				if val.text == trans:
					freq = int(val.attrib['freq'])+1
					val.attrib['freq'] = str(freq)
					kfvn = True
		
			if kfvn == False:
				new_trans = Et.Element('transliteration', {'freq':'1'})
				new_trans.text = trans
				key.append(new_trans)

	if kf == False:
		child = Et.Element('word', {'name': word})
		sub_child = Et.Element('transliteration', {'freq':'1'})
		sub_child.text = trans
		child.append(sub_child)
		root.append(child)

	Et.ElementTree(root).write('transliteration.xml', encoding='UTF-8')

def data_begin():
	global tree
	global root
	if os.path.isfile('transliteration.xml'):
		pass
	else:
		temp = Et.ElementTree(Et.Element('data'))
		temp.write('transliteration.xml')
		del temp
	tree = Et.parse('transliteration.xml')
	root = tree.getroot()

if __name__ == '__main__':
	data_begin()