# TweeperBot

This is a very simple bot that reads text from a file and posts a tweet, then removes the line from the file so it doesn't get posted again. This uses the Tweepy library for Twitter API intergration.
You will have to set up a developer account with Twitter to get the required keys to use this bot. Once your keys are added, you can use the dummyList file provided which has 50 random quotes simply for testing and demo, or you can edit the code to pull from your own text file.

This code is the barebones version of 2 Twitter bots currently running: [Rocket Discourse Bot](https://twitter.com/RocketDiscourse) and [Shuttle Discourse Bot](https://twitter.com/STSDerivedBot)
These both are currently on AWS Lambda and are set to post every hour.


# Tweepy Library

The Tweepy library is required to use this code, and can be found at https://www.tweepy.org/


# AWS Lambda Release


This is a version of the code created specifically to run on the AWS Lambda service. This will read text from a file but not edit the file of what lines were used, allowing for different combinations of lines. You will have to install a layer with all require python libraries to use this.
