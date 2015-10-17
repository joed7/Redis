##Strings   

The Redis String type is the simplest type of value associated with a key. When we use redis string, we map one string to another. Redis strings can be used to implement cache system like Memcache where string keys are used to store authentication information, cache complex queries etc.
Strings can also be used as atomic counters using commands of __INCR__ family.

__Important [String](http://redis.io/commands#string) functions__

* __SET key value__: Sets value for a key. If key holds a value, it is overwritten.    
`set login rohit` 

* __GET key__: Returns the value associated key.  
`GET login`

* __INCR key__: Increments the value of key by one. It can be used to maintain counter.  
`INCR ctr`

* __APPEND key value__: Appends the value to a key.  
`APPEND msg hello`

