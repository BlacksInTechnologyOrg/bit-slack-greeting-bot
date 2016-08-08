"""
Description:
Helper functions
"""

import yaml


def load_config(get_settings=None):
    """
    Description:
    loads config.yml
    settings should be passed in as a dictionary.
    get_settings = { 'settings for': [ 'setting1', 'setting2', 'setting3', {'setting_key': 'setting_value'} ] }
    """
    config = dict()

    if not get_settings:
        return "Please specify what settings you would like to parse"

    try:
        open_config = yaml.load(open('config.yml'))
    except:
        print("Could not load Config file.")

    for settings in get_settings:
        settings_list = [x for x in get_settings[settings]]
        for setting in settings_list:
            try:
                if isinstance(setting, dict):
                    key = (', '.join(setting.keys()))
                    value = (', '.join(setting.values()))
                    config[value] = open_config[settings][key][value]
                else:
                    config[setting] = open_config[settings][setting]
            except:
                print "Issue loading {0} in config.yml".format(setting)
    return config
