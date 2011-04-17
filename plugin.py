'''
The twitswarm base plugin module.
'''

from io import send, listen

class base_plugin:
    '''
    The twitswarm base plugin class definition. All plugins will need to extend
    this.
    '''

    # create instances of the ``send`` and ``listen`` IO classes
    listen = listen()
    send = send()

