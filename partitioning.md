##Partitioning

Partitioning is the process of splitting data into multiple Redis instances, so that every instance will only contain a subset of the total keys. Partitioning is useful because 

* It allows for much larger databases, using the sum of the memory of many computers.  
* It allows scaling the computational power to multiple cores and multiple computers, and the network bandwidth to multiple computers and network adapters.

There are different ways for doing partitioning. There is __Range partitioning__ where we map ranges of objects in specific redis instances; For e.g.  we could say users from ID 0 to ID 10000 will go into instance R0, while users form ID 10001 to ID 20000 will go into instance R1 and so forth. There is __Hash partitioning__ where for a key we compute the hash and apply the modulo operation to get a number representing our Redis instance; One limitation of basic hash partitioning is that when we want to add or remove a node from the system, we have to rearrange all of the keys of the database. To resolve this issue, an advanced form of of hash partitioning  was invented called [__consistent hashing__](https://en.wikipedia.org/wiki/Consistent_hashing) which is implemented by a few Redis client

__Disadvantages of Partitioning__

* Operations involving multiple keys are usually not supported. For instance you can't perform the intersection between two sets if they are stored in keys that are mapped to different Redis instances.

* Redis transactions involving multiple keys can not be used.

* When partitioning is used, data handling is more complex, for instance you have to handle multiple RDB / AOF files, and to make a backup of your data you need to aggregate the persistence files from multiple instances and hosts.

* Adding and removing capacity can be complex because rebalancing of keys needs to be done.


__Different implementation of partitioning__

* __Client side partitioning__: It means that the clients directly select the right node where to write or read a given key. Many Redis clients implement client side partitioning. 

* __Proxy assisted partitioning__: It means that our clients send requests to a proxy that is able to speak the Redis protocol, instead of sending requests directly to the right Redis instance. The proxy will make sure to forward our request to the right Redis instance accordingly to the configured partitioning schema, and will send the replies back to the client.

* __Query routing__: It means that you can send your query to a random instance, and the instance will make sure to forward your query to the right node