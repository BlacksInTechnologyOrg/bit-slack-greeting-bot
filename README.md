BiT Slack Bot Project

The Blacks-In-Technology (BiT) group is working on a SlackBot project! Let's get
some minds together and add some functionality to the [Blacks-In-Technology Slack](http://blacksintechnology.slack.com)
rooms.

## Status

Right now we're at the very beginning of the project, where platform decisions and
requirements are beign hammered out. We've discussed using [Given-When-Then](https://en.wikipedia.org/wiki/Given-When-Then) to describe desired features and [Python](https://www.python.org/) as the development language.

## Installation

Clone repo

```
 git clone git@github.com:BlacksInTechnologyOrg/bit-slack-greeting-bot.git
```

Install python requirments

```
  cd bit-slack-greeting-bot
  pip install -r requirements.txt
```

Create config.yml

```
 cp config.example.yml config.yml

```

Update config settings

````yaml
slack:
  token: <token>
  bot_user: <bot user>
  channels:
    chanel1: <chanel1 id>
    channe2: <channel2 id>
  messages:
    greeting_message: |
                      Hi, I'm bitbot :bitlogo: . This is our first community coding project!
                      Join in on the fun!
                      Hack all the things :neckbeard:!
                      Drink all the :beer:!
    another_message: |
                     A differnt message to post.`
````

## Usage

```
python bitbot.py
```

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## History

TODO: Write history

## Credits

TODO: Write credits

## License

BiT Slack Bot Project is using the [MIT License (MIT)](LICENSE.txt).
