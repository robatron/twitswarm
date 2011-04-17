'''
Application plugin interface to twitswarm for the plugins.
'''

# -----------------
# feed definitions
# -----------------
class feeds:
    ''' Define the twitter feed types '''
    ALL = 0
    FRIENDS = 1
    USER = 2
    DIRECT = 3

# -----
# send
# -----
class send:
    def now(self, msg, toUsers=None, toSwarm=False):
        '''
        Update this agent's status with ``msg``. 
        
        Optionally, provide a list of twitter usernames to @mention in the
        ``toUsers`` parameter. Also, set ``toSwarm`` to "True" to inclue the
        swarm's hash tag in the message.
        '''
        pass

    def auto(self, messasge, interval, toUsers=None, toSwarm=False):
        ''' 
        Register a ``message`` to auto-send at the specified ``interval``.
        
        Optionally, provide a list of twitter usernames in ``toUsers`` to send
        the message to, and/or set ``toSwarm`` to "True" to include the swarm's
        hash tag in the message.
        '''
        pass

    def direct(self, msg, user):
        ''' send a direct ``message`` to the specified ``user``. '''
        pass

# -------
# listen
# -------
class listen(object):
    def listen(self,  msgPattern, onFeed, handler):
        ''' 
        Register a regex pattern ``msgPattern`` to listen for on the feed 
        ``onFeed`` and call the handler function ``handler`` when the message 
        is matched. 
        
        The matched tweet will be passed to the handler function.
        '''
        handler("hello")

    def waitFor(self, msgPattern, onFeed):
        '''
        Block execution and wait for a regex pattern ``msgPattern`` on feed 
        ``onFeed`` at which point, return with the tweet.
        '''
        pass

