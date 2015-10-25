##Installation

__Redis__ can be installed in Linux/Mac by following these instructions

1: Download the latest version of Redis.  
  `wget http://download.redis.io/releases/redis-3.0.4.tar.gz`  
2: Extract the binaries.  
  `tar xzf redis-3.0.4.tar.gz`  
3: Change directory to extracted directory.  
  `cd redis-3.0.4`  
4: Compile Redis  
  `make`
  
The binaries that are now compiled are available in the src directory. Run Redis with:  
`src/redis-server`

You can interact with Redis using the built-in client:  
`src/redis-cli`

Example session:
```
redis 127.0.0.1:6379> set foo 1
OK
redis 127.0.0.1:6379> get foo
"1"
```
__Note__: As per official documentation, The Redis project does not officially support Windows. However, the Microsoft Open Tech group develops and maintains this Windows port targeting Win64.

Refer to the [documentation](http://redis.io/download) for more information.


[Previous](https://github.com/joed7/Redis/blob/master/introduction.md)  |  [Home](https://github.com/joed7/Redis)  |  [Next](https://github.com/joed7/Redis/blob/master/string.md)