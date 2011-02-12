'''
Plugin interface to twitswarm for the plugins.
'''

# --------
# senders
# --------

def send(msg, toUser=None, toGroup=None):
    '''
    Update this agent's status with ``msg``. Optionally, provide a list of 
    twitter usernames to @mention. Set ``toGroup`` to "True" to send to
    include the group's hash tag.
    '''
    pass

def autoSend(msg, interval, toUser=None, toGroup=None):
    ''' auto-send messages at the specified ``interval`` '''
    pass

def sendDirect(msg, toUser):
    ''' send a direct message to a user '''
    pass

# ----------
# listeners
# ----------

def listenFor(msgPattern, onFeed, handler):
    ''' 
    Listen for the regex pattern ``msgPattern`` on the feed ``onFeed``
    and call the handler function ``handler`` when the message is found.
    The matched tweet will be passed to the handler function.
    '''
    pass

def waitFor(msgPattern, onFeed):
    '''
    Block execution and wait for a regex pattern ``msgPattern`` on feed 
    ``onFeed`` at which point, return with the tweet.
    '''
    pass

