##Redis-Py 

In order to access Redis from python, we need a Redis client; [Redis-Py](https://github.com/andymccurdy/redis-py/) is one such client.

__Installation__

Redis-Py can be installed using this pip command `sudo pip install redis`.

__Connecting to Redis__

Here is a python code snippet which opens a connection to Redis, sets a key and queries it.

```
import redis

#Opens a connections to redis
r = redis.Redis(host='localhost',password='')

#check if connection exists
r.ping()

```

__Using Redis data structures with Redis-Py__

* __String__  
```
import redis
r = redis.Redis(host='localhost',password='')

r.ping()

#setting a key 
r.set('name','rohit') 

#querying a key
print r.get('name')
```

* __List__
```
'''Python script demonstrating using list with Redis-Py
'''
 
import redis

#Opens a connections to redis
r = redis.Redis(host='localhost',password='')

r.delete('msgQueue')

r.lpush('msgQueue','msg1')
r.lpush('msgQueue','msg2')
r.lpush('msgQueue','msg3')
r.lpush('msgQueue','msg4')

#print all the message in the queue
print r.lrange('msgQueue',0,-1)

#print the first two messages in the queue
print r.lrange('msgQueue',0,1)

```
* __Set__
```
'''Python script demonstrating using sets with Redis-y
'''
 
import redis

r = redis.Redis(host='localhost',password='')

r.delete('visitors')

#Visitors is a set maintaining set of unique visitors
r.sadd('visitors','A')
r.sadd('visitors','B')
r.sadd('visitors','C')
r.sadd('visitors','C')
r.sadd('visitors','B')
r.sadd('visitors','D')

#print all of the members of the set
print r.smembers('visitors')

#Check if a particular user has visited the site
print r.sismember('visitors','A')
print r.sismember('visitors','E')
```

* __Sorted-Set__
