# twitswarm
Stands for "Twitter Swarm", a non-malicious, distributed twitter bot mesh network.

The idea is that you can be running *n* agents that would have the ability to interact with each other in various, productive ways. For example, the main prospective use of these agents would be to make sure each of their siblings were alive and well. We'll call this "Robot Roll Call" ((very related)[http://www.youtube.com/watch?v=wKvSfG_XYyU]). In Robot Roll Call, each agent would ping each of their siblings. If one or more of their siblings didn't answer, they would (@Mention)[http://support.twitter.com/entries/14023-what-are-replies-and-mentions] their master with a report.

Each agent should be running an identical codebase.

## Master control of the swarm
The swarm should be able to be commanded by one or more humans. Each agent should listen for commands via public twitter feed, and direct messages. E.g., you may want to have the agents restart a service on their host machine, or force-update themselves.

## Plugin system
There should be a robust and powerful plugin system for adding and modifying commands.

## Sibling agent auto-discover
Ideally, we want the swarm to auto-discover new siblings. The new agent should simply be able to tweet something like "#myswarm (Hey you guys!)[http://www.youtube.com/watch?v=mkB5-BHxKZI]" to be discovered by, and aclimated into the swarm.

## Authenticaton
### Inter-agent
When a new sibling is discovered, how can the swarm verify it's one of theirs? Twitter's (direct message system)[http://support.twitter.com/entries/14606-what-is-a-direct-message-dm] should be able to be used for this purpose. A handshake could go something like this:
 0. The canidate agent tweets the auto-discover announcement that contains a tag associated with the swarm, e.g., "#myswarm"
 0. Each member of the swarm sees the announcement.
 0. Each member asks the canidate agent for a password via direct message.
 0. If the canidate agent replies with the correct password, each swarm member accepts the new member into the group.
### Master-to-swarm
Each agent should know its masters and only respond to commands given by them. There should be a way to add/remove masters from the swarm by tweetings something like, "#myswarm add master @someone" or "#myswarm remove master @someone".

## Codebase auto-update
Each agent should be able to auto-update itself by occationally pulling from a git repository.

