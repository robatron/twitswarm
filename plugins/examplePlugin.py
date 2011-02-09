'''
Example plugin

Just messing around. No real functionality yet!

Things I found this plugin needs from twitswarm:
    
    registerAutosay:
        Register an auto announcement every _ seconds
    
    registerListener:
        Start listening for specified message from specified stream. Call
        handler when it finds a match.

        Available streams:
            public - listen to entire public stream
            family - only friends of this agent (siblings/masters?)
            user - listen to a specific user
            mentions - only tweets @mentioning this agent
            direct - direct message inbox

    reply:
        Send something to a specific user
'''

def init():
    '''
    Called when plugins are initialized?
    '''

    # Say hello, respond to hellos  
    registerAutoSay(
        interval = 10*60, # every 10 minutes?
        say = "Hello, everybody!"
    )

    registerListener(
        stream = 'friends',
        listenFor = r'Hello everybody!',
        handler = helloListener
    )

    # Conversation test - 
    #   a: Knock knock
    #   b: Who's there?
    #   a: It's me. Open the goddamn door.
    #   b: Ok.
    #   a: Seriously, open the door!
    #   b: FINE, GEEZ
    registerConvo(
        stream = 'friends'
        interval = 30*60, # every 30 minutes
        say = "Knock knock",
        handler = knockKnockHandler
    )

def knockKnockHandler(tweet):
    '''
    Get's called when this agent recieves a "knock knock"
    '''
    reply(
        to = tweet['user']['screen_name']
        say = "Who's there?"

    listenFor(
        r"It's me. Open the goddamn door.",
        stream = ('user', tweet['user']['screen_name']),
        # ...


def helloListener(tweet):
    '''
    Receives the entire tweet as a dictionary?
    '''

    # send to specific user
    reply(
        to = tweet['user']['screen_name'],
        say = 'Hi, Dr. %s!'%tweet['user']['screen_name']

