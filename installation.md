##Installation

__Redis__ can be installed in Linux/Mac by following these instuctions

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
'''
redis 127.0.0.1:6379> set foo 1
OK
redis 127.0.0.1:6379> get foo
"1"
'''
