"""
Author: BIT Community

Description:

bitbot is a simple slack greetings bot developed by the BIT community
to help promote opensource and BIT code collaboration.

"""
from slackclient import SlackClient
from helpers import load_config

try:
    slack_config = load_config(get_settings="slack")
except:
    print("Problem loading config settings")

if slack_config:
    slack_token = slack_config['slack_token']
    introduction_channel_id = slack_config['introduction_channel_id']
    bot_user = slack_config['bot_user']
    greeting_message = slack_config['greeting_message']


def slack_client_connect():
    slack_client = SlackClient(slack_token)
    return slack_client


def slack_client_test():
     slack_client = slack_client_connect()
     print(slack_client.api_call('api.test'))
     print(slack_client.api_call('auth.test'))


def slack_post_message(message=None):
    slack_client = slack_client_connect()
    if message:
        post = slack_client.api_call("chat.postMessage", as_user="true:",
                                     channel=introduction_channel_id,
                                     text=message)
    else:
        post = "There was no message to send."
    return post


#slack_client_test()
#slack_post_message(message=greeting_message)


