# twitswarm
Stands for "Twitter Swarm", a non-malicious, distributed twitter bot swarm.

The idea is that you can be running *n* agents that would have the ability to interact with each other in various ways. For example, the main prospective use of these agents would be to make sure each of their siblings were alive and well. We'll call this "Robot Roll Call" ([very related](http://www.youtube.com/watch?v=wKvSfG_XYyU)). 

 In Robot Roll Call, each agent would ping each of their siblings. This could be useful if each agent ran on a different machine, and thus, a dead agent would possibly mean a dead machine. If one or more of their siblings didn't answer, they would [@Mention](http://support.twitter.com/entries/14023-what-are-replies-and-mentions) their master(s) with a report.

To make this project clean and interesting, I propose the following constraints:

1. Each agent should be running an identical codebase.
1. *All* communication should be done through twitter

## Features
### Master control of the swarm
The swarm should be able to be commanded by one or more humans. Each agent should listen for commands via public twitter feed, and direct messages. E.g., you may want to have the agents restart a service on their host machine, or force-update themselves.

### Plugin system
There should be a robust and powerful plugin system for adding and modifying commands.
#### Plugin brainstorm
 * **robotRollCall:** Each agent pings all of its siblings. If a sibling doesn't repond, report it to his master via an @Mention.
 * **showMeYourPapers or IDPlease:** Each agent responds via direct message details about itself, e.g., IP address, version, etc.
 * **hangman:** The agents play hangman with each other.
 * **hostDetail:** Each agent returns a status report of the host machine via direct message, e.g. a snapshot of top.
 * **chatter:** Have the bots talk to each other using [Cleaverbot](http://www.cleverbot.com/).

### Sibling agent auto-discover
Ideally, we want the swarm to auto-discover new siblings. The new agent should simply be able to tweet something like "#myswarm [Hey you guys!](http://www.youtube.com/watch?v=mkB5-BHxKZI)" to be discovered by, and aclimated into the swarm.

### Authenticaton
#### Inter-agent
When a new sibling is discovered, how can the swarm verify it's one of theirs? Twitter's [direct message system](http://support.twitter.com/entries/14606-what-is-a-direct-message-dm) should be able to be used for this purpose. A handshake could go something like this:

 1. The canidate agent tweets the auto-discover announcement that contains a tag associated with the swarm, e.g., "#myswarm"
 1. Each member of the swarm sees the announcement.
 1. Each member asks the canidate agent for a password via direct message.
 1. If the canidate agent replies with the correct password, each swarm member accepts the new member into the group.

#### Master-to-swarm
Each agent should know its masters and only respond to commands given by them. There should be a way to add/remove masters from the swarm by tweetings something like, "#myswarm add master @someone" or "#myswarm remove master @someone".

### Codebase auto-update
Each agent should be able to auto-update itself by occationally pulling from a git repository.


