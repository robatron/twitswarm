'''
The twitswarm base plugin module.
'''

class base_plugin:
    '''
    The twitswarm base plugin class definition. All plugins will need to extend
    this.
    '''

    # A list of listeners to call 
    listeners = []

    def register_listener(self, search_query, handler_function):
        print 'Registering tweet listener for search query ``%s``'%search_query
        self.listeners.append({
            'search_query':search_query, 
            'handler':handler_function
        })

