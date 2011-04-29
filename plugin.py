'''
The twitswarm base plugin module.
'''

import json
from datetime import datetime

class base_plugin:
    '''
    The twitswarm base plugin class definition. All plugins extend this
    '''

    # A list of listeners to listen for
    listeners = []

    class listener:
        def __init__(self, search_query, handler):
            self.search_query = search_query
            self.handler = handler
            self.since_id = 0

    def register_listener(self, search_query, handler_function):
        print 'Registering tweet listener for search query ``%s``'%search_query
        self.listeners.append(self.listener(search_query, handler_function))

    def listen(self, twitter):
        print 'Running through the listeners for %s'%self.__class__.__name__
        for listener in self.listeners:

            results = []

            # We want results from this time and later, so let's run an 
            # initial search to obtain the latest tweet id for the listeners
            if listener.since_id == 0:
                print "First run on this listener. Getting most current ID."
                response = twitter.search(q=listener.search_query, rpp=1)
                listener.since_id = int(response['max_id_str'])
                print "Obtained most current ID: %s"%listener.since_id

            # Otherwise, we have a since tweet id. Let's run our query on all
            # tweets since this tweet ID.
            else:           
                # Now let's get the results from this time on
                nr_results = 1
                cur_page = 1
                print "Getting current results for query ``%s``:."\
                        %listener.search_query

                # While we have returned results, get run the query, then go
                # go to the next page of results
                while nr_results > 0:
                    response = twitter.search(q=listener.search_query, 
                            since_id=listener.since_id, rpp=100, page=cur_page)
                    print "Begin page %s >>>"%cur_page
                    for result in response['results']:
                        long_text = result['text']
                        short_text = 0
                        if len(long_text) <=30:
                            short_text = long_text[:30]
                        else:
                            short_text = long_text[:27] + '...'
                        #dt = datetime.strptime(result['created_at'],'%a, %d %b %Y %H:%M:%S')
                        dt = result['created_at']
                        print '\t%s "%s" from @%s'%(dt, 
                                short_text,
                                result['from_user'])
                        results.append(result)
                    print "<<< end page %s"%cur_page
                    listener.since_id = int(response['max_id_str'])
                    print "Since ID changed to %s"%listener.since_id
                    nr_results = len(response['results'])
                    cur_page += 1
                print "That's all for now!"

                # Finally, call the handler function for the current listener
                # for each result
                for result in results:
                    listener.handler(result, twitter)

