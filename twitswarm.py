#! /usr/bin/env python
'''
A distributed twitter bot platform.
'''

from settings import *
import time

# temporary plugin imports (will eventually be handled by the plugin manager)
from plugin__hello_world import hello_world

def main():
    ''' Runs at program start '''
    print '-------------------'
    print ' T W I T S W A R M '
    print '-------------------'
    print 'Hello from Agent %s!'%TWITTER_USERNAME
    print "Please check back later :)"
    dealWithPluginsOrWhatever()
    start()
    exit(0)

def dealWithPluginsOrWhatever():
    plugins = []
    plugins.append(hello_world())

def start():
    ''' Main program loop. '''
    while True:
        try:
            time.sleep(10000)
        except KeyboardInterrupt:
            print "\nAgent %s shutting down. Bye!"%TWITTER_USERNAME
            break 

if __name__ == '__main__':
    main()

