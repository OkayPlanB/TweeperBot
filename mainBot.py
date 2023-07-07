#Import required libraries
import os
import random
import tweepy

#Create API client with keys
client = tweepy.Client(consumer_key='Enter Your API Key Here',
                       consumer_secret='Enter Your API Secret Here',
                       access_token='Enter Your Access Token Here',
                       access_token_secret='Enter Your Access Secret Here')

#Define text file and temp file
original_file = 'dummyList.txt'
temp_file = 'temp.txt'

#Opens list file
with open("dummyList.txt", "r") as file:
    allText = file.read()
    words = list(map(str, allText.splitlines()))

#Randomly picks line from list and defines tweet       
tweet = random.choice(words) 

#Posts tweet
response = client.create_tweet(text=tweet)

#Removes tweeted line from file as saves as temp.txt
with open(original_file, 'r') as input:
    with open(temp_file, 'w') as output:
        for line in input:
            output.write(line.replace(tweet, ""))

#Closes the main and temp file from the script
input.close()
output.close()

#Replaces original file with updated list after tweet
os.replace('temp.txt', 'dummyList.txt')
