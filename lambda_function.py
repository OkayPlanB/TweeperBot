import json
import os
import random
import tweepy

#Create API client with keys
client = tweepy.Client(consumer_key='Enter Your API Key Here',
                       consumer_secret='Enter Your API Secret Here',
                       access_token='Enter Your Access Token Here',
                       access_token_secret='Enter Your Access Secret Here')

#Define text file
original_file = 'dummyList.txt'

#Opens list file
with open(original_file, "r") as file:
    allText = file.read()
    words = list(map(str, allText.splitlines()))

#Randomly picks word from list and builds tweet        
tweet = random.choice(words) 

#Posts tweet
response = client.create_tweet(text=tweet)

#Required callback for Lambda
def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
