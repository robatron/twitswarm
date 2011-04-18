#! /usr/bin/env python
'''
A distributed twitter bot platform.
'''

import time
import json
from twitter import oauth_dance, OAuth, Twitter
from twitter import TwitterHTTPError

from settings import *
import app_info

# temporary plugin imports (will eventually be handled by the plugin manager)
from plugin__hello_world import hello_world

def main():
    ''' Runs at program start '''
    ts = twitswarm()
    ts.start()
    exit(0)

class twitswarm:
    plugins = []
    twitter = None
    test_val = None   

    def __init__(self):
        print '--[twitswarm]----------'
        print 'Hello from Agent %s!'%TWITTER_USERNAME
        self.load_plugins()
        self.authenticate()

    def authenticate(self):
        print "Starting authentication dance:"
        print "--"

        try:
            token_key, token_secret = oauth_dance.oauth_dance(
                    app_info.APP_NAME, app_info.CONSUMER_KEY, 
                    app_info.CONSUMER_SECRET)
            oauth = OAuth(token_key, token_secret, app_info.CONSUMER_KEY, 
                    app_info.CONSUMER_SECRET)
            self.twitter = Twitter(auth=oauth)
        except TwitterHTTPError:
            print "Authentication error!"
            self.finish(1)
        except KeyboardInterrupt:
            self.finish()

        print "--"
        print "Authenticated!"

    def load_plugins(self):
        self.plugins.append(hello_world())

    def start(self):
        ''' Main program loop. '''
        print 'Starting main program loop. Press Ctrl+c to exit.'

        while True:
            try:
                for plugin in self.plugins:

                    # listen for each plugin's registered listeners
                    for listener_spec in plugin.listeners:
                        self.look_for(listener_spec['search_query'], 
                                listener_spec['handler'])

                    # sleep for a bit as to not anger le twitters
                    time.sleep(TWITTER_POLL_INTERVAL)

            # quit on Ctrl+c
            except KeyboardInterrupt:
                self.finish()

    def look_for(self, query, handler):
        print 'Performing search on ``%s``, calling ``%s`` on matched results'\
                %(query,handler.__name__)
        print json.dumps(self.twitter.search(q=query), indent=4)


    def finish(self, status=0):
        print "\nAgent %s shutting down. Bye!"%TWITTER_USERNAME
        exit(status)

if __name__ == '__main__':
    main()

