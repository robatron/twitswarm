'''
Input/output objects for twitswarm.
'''

class feeds:
    ''' Define the twiter feed types '''
    ALL = 0
    FRIENDS = 1
    USER = 2
    DIRECT = 3

class send:
    ''' Functions relating to sending tweets/messages. '''

    def now(self, message, to_users=None, to_swarm=False):
        '''
        Update this agent's status with ``message``. 
        
        Optionally, provide a list of twitter usernames to @mention in the
        ``to_users`` parameter, and/or set ``to_swarm`` to "True" to
        include the swarm's hash tag in the message.
        '''
        pass

    def auto(self, messasge, interval, to_users=None, to_swarm=False):
        ''' 
        Register a ``message`` to auto-send at the specified ``interval``.
        
        Optionally, provide a list of twitter usernames in ``to_users`` to 
        send the message to, and/or set ``to_swarm`` to "True" to include 
        the swarm's hash tag in the message.
        '''
        pass

    def direct(self, message, to_users):
        ''' send a direct ``message`` to the specified list of users in
        ``to_user``. '''
        pass

class listen:
    ''' Functions relating to recieving/listening for tweets/messages. '''

    def register(self,  msg_pattern, on_feed, handler):
        ''' 
        Register a regex pattern ``msg_pattern`` to listen for on the feed 
        ``on_feed`` and call the handler function ``handler`` when the 
        message is matched.
        
        The matched tweet will be passed to the handler function.
        '''
        print 'Listening for pattern %r on feed %s'%(msg_pattern, on_feed)
        pass


    def waitFor(self, msg_pattern, on_feed):
        '''
        Block execution and wait for a regex pattern ``msg_pattern`` on 
        feed ``on_feed`` at which point, return with the tweet.
        '''
        pass

