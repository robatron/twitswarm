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
            'god',
            self.hello_world_responder 
        )

    def hello_world_responder(self, tweet):
        ''' Responder for "Hello world!" tweets '''
        print "This is the hello_world_responder! Here's the tweet I got: %s"\
                %tweet['text']

