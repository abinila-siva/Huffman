import sys
import argparse
import shutil
from collections import Counter

results='-'

class node:
    def __init__(self, frequency, literal, left=None, right=None):
        self.frequency = frequency
        self.literal = literal
        self.left = left
        self.right = right
        self.huff = ''
 
def save_char(literal,results,fileName,code):
	fil = open(fileName,'a')
	if code==False:
		fil.write(results)
	else:
		fil.write(results+':'+f'{literal}'+'\n')
 
def printNodes(node, key,fileName,code,val=''):
    new_val = val + str(node.huff)
    if(node.left):
        printNodes(node.left, key,fileName,code, new_val)
    if(node.right):
        printNodes(node.right,key,fileName,code, new_val)
    if(not node.left and not node.right and node.literal == key):
        results = new_val
        save_char(node.literal, results,fileName,code)
   	    
        	

def encode(fin, fout):
	print("Encoding Starts", fin, fout)
	f_in = open(fin,'r')
	f_out = open(fout,'w+')
	f_out.write('')
	content = str(f_in.read())
	frequency = dict(Counter(content))	
	keys = list(frequency.keys())
	frequency = list(frequency.values())
	nodes = []
	 
	for x in range(len(keys)):
	    nodes.append(node(frequency[x], keys[x]))
	 
	while len(nodes) > 1:
	    nodes = sorted(nodes, key=lambda x: x.frequency)	 
	    left = nodes[0]
	    right = nodes[1]	 
	    left.huff = 0
	    right.huff = 1
	    newNode = node(left.frequency+right.frequency, left.literal+right.literal, left, right)
	    nodes.remove(left)
	    nodes.remove(right)
	    nodes.append(newNode)
	
	for char in content:
		printNodes(nodes[0],key=char,fileName=fout,code=False)

	print("Encoding Done")

	file_code = open('code.txt','w+')

	for char in keys:
		printNodes(nodes[0],key=char,fileName='code.txt',code=True)

	print("Code is stored..")


def decode(fin, fout):
	print("Decoding Started", fin, fout)
	
	file_code = open('code.txt','r')
	dictionary = {}
	codes = file_code.readlines()
	
	for code in codes:
		if ':' in code:
			item = code.split(':')
			key = item[0]

			if len(item[1])==1:
				value = item[1]
			else:
				value = item[1].replace('\n','')

			dictionary[key] = value

	f_content = open(fin,'r')
	f_decoded = open(fout,'w+')

	content = f_content.readlines()
	output = ''
	
	code = ''
	for char in content[0]:
		code += char

		if code in dictionary.keys():
			output+=dictionary[code]
			code=''

	f_decoded.write(output)	

	print("Decoding Done")


def get_options(args=sys.argv[1:]):
	parser = argparse.ArgumentParser(description="Huffman compression.")
	groups = parser.add_mutually_exclusive_group(required=True)
	groups.add_argument("-e", type=str, help="Encode files")
	groups.add_argument("-d", type=str, help="Decode files")
	parser.add_argument("-o", type=str, help="Write encoded/decoded file", required=True)
	options = parser.parse_args()
	return options


if __name__ == "__main__":
	options = get_options()
	if options.e is not None:
		encode(options.e, options.o)
	if options.d is not None:
		decode(options.d, options.o)
