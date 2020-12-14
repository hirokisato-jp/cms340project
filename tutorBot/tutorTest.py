#!/usr/bin/python3

################################################################################################################################
#  NAME:  Jenny Goldsher, Noah Harvey, Deandra Martin, Hiroki Sato
#  DATE:  03112020
#  IDEA:  this script will post a basic message to the slack channel #tutoring-Bot
################################################################################################################################

####  IMPORTS  #################################################################################################################

import slack

####  GLOBALS  #################################################################################################################

token = ""

####  FUNCTIONS  ###############################################################################################################

####  MAIN  ####################################################################################################################

def main():
    bot = slack.WebClient(token=token)
    bot.chat_postMessage(channel="#tutoring-bot",text="Hello World\nI come from tutorTest.py running on a cloud server!")

if(__name__=="__main__"): main()
