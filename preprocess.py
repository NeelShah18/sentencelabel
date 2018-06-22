from textblob import TextBlob
from nltk import word_tokenize

def ngram(text, gram=2):
	'''convert test to n-gram

	Args:
		text(str): Text to convert in n-gram
		gram(int): Number of n-gram
	
	Results:
		__gram_model(list(list)): return list of list depends on n-gram input

	Defaults:
		gram = 2

	'''
	__analyzer = TextBlob(str(text)) 
	return __analyzer.ngrams(n=gram)

def tokenizer(text):
	'''tokenizer return tokens of the text.

	Args:
		text(str): Text to convert in tokens

	Results:
		__tokens(list): List of tokens of given text

	'''
	return word_tokenize(str(text))


def test():
	x = ngram("ever use may thought sat high school english class grown find writing far ever would expected",3)
	print(x)
	print(tokenizer("ever use may thought sat high school english class grown find writing far ever would expected"))
	return None

if __name__ == '__main__':
	test()