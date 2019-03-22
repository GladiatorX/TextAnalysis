import sys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Sample application to demonstrate the use of textblob library for sentiment analysis
#on stream of #hastag twitter data accessed via api request

non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd) #INORDER TO PROCESS EMOJIS

ACCESS_TOKEN = #YOUR_ACCESS_TOKEN
ACCESS_SECRET = #YOUR_ACCESS_SECRET
CONSUMER_KEY = #YOUR_CONSUMER_KEY
CONSUMER_SECRET = #YOUR_CONSUMER_SECRET

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)

#print(api.me().name)
query=#olease enter desiered hastag string here
Search_Result = api.search(query,count=30)

lstTweets_ = []
lstlPolarity_ = []
for tweet in Search_Result:
    lTweets_ =tweet.text.translate(non_bmp_map) #processing emoji translate function
    analysis = TextBlob(lTweets_)
    lPolarity_ = analysis.sentiment.polarity
    #can create positive n negative polarity plot bar chart
    lstTweets_.append(lTweets_)
    lstlPolarity_.append(lPolarity_)


df = pd.DataFrame(
    {'Tweets': lstTweets_,
     'Polarity': lstlPolarity_,
     })
df.to_csv('sentiment.csv')

plt.axis([0,70,0,1])
plt.xlabel('Time')
plt.ylabel('sentiment')
plt.plot(lstlPolarity_,'go')
plt.show()
