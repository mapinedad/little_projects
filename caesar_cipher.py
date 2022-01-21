class CaesarCipher:
	"""Class for doing encryption and decryption using a Caesar Cipher."""

	def __init__(self, shift):
		"""Construct Caesar Cipher using given integer shift for rotation."""
		self._forward = ''.join([chr((k + shift) % 26 + ord('A')) for k in range(26)])
		self._backward = ''.join([chr((k - shift) % 26 + ord('A')) for k in range(26)])

	def encrypt(self, message):
		"""Return string representing encripted message."""
		return self._transform(message, self._forward)

	def decrypt(self, secret):
		"""Return decrypted message given encrypted secret."""
		return self._transform(secret, self._backward)

	def _transform(self, original, code):
		"""Utility to perform transformation based on given code string."""
		msg = list(original)
		for k in range(len(msg)):
			if msg[k].isupper():
				j = ord(msg[k]) - ord('A')	# index from 0 to 25
				msg[k] = code[j]	# replace this character
		return ''.join(msg)


if __name__ == '__main__':
	
	cipher = CaesarCipher(6)
	
	message = """Lists, tuples, and strings in Python are one-dimensional. We use a single index to
				access each element of the sequence. Many computer applications involve multidimensional
				data sets. For example, computer graphics are often modeled in either two or three dimensions.
				Geographic information may be naturally represented
				in two dimensions, medical imaging may provide three-dimensional scans
				of a patient, and a company’s valuation is often based upon a high number of independent
				financial measures that can be modeled as multidimensional data. A
				two-dimensional array is sometimes also called a matrix. We may use two indices,
				say i and j, to refer to the cells in the matrix. The first index usually refers to a
				row number and the second to a column number, and these are traditionally zeroindexed
				in computer science. Figure 5.22 illustrates a two-dimensional data set
				with integer values. This data might, for example, represent the number of stores
				in various regions of Manhattan.""".upper()
	
	coded = cipher.encrypt(message)
	
	decoded = cipher.decrypt(coded)
	
	print("Codified message: ", coded, "\n", "Message decoded: ", decoded)
