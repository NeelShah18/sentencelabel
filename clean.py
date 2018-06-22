import re
from textblob import TextBlob
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

#default setting for data cleaning
default_settings = {
	'to_upeer' : False,
	'to_lower' : False,
	'remove_special' : False,
	'remove_number' : False,
	'spelling_correction' : False,
	'remove_stopwords' : False,
	'remove_punchuation' : False, 

}

def clean_it(text, settings = default_settings):
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
	__text = str(text)
	try:
		if settings['to_upeer'] == True:
			__text = __text.upper()
		
		if settings['to_lower'] == True:
			__text = __text.lower()
		
		if settings['remove_special'] == True:
			__text = re.sub('[^A-Za-z0-9]+', ' ', __text)

		if settings['remove_number'] == True:
			__text = ''.join([__i for __i in __text if not __i.isdigit()])

		if settings['remove_stopwords'] == True:
			joiner = " "
			stop_words = set(stopwords.words('english'))
			word_tokens = word_tokenize(__text)
			filtered_sentence = [w for w in word_tokens if not w in stop_words]
			__text = joiner.join(filtered_sentence)

		if settings['remove_punchuation'] == True:
 			__pattern = re.compile('[%s]' % re.escape(string.punctuation))
 			__text = str(__pattern.sub('', __text))

		if settings['spelling_correction'] == True:
			__clean = TextBlob(__text)
			__text = __clean.correct()

	except Exception as e:
		print("Error wrong settings"+str(e))
		return __text

	return __text


def test():
	test_settings = {
	'to_upeer' : False,
	'to_lower' : True,
	'remove_special' : True,
	'remove_number' : False,
	'spelling_correction' : True,
	'remove_stopwords' : True,
	'remove_punchuation' : True, 
	}

	text = "“When will I ever use this?” you may have thought as you sat in that high-school English class. Now, all grown up, you find yourself writing far more than you ever would have expected."
	text = clean_it(text, test_settings)
	print(text)
	return None


if __name__ == '__main__':
	test()