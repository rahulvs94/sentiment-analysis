# sentiment analysis

Project 1: Sentiment analysis on tweets using Twitter API
	
	- Basic implementation of sentiment analysis on tweets made by number of users 
	- Output positive/negative sentiment of the filtered tweets (default = 15)
	- Vary the number of search result by changing count parameter in search API 
	- Can provid list of arguments in the search field, 
		eg. python sentiment_analysis_twitter.py "Virat Kohli" "Rohit Sharma"
	
Usage: python sentiment_analysis_twitter.py "<name>"
		   
Requirement: Twitter account, Tweepy, TextBlob


Project 2: Sentiment analysis on movie data

	- Refine the movie data for fitting into vectorize form
	- Output sentiment analysis of movie data using Logistic Regression and SVM
	- Also trained with LSTM, CNN1D, EMbedded layer
	- Effect of removing stop words, stemming, lemmatization, n-grams, term-frequency and inverse data-frequency (TF-IDF) analyzed 
	- Lowering the numbers in tuple for n-grams increases the size of dictionary as well as time to fit the model

Usage: Run the cells to see results


Kaggle Kernel: 
	https://www.kaggle.com/rahulvs94/hyperparameter-tuning-sklearn-keras-talos?scriptVersionId=11680199
