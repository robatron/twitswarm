# this is the configuration file for twitswarm

'''
Twitter API call-cycle duration.

How long between twitter API-call cycles in seconds? Note that we are
generally limited to 350 POST API calls per hour per user which means no 
more 1 call per 11 seconds or so.
'''
cycleDuration = 15
