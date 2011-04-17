#! /usr/bin/env python
'''
A distributed twitter bot platform.
'''

from plugin__hello_world import hello_world

def main():
    ''' Runs at program start '''
    print '-------------------'
    print ' T W I T S W A R M '
    print '-------------------'
    print "This totally isn't implemented at all yet."
    print "Please check back later :)"
    dealWithPluginsOrWhatever()
    exit(0)

def dealWithPluginsOrWhatever():
    plugins = []
    plugins.append(hello_world())

# run main once everything's loaded
if __name__ == '__main__':
    main()
