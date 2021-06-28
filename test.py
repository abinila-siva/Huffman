import unittest

from huffman import encode, decode

class TestHuffman(unittest.TestCase):
	
	def test_1_E1(self):

		input_file = 'encrypt_txt1.txt'
		output_file = 'encrypt_res1.txt'
		encryp_file = open(input_file,'w+')
		input = 'abinila'
		outType = '0111010111100001'
		encryp_file.write(input)
		encryp_file.close()
		encode(input_file, output_file)
		output_file = open(output_file,'r')
		output = output_file.readlines()
		isValid = (output[0]==outType)
		self.assertTrue(isValid)

	def test_2_D1(self):
		
		input_file = 'encrypt_res1.txt'
		output_file = 'decryp_res1.txt'
		decode(input_file, output_file)
		f_decode = open(output_file,'r')
		output = f_decode.readlines()
		outType = 'abinila'
		isValid = (output[0]==outType)
		self.assertTrue(isValid)
   
	def test_3_E2(self):

		input_file = 'encryp_txt2.txt'
		output_file = 'encryp_res2.txt'
		encryp_file = open(input_file,'w+')
		input = 'ABINILA'
		outType = '0111010111100001'
		encryp_file.write(input)
		encryp_file.close()
		encode(input_file, output_file)
		output_file = open(output_file,'r')
		output = output_file.readlines()
		isValid = (output[0]==outType)
		self.assertTrue(isValid)


	def test_4_D2(self):
		
		input_file = 'encryp_res2.txt'
		output_file = 'Dec_res2.txt'
		decode(input_file, output_file)
		f_decode = open(output_file,'r')
		output = f_decode.readlines()
		outType = 'ABINILA'
		isValid = (output[0]==outType)
		self.assertTrue(isValid)
		
	def test_5_E3(self):

		input_file = 'encryp_txt3.txt'
		output_file = 'encryp_res3.txt'
		encryp_file = open(input_file,'w+')
		input = '12345abcd'
		outType = '11101111000001010011100101110'
		encryp_file.write(input)
		encryp_file.close()
		encode(input_file, output_file)
		output_file = open(output_file,'r')
		output = output_file.readlines()
		isValid = (output[0]==outType)
		self.assertTrue(isValid)


	def test_6_D3(self):
		input_file = 'encryp_res3.txt'
		output_file = 'Dec_res3.txt'
		decode(input_file, output_file)
		f_decode = open(output_file,'r')
		output = f_decode.readlines()
		outType = '12345abcd'
		isValid = (output[0]==outType)
		self.assertTrue(isValid)



if __name__ == '__main__':
	unittest.main()