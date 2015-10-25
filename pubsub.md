##Publisher and Subscriber

Redis provides a Publisher/Subscriber based message queue system. In redis pub/sub, Senders(Publishers) don't send their messages directly to specific receivers(subscribers); Instead, messages are sent by publishers to channels without any knowledge of the subscribers, Subscribers who wish to receive messages subscribe to these channels wihtout any knowledge of these publishers. This decoupling of publishers and subscribers can allow for greater scalability and a more dynamic network topology.

__Important [Pub/Sub](http://redis.io/commands#pubsub) functions__:

* __SUBSCRIBE channel [channel...]__: Subscribe the client to the specified channels.  
`SUBSCRIBE testers`

* __UNSUBSCRIBE channel [channel...]__: Unsubscribe the client from the given channels.  
`UNSUBSCRIBE` testers  

* __PUBLISH channel message__: Posts a message to the given channel.  
`PUBLISH developers "message for developers"`


__Common use case__

Redis pub/sub can be used to implement mobile game chat, where we can have one __global channel__ for system wide chat and __alliance channel__ for each alliance. All the users of the game will subscribe to global channel and alliance channel for their alliance.


__Redis Pub/Sub in python__  

A very basic chat implmentation using Redis Pub/Sub in python can be found [here](https://github.com/joed7/Redis/tree/master/chat).
The example consists of a [publisher](https://github.com/joed7/Redis/blob/master/chat/pub.py) and [subscriber](https://github.com/joed7/Redis/blob/master/chat/sub.py). Both of them are python scripts and can be executed as follws:

```
python pub.py sender channel

python sub.py channel
```

Publisher sends the message to the specfied channel until it encouters exit message; Subscriber subscribes to the specified channel and receives 
messages until it encounters the exit message,On encountering exit message, it unsubscribes from that channel and exits.

[Previous](https://github.com/joed7/Redis/blob/master/twitter.md)  |  [Home](https://github.com/joed7/Redis)  |  [Next](https://github.com/joed7/Redis/blob/master/pipelining.md)

 