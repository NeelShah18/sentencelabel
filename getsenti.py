from textblob import TextBlob
import emot

def base_emoji(text, flag):
	'''base_emoji return setiment of the text based on emoji and emoticons in text.

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
	if __temp_emoji['flag'] == True:
		for data in __temp_emoji['mean']:
			__pre_final_text = str(__pre_final_text) + str(data)+" "
			
	if __temp_emoti['flag'] == True:
		for data in __temp_emoti['mean']:
			__pre_final_text = str(__pre_final_text) + str(data)+" "
			
	if len(__pre_final_text) < 2:
		__pre_final_text = text

	__analysis = TextBlob(__pre_final_text)

	#choosing output formate of sentiment based on flag
	if flag == False:
		__prob_sentiment = round(__analysis.sentiment.polarity, 4)
	else:
		__prob_sentiment = get_solid_setiment(__analysis.sentiment.polarity)

	return __prob_sentiment

def base_text(text, flag):
	'''base_text return setiment of the text based on given text.

	Args:
		text (str): Setence of paragraph for calculating setiment.
		flag (boolean): True --> It gives 5 criteria 0,1,2,3,4 where 2(Nutral), 4(very positive), 1(very negative)
						False --> Gives probability with 2 floating point accuray between -1(negative) to 1(positive)
	
	Returns:
		__prob_sentiment: If flag = True it will return number(int) between 0 to 4
						  If flag = False it will return nmber(float-2f) between -1 to 1

	'''
	__analysis = TextBlob(text)
	if flag == False:
		__prob_sentiment = round(__analysis.sentiment.polarity, 4)
	else:
		__prob_sentiment = get_solid_setiment(__analysis.sentiment.polarity)

	return __prob_sentiment

def get_solid_setiment(__prob_sentiment):
	'''get_solid_setiment return setiment in 5 criteria between 0 to 4.

	Args:
		__prob_sentiment(float): Sentiment of text in floating.
		
	Returns:
		__solid_sentiment: Integer value between 0(very negative) to 4(very positive).

	'''
	__solid_setiment = 2
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

if __name__ == '__main__':
	test()