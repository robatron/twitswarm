'''
Example plugin

Just messing around. No real functionality yet! Attempting to use all of the
API functions.
'''

from twitIO import feeds, listen

class ExamplePlugin():
    def __init__(self, a):
        ''' initialize '''

        self.listen = listen()

        self.listen.listen(
            r"Hello world!",    # regex of what to listen for
            feeds.ALL,          # what feed to listen on
            self.helloWorldResponder # function to call when it matches 
        )

    def helloWorldResponder(self, tweet):
        ''' Responder for "Hello world!" tweets '''
        print tweet

