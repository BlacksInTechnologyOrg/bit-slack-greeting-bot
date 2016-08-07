"""
Author: BIT Community

Description:

bitbot is a simple slack greetings bot developed by the BIT community
to help promote opensource and BIT code collaboration.

"""
import time
from slackclient import SlackClient
from helpers import load_config

slack_settings = dict()
slack_settings['slack'] = ['slack_token', {'channels': 'introduction'}, 'bot_user', {'messages': 'greeting_message'}]


try:
    slack_config = load_config(get_settings=slack_settings)
except:
    print("Problem loading config settings")

if slack_config:
    slack_token = slack_config['slack_token']
    introduction_channel_id = slack_config['introduction']
    bot_user = slack_config['bot_user']
    greeting_message = slack_config['greeting_message']
else:
    exit()


def slack_client_connect():
    try:
        slack_client = SlackClient(slack_token)
    except:
        slack_client = False
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


def slack_event_parser(output):
    output_list = output
    if output_list and len(output_list) > 0:
        for output in output_list:
            #print(output['text'], output['channel'])
            return output

#slack_client_test()

if __name__ == "__main__":
    slack_client = slack_client_connect()
    socket_delay = 1
    if slack_client.rtm_connect():
        print("BITBOT is connected to Slack")
        while True:
            output = slack_event_parser(slack_client.rtm_read())
            if output['type'] == 'team_join':
                slack_post_message(message=greeting_message)
            time.sleep(socket_delay)
    else:
        print("Could not connect to slack. Check your token or network connection.")
