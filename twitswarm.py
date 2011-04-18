#! /usr/bin/env python
'''
A distributed twitter bot platform.
'''

import time
from twitter import oauth_dance, OAuth, Twitter
from twitter import TwitterHTTPError

from settings import *
import app_info

# temporary plugin imports (will eventually be handled by the plugin manager)
from plugin__hello_world import hello_world

plugins = []
leTwitter = None

def main():
    ''' Runs at program start '''
    print '-------------------'
    print ' T W I T S W A R M '
    print '-------------------'
    print 'Hello from Agent %s!'%TWITTER_USERNAME
    load_plugins()
    authenticate()
    start()
    exit(0)

def authenticate():
    print "Authenticating with twitswarm. Follow directions in browser."
    print "--"
    try:
        token_key, token_secret = oauth_dance.oauth_dance(app_info.APP_NAME, 
                app_info.CONSUMER_KEY, app_info.CONSUMER_SECRET)
        oauth = OAuth(token_key, token_secret, app_info.CONSUMER_KEY, 
                app_info.CONSUMER_SECRET)
        leTwitter = Twitter(auth=oauth)
    except TwitterHTTPError:
        print "Authentication error!"
        byebye(1)
    except KeyboardInterrupt:
        byebye()
    print "--"
    print "Authenticated!"

def load_plugins():
    plugins.append(hello_world())

def start():
    ''' Main program loop. '''
    print 'Starting main program loop. Press Ctrl+c to exit.'

    while True:
        try:
            for plugin in plugins:

                # listen for each plugin's registered listeners
                for listener_spec in plugin.listeners:
                    listen_for(listener_spec['search_query'], 
                            listener_spec['handler'])

                # sleep for a bit to respect the twitter API's rate limiting
                time.sleep(TWITTER_POLL_INTERVAL)
        # quit on Ctrl+c
        except KeyboardInterrupt:
            byebye()

def listen_for(query, handler):
    print 'Performing search on ``%s``, calling ``%s`` on matched results'\
            %(query,handler.__name__)
    print leTwitter.search(q=query)


def byebye(status=0):
    print "\nAgent %s shutting down. Bye!"%TWITTER_USERNAME
    exit(status)

if __name__ == '__main__':
    main()

