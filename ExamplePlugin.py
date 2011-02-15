'''
Example plugin

Just messing around. No real functionality yet! Attempting to use all of the
API functions.
'''

from twitswarm import feeds, tweet
from twitswarm.plugins import plugin, api

class ExamplePlugin(plugin):
    def __init__(self):
        ''' initialize '''

        api.listenFor(
            r"Hello world!",    # regex of what to listen for
            feeds.ALL,          # what feed to listen on
            helloWorldResponder # function to call when it matches 
        )

    def helloWorldResponder(self, tweet):
        ''' Responder for "Hello world!" tweets '''
        api.send("'Sup.", tweet.username)

