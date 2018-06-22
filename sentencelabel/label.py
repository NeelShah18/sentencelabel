from textblob import TextBlob
import emot

def base_emoji(text, flag):
	'''base_emoji return setiment of the tect based on emoji and emoticons in text.

	Args:
		text (str): Setence of paragraph for calculating setiment.
		flag (boolean): True --> It gives 5 criteria 0,1,2,3,4 where 2(Nutral), 4(very positive), 1(very negative)
						False --> Gives probability with 2 floating point accuray between -1(negative) to 1(positive)
	
	Returns:
		__prob_sentiment: If flag = True it will return number(int) between 0 to 4
						  If flag = False it will return nmber(float-2f) between -1 to 1

	'''
	#convert input to string
	text = str(text)
	__temp_emoji = emot.emoji(text)
	__temp_emoti = emot.emoticons(text)
	__pre_final_text = ""

	#Finding emoji and emoticons from text
	if __temp_emoji[0]['flag'] == True:
		for data in __temp_emoji:
			__pre_final_text = str(data['mean'])+" "
			print(__pre_final_text)
	if __temp_emoti['flag'] == True:
		for data in __temp_emoti['mean']:
			__pre_final_text = str(data)+" "
			print(__pre_final_text)
	if len(__pre_final_text) < 2:
		__pre_final_text = text

	__analysis = TextBlob(__pre_final_text)

	#choosing output formate of sentiment based on flag
	if flag == False:
		__prob_sentiment = __analysis.sentiment.polarity
	else:
		__prob_sentiment = get_solid_setiment(__analysis.sentiment.polarity)

	return __prob_sentiment

def base_text(text, flag):
	__analysis = TextBlob(text)
	if flag == False:
		__prob_sentiment = __analysis.sentiment.polarity
	else:
		__prob_sentiment = get_solid_setiment(__analysis.sentiment.polarity)

	return __prob_sentiment

def get_solid_setiment(__prob_sentiment):
	__solid_setiment = 2
	__prob_sentiment = __analysis.sentiment.polarity
	if __prob_sentiment <= -0.5:
		__solid_setiment	= 0
	elif __prob_sentiment <= -0.99 and __prob_sentiment > -0.5:
		__prob_sentiment = 1
	elif __prob_sentiment <= 0.5 and __prob_sentiment >= 0.1:
		__solid_setiment = 3
	elif __prob_sentiment <= 1 and __prob_sentiment > 0.5:
		__solid_setiment = 4
	elif __prob_sentiment == 0:
		__solid_setiment = 2
	else:
		__solid_setiment = 2	
	
	return __solid_setiment

class get_label(objecct):

	def __init__(self):
		self.__text = "Sample text data! And I am positive :-)"
		self.__on_base = "text"
		self.__flag_prob = False
	
	def get_label(self, text, on_base = "t", flag_prob=False):
		self.result = {}
		self.__text = text
		self.__on_base = on_base
		self.__flag_prob = flag_prob
		if __on_base == "e":
			result = base_emoji(self.text, self.flag_prob)
		elif __on_base == "t":
			result = base_text(self.text, self.flag_prob)
		else:
			result = {error: "Choose right on_base, it must be e or t, wehere e = emoji and t = text."}

		return result

def test():
	'''
	It is test function of current file: label.py
	'''
	x = base_emoji("I love python 👨 :-)", False)
	print(x)
	return None

if __name__ == '__main__':
	test()