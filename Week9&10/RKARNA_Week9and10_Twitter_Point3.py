'''
DSC540-T301 Data Preparation (2215-1)
Purpose of Program:  Connect to the Twitter API and do a simple data pull -- Week 9 & 10: Point-3 Excercise
Author: Rajasekharreddy Karna
Date: 05/22/2021
'''

import os
import tweepy as tw
import pandas as pd

consumer_key='2mJTguWuPZ1x33Tiq3KMdOiaC'
consumer_secret='4a1b9sStVDbSNNe0lQAsQbIP8PAsr0ORgrzkYFV6HCjq8MQ5L1'
access_token='1396037029104812041-46NlcxJTBHmFXCYiiyaGpOjO2WjLd6'
access_token_secret='dFY7Tmq3SoWVwQZyFNCXoRPhWrrvLs8vXR6gUp3eXFJze'

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

# Send Tweet
# Post a tweet from Python
api.update_status("Look, I'm tweeting from Bellevue University class")

# Define the search term and the date_since date as variables
search_words = "Bellevue University"
date_since = "2021-01-01"

# Collect tweets
tweets = tw.Cursor(api.search,
              q=search_words,
              lang="en",
              since=date_since).items(5)
tweets
