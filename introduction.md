##Introduction

Redis is an open source, __in-memory__ data-structure store, used as database, cache and message broker. While it is described as a key-value store, unlike traditional key-value stores where you associate string keys to string values, in Redis the value is not limited to a simple string, but can also hold more complex data structures; It supports data structures such as strings, hashes, lists, sets, sorted sets with range queries, bitmaps, hyperloglogs and geospatial indexes with radius queries. The name Redis means __REmote DIctionary Server__.

Some key advantages of Redis are as follows:

* Since Redis works with an in-memory dataset, it is exceptionally fast. Depending on the use case, one can persist it either by dumping the dataset to disk every once in a while, or by appending each command to a log. Persistence can be optionally disabled, if one just needs a feature-rich, networked, in-memory cache.

* All the Redis operations are atomic, which ensures that if two clients concurrently access Redis server will get the updated value.

* Redis supports most of the datatypes like list, set, sorted set, hashes. This makes it very easy to solve a variety of problems because we know which problem can be handled better by which data type. For e.g. message queue using __list__, leader-board using __sorted set__ , a collection of unique items using __sets__, custom object using __hashes__ etc.
  
* Redis supports master-slave replication that allows slave Redis servers to be exact copies of master servers.

* Redis provides fast Publish/Subscribe messaging system which can be used to implement message queues.

[Home](https://github.com/joed7/Redis)  |  [Next](https://github.com/joed7/Redis/blob/master/installation.md)
