sentencelabel
===============================

#### Open source to label the test data based on setiment. We also adding functioanlity such as text is realted to which area(for example food, politics, education etc).

This library is all in one solution for data cleaning, labeling and converting in n-gram or tokens for future processing.

Below is basic function of sentencelabel library. (It is still in development and new feature will be add.) Please create new issue for new functioanlity you want. 

**get_sentiment** gives the setiment of the text. It gives option to analysis the text based on emoji and emoticons together or only text. You can also choose type of output you need for setiment
of the test. It will be float between -1 to 1 where -1 to extrem negative to 1 extrem postive, 0 consider as nutral. You also chose the integer(criteria based sentiment) between 0 to 4.
where 0 in extrem negative, 1 is negative, 2 in nutral, 3 in positive, 4 in extrem positive.

**Note: If you choose emoji and emoticond base and you don't have emoji or emoticons in text it will do sentiment analysis on text.**


```
get_sentiment return setiment of the text, emoji and emoticons in text.

Args:
	text (str): Setence of paragraph for calculating setiment.
	on_base(charater): 't' for text sentitement and 'e' for emoji ant emoticons sentiment
	flag (boolean): True --> It gives 5 criteria 0,1,2,3,4 where 2(Nutral), 4(very positive), 1(very negative)
					False --> Gives probability with 2 floating point accuray between -1(negative) to 1(positive)

Returns:
	__prob_sentiment: If flag = True it will return number(int) between 0 to 4
					  If flag = False it will return nmber(float-2f) between -1 to 1

Defaults:
	text = "Sample text data! And I am positive :-)"
	on_base = "t"
	flag_prob = False
```

code example:
```python
>>> text = "I love python :-) why not"
>>> sentencelabel.get_sentiment(text=text, on_base='e', flag_prob=False)
0.8
>>> sentencelabel.get_sentiment(text=text, on_base='e', flag_prob=True)
4
>>> sentencelabel.get_sentiment(text=text, on_base='t', flag_prob=False)
0.5
>>> sentencelabel.get_sentiment(text=text, on_base='t', flag_prob=True)
3

```

**ngram** function convert any text to n-gram formate as we want. here gram in gram jumber we want.

```
ngram function convert test to n-gram

	Args:
		text(str): Text to convert in n-gram
		gram(int): Number of n-gram
	
	Results:
		__gram_model(list(list)): return list of list depends on n-gram input

	Defaults:
		gram = 2
```

code example:
```python
>>> text = "I love python :-) why not"
>>> sentencelabel.ngram(text=text, gram=2) #2-gram
[WordList(['I', 'love']), WordList(['love', 'python']), WordList(['python', 'why']), WordList(['why', 'not'])]
>>> sentencelabel.ngram(text=text, gram=3) #3-gram
[WordList(['I', 'love', 'python']), WordList(['love', 'python', 'why']), WordList(['python', 'why', 'not'])]
>>> sentencelabel.ngram(text=text, gram=4) #4=gram
[WordList(['I', 'love', 'python', 'why']), WordList(['love', 'python', 'why', 'not'])]
>>> sentencelabel.ngram(text=text, gram=5) #5-gram
[WordList(['I', 'love', 'python', 'why', 'not'])]

```

**tokenizer** convert given text into tokens

```
tokenizer return tokens of the text.

	Args:
		text(str): Text to convert in tokens

	Results:
		__tokens(list): List of tokens of given text
```

code example:
```python
>>> text = "I love python :-) why not"
>>> sentencelabel.tokenizer(text=text)
['I', 'love', 'python', ':', '-', ')', 'why', 'not']

```

**do_clean** funciton provide cleaning of the text. Their are multiple option are avilable you can chose from uppercase, lowercase, spelling correction, stop words remobe, punchuation remove, special cahrter remove. In future we are adding more function to this library. 

```
do_clean function different type of text cleaning.

	Args:
		text(str): Text to ne cleaned.
		settings(dict): Dictonary of different type of settings.

	defaults: Here True flag means to do that things on given text.
		default_settings : {
			'to_upper' : False, #True convert all text to uppercase
			'to_lower' : False, #True convert all text to lower case
			'remove_special' : False, #True will remove special charaters from text
			'remove_number' : False, #True will remove digits from text
			'spelling_correction' : False, #True will correct the spelling in text
			'remove_stopwords' : False, #True will remove stop words from text
			'remove_punchuation' : False, #True will remove punchuation from text
		}
```

```python
>>> text = "“When will I ever use this?” you may have thought as you sat in that high-school English class. Now, all grown up, you find yourself writing far more than you ever would have expected."
>>> test_settings = {
...     'to_upper' : False,
...     'to_lower' : True,
...     'remove_special' : True,
...     'remove_number' : False,
...     'spelling_correction' : True,
...     'remove_stopwords' : True,
...     'remove_punchuation' : True, 
...     }
>>> sentencelabel.do_clean(text, test_settings)
'ever use may thought sat high school english class grown find writing far ever would expected'

```
