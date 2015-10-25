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
'''Python script demonstrating using sets with Redis-py
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

* __Hash and Sorted-Sets__

```
import redis

#Opens a connections to redis
r = redis.Redis(host='localhost',password='')

r.delete('player:1')
r.delete('player:2')
r.delete('player:3')
r.delete('player:4')
r.delete('leaderboard')

#Hash Representing user objects
r.hmset('player:1',{'id':1,'dname':'xyz','platform':'android'})
r.hmset('player:2',{'id':2,'dname':'pqr','platform':'ios'})
r.hmset('player:3',{'id':3,'dname':'xxx','platform':'winodws'})
r.hmset('player:4',{'id':4,'dname':'yyy','platform':'online'})


#adding entries to sorted set, user_id,score
r.zadd('leaderboard','1',15,'2',25)
r.zadd('leaderboard','3',9)
r.zadd('leaderboard','4',0)

#getting id for the user with highest score
id=r.zrevrange('leaderboard',0,0)
print 'display name of the player with higest score: '+r.hget('player:'+str(id[0]),'dname')
```

[Previous](https://github.com/joed7/Redis/blob/master/sortedset.md)  |  [Home](https://github.com/joed7/Redis/blob/master/home.md)  |  [Next](https://github.com/joed7/Redis/blob/master/twitter.md)