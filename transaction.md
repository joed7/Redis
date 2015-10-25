##Transactions

A [transaction](http://redis.io/topics/transactions) in redis is a collection of commands placed between MULTI and EXEC (or DISCARD for rollback). Once a MULTI has been encountered, the commands on that connection are queued and are not executed until EXEC is encountered, when they are all applied in a single unit (i.e. without other connections getting time between operations). If a DISCARD is seen instead of a EXEC, everything is thrown away. 
It can never happen that a request issued by another client is served in the middle of the execution of a Redis transaction. This guarantees that the commands are executed as a single isolated operation.

__Usage Examples__

Here is an example demonstrating EXEC command:

```
> MULTI  #start of a transaction
OK
> INCR foo # operation is queued, not executed
QUEUED
> INCR bar
QUEUED
> EXEC #on encountering EXEC, redis executes the queued operations
1) (integer) 1
2) (integer) 1
```

This is an example of DISCARD command:

```
> SET foo 1
OK
> MULTI #start of a transaction
OK
> INCR foo #Queue a redis operation
QUEUED
> DISCARD #Discard all of the queued operations
OK
> GET foo
"1"
```

__Check and set behavior in Redis transaction__

Redis provides a function called __WATCH__ which is used to monitor changes in the keys. If at least one watched key is modified before the EXEC command, the whole transaction aborts, and EXEC returns a Null reply to notify that the transaction failed.

__Writing atomic increment without using watch__

```
redis.multi()
current = redis.get('counter')
redis.set('counter', current + 1)  
redis.exec()
```
In the above transaction, there is a race condition between transcations. Multiple transactions can fetch the same value for coutner and increment it by 1, thus giving us an inconsistent state for the variable. To fix this, we can make use of the Watch command,

```
redis.watch()
current = redis.get('counter')
redis.multi ()
redis.set('counter', current + 1)  
redis.exec()
```
If another client changes the value of counter after we’ve called watch on it, our transaction will fail. If no client changes the value, the set will work. We can execute this code in a loop until it works.

[Previous](https://github.com/joed7/Redis/blob/master/pipelining.md)  |  [Home](https://github.com/joed7/Redis)  |  [Next](https://github.com/joed7/Redis/blob/master/partitioning.md)