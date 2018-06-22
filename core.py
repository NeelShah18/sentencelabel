from getsenti import base_emoji, base_text
from clean import clean_it
from nltk import word_tokenize
from textblob import TextBlob

def get_sentiment(text="Sample text data! And I am positive :-)", on_base = "t", flag_prob=False):
	'''base_emoji return setiment of the tect based on emoji and emoticons in text.

Args:
	text (str): Setence of paragraph for calculating setiment.
	flag (boolean): True --> It gives 5 criteria 0,1,2,3,4 where 2(Nutral), 4(very positive), 1(very negative)
					False --> Gives probability with 2 floating point accuray between -1(negative) to 1(positive)

Returns:
	__prob_sentiment: If flag = True it will return number(int) between 0 to 4
					  If flag = False it will return nmber(float-2f) between -1 to 1

Defaults:
	text = "Sample text data! And I am positive :-)"
	on_base = "t"
	flag_prob = False

'''
	result = {}
	text = text
	on_base = on_base
	flag_prob = flag_prob
	if on_base == "e":
		result = base_emoji(text,flag_prob)
	elif on_base == "t":
		result = base_text(text, flag_prob)
	else:
		result = {error: "Choose right on_base, it must be e or t, wehere e = emoji and t = text."}

	return result

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

def do_clean(text, settings):
	'''clean_it function different type of text cleaning.

	Args:
		text(str): Text to ne cleaned.
		settings(dict): Dictonary of different type of settings.

	defaults: Here True flag means to do that things on given text.
		dettings : {
			'to_upeer' : False,
			'to_lower' : False,
			'remove_special' : False,
			'remove_number' : False,
			'spelling_correction' : False,
			'remove_stopwords' : False,
			'remove_punchuation' : False, 
		}
	'''
	return clean_it(text, settings)


def test():
	'''test fucntion for setencelabel library.
	'''
	test_data = "I love python 👨 :-)"
	result = get_sentiment(text=test_data, on_base='e', flag_prob=False)
	print(result)
	x = ngram("ever use may thought sat high school english class grown find writing far ever would expected",3)
	print(x)
	print(tokenizer("ever use may thought sat high school english class grown find writing far ever would expected"))
	return None

if __name__ == '__main__':
	test()