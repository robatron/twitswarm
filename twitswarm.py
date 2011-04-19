#! /usr/bin/env python
'''
A distributed twitter bot platform.
'''

import time
import pickle
from twitter import oauth_dance, OAuth, Twitter
from twitter import TwitterHTTPError

from settings import *
import app_info

# temporary plugin imports (will eventually be handled by the plugin manager)
from plugin__hello_world import hello_world

def main():
    ''' Runs at program start '''
    try:
        ts = twitswarm()
        ts.start()
    except KeyboardInterrupt:
        ts.finish()
    exit(0)

class twitswarm:
    plugins = []
    twitter = None

    def __init__(self):
        print '--[twitswarm]----------'
        print 'Hello from Agent %s!'%TWITTER_USERNAME
        self.load_plugins()
        self.authenticate()

    def authenticate(self):
        print "Authenticating..."
        oauth = None
        try:
            oauth_file = open("oauth.dat", 'r')
            oauth = pickle.load(oauth_file)
        except IOError:
            print "Oauth file not found. Starting twitter oauth dance."
            try:
                token_key, token_secret = oauth_dance.oauth_dance(
                        app_info.APP_NAME, app_info.CONSUMER_KEY, 
                        app_info.CONSUMER_SECRET)
                oauth = OAuth(token_key, token_secret, app_info.CONSUMER_KEY, 
                        app_info.CONSUMER_SECRET)
                oauth_file = open("oauth.dat",'w')
                pickle.dump(oauth, oauth_file)
            except TwitterHTTPError:
                print "Authentication error!"
                self.finish(1)

        self.twitter = Twitter(auth=oauth)
        print "Authenticated!"

    def load_plugins(self):
        self.plugins.append(hello_world())

    def start(self):
        ''' Main program loop. '''
        print 'Starting main program loop. Press Ctrl+c to exit.'

        while True:
            for plugin in self.plugins:
                plugin.listen(self.twitter)

                # sleep for a bit as to not anger le twitters
                time.sleep(TWITTER_POLL_INTERVAL)

    def finish(self, status=0):
        print "\nAgent %s shutting down. Bye!"%TWITTER_USERNAME
        exit(status)

# Start twitswarm after the file's loaded
if __name__ == '__main__':
    main()
