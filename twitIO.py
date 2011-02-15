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
    def now(self, msg, toUser=None, toGroup=None):
        '''
        Update this agent's status with ``msg``. Optionally, provide a list of 
        twitter usernames to @mention. Set ``toGroup`` to "True" to send to
        include the group's hash tag.
        '''
        pass

    def auto(self, msg, interval, toUser=None, toGroup=None):
        ''' auto-send messages at the specified ``interval`` '''
        pass

    def direct(self,msg, toUser):
        ''' send a direct message to a user '''
        pass

# -------
# listen
# -------
class listen(object):
    def listen(self,  msgPattern, onFeed, handler):
        ''' 
        Listen for the regex pattern ``msgPattern`` on the feed ``onFeed``
        and call the handler function ``handler`` when the message is found.
        The matched tweet will be passed to the handler function.
        '''
        handler("hello")

    def waitFor(self, msgPattern, onFeed):
        '''
        Block execution and wait for a regex pattern ``msgPattern`` on feed 
        ``onFeed`` at which point, return with the tweet.
        '''
        pass

