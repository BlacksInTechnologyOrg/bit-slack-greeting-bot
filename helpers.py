"""
Definition:
Helper function
"""

import yaml


def load_config(get_settings=None):
    """
    Load config.yml
    """
    config = dict()

    if not get_settings:
        return "Please specify what settings you would like to parse"

    try:
        load_config = yaml.load(open('config.yml'))
    except:
        return "Could not load Config file."
    try:
        config['slack_token'] = load_config[get_settings]['token']
    except:
        return "Issue loading token in config.yml"
    try:
        config['bot_user'] = load_config[get_settings]['bot_user']
    except:
        return "Issue loading bot_user name in config.yml"
    try:
        config['introduction_channel_id'] = load_config[get_settings]['introduction_channel_id']
    except:
        return "Issue loading introduction_channel_id in config.yml"
    try:
        config['greeting_message'] = load_config[get_settings]['greeting_message']
    except:
        return "Issue loading slack message"

    return config
