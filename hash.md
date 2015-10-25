##Hashes
Redis Hashes are maps between string fields and string values, so they are the perfect data type to represent objects.

__Important [Hash](http://redis.io/commands#hash) functions__

* __HMSET key field value [field value...]__: Sets the specified fields to their respective values in the hash stored at key. 

```
HMSET user:1 login "rohit" password "passowrd" email "abc@xyz.com" #defines a User Object with fields login, passowrd, email for user 1 in this example  

HMSET twitter:user:1 name "rohit" followers "20" following "50" #defines twitter object for user:1
```

* __HMGET key field [field...]__: Returns the values associated with the specified fields in the hash stored at key.  
`HMGET user:1  age city #returns the age and city attribute for user 1`

* __HSET key field value__: Sets field in the hash stored at key to value.  
`HSET user:1 surname 'gupta'`

* __HGET key field__: Returns the value associated with field in the hash stored at key.  
`HGET user:1 surname`

* __HGETALL key__: Returns all fields and values of the hash stored at key. In the returned value, every field name is followed by its value, so the length of the reply is twice the size of the hash.  
`HGETALL user:1 #returns all of the attributes of user 1`

* __HDEL key field[field..]__: Removes the specified fields from the hash stored at key.  
`HDEL user:1 city #deletes the city attribute for user`

* __HEXISTS key field__: Returns if field is an existing in hash. 1 if hash contains field, 0 if it doesn't.  
`HEXISTS user:1 city #checks if city attribute exists for user:1`

__Common Use cases__

As noted earlier, Hashes are used to represent object in Redis. For e.g
```
HMSET user:credential:1  login "rohit" password "passowrd" email "abc@xyz.com" #defines credentials for user1
HMSET tweet:101  user "user1" tweet "text"  time "time" #defines a tweet object

```

[Previous](https://github.com/joed7/Redis/blob/master/string.md)  |  [Home](https://github.com/joed7/Redis/blob/master/home.md)  |  [Next](https://github.com/joed7/Redis/blob/master/list.md)
 