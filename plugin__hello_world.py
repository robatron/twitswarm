'''
An example plugin that listens for "Hello world!" and responds to the sender 
with "'sup".
'''

from plugin import base_plugin
from io import feeds

class hello_world(base_plugin):

    def __init__(self):
        '''Initialize this example plugin.'''

        # register a listener for 'hello world'
        self.register_listener(
            #'Hello world!',            
            'lol',
            self.hello_world_responder 
        )

    def hello_world_responder(self, tweet, twitter):
        ''' Responder for "Hello world!" tweets '''
        #twitter.statuses.update(status="Hi there, @%s!"%tweet['from_user'],
        #        in_reply_to_status_id=tweet['id'])

