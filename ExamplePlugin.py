'''
An example plugin that listens for "Hello world!" and responds to the sender 
with "'sup".
'''

from twit_plugin import base_plugin, feeds

class plugin__hello_world(base_plugin):
    def __init__(self):
        '''Initialize this example plugin.'''

        # register a listener for 'hello world'
        self.listen.listen(
            r'Hello world!',            # regex of what to listen for
            feeds.ALL,                  # what feed to listen on
            self.hello_world_responder  # function to call when it matches 
        )

    def hello_world_responder(self, tweet):
        ''' Responder for "Hello world!" tweets '''
        print tweet

