from textblob import TextBlob
import tweepy
import re
import pprint
import sys


#Authentication via API app

auth = tweepy.OAuthHandler('w1z4mskpHBbRYIuzQOoGtzQan', 'GkxjpNVpvuQWAm8pCwuLYovGwSfq1zItL2PtjZTIY1mYvqOJxQ')
auth.set_access_token('208155192-7ShX8v9AuvT0GqsBpHMQaNrPsyC3TuZdPH1nA6C9',
                              'Z279T5RxOakDbvsKD5acs4vPOLIHu9MDX1e7dfoHolD6t')
api = tweepy.API(auth)

search_term = 'Elden Ring AND elden ring'

tweet_amount = 2000

tweets = tweepy.Cursor(api.search_tweets, q=search_term, lang='en').items(tweet_amount)

# establish ref. point for subjectivity and polarity @ 0, same for the positive, negative and neutral count

polarity = 0
subjectivity = 0

positive = 0
negative = 0
neutral = 0

# If to display the tweet and score, empty dictionary for the tweets: key is tweet, arg is polarity score

positives = {}
negatives = {}
neutrals = {}



for tweet in tweets:

    # Cleaning the tweets
    final_text = tweet.text.replace('RT', '')
    final_text = re.sub(r"http\S+", "", final_text)
    final_text = re.sub('#[A-Za-z0-9]+', '', final_text)
    final_text = re.sub('\\n', '', final_text)

    #start analysis of tweets using textblob
    analysis = TextBlob(final_text)

    if analysis.polarity > 0:
        positive += 1
        positives[final_text] = analysis.polarity
    elif analysis.polarity < 0:
        negative += 1
        negatives[final_text] = analysis.polarity
    else:
        neutral += 1
        neutrals[final_text] = analysis.polarity

    polarity += analysis.polarity
    subjectivity += analysis.subjectivity

print(f'The overall polarity is {polarity}, with a subjectivity score of {subjectivity}')
print(f'nr of positive tweets= {positive}')
print(f'nr of negative tweets= {negative}')
print(f'nr of neutral tweets= {neutral}')

pprint.pprint(f'these are the positives and score:\n {positives}')

pprint.pprint(f'these are the negatives and score:\n {negatives}')

