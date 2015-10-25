##Pipelining

The usual way a Redis client interacts with the server is to issue a command, wait till it gets executed and then read the returned response. So, when the number of commands grows, performance can take a hit. One way of improving this is by using pipelining, in which case you send your commands to the server in a group in a single request, and read the combined responses at the end in one block when the pipeline is "closed".
Thus you save on the RTT(Round Trip Time), the time taken by the packets to travel from the client to the server, and back from the server to the client to carry the reply.
 
__Usage Example__

```
'''Python Script demonstrating concepts of pipelining
'''

import redis
import time

r = redis.Redis(host='localhost',port=6379) 
pipe = r.pipeline(transaction=False)
lst = range(100000)

start_time = time.time()
for i in lst:
    pipe.set("key"+str(i),"value"+str(i))

pipe.execute()
print("--- %s seconds with Pipelining---" % (time.time() - start_time))

start_time = time.time()
for i in lst:
    r.set("key"+str(i),"value"+str(i))
print("--- %s seconds without Pipelining ---" % (time.time() - start_time))
    
    
```    

In this example, we are trying to set 100,000 keys. Initially, we try it with pipe-lining by getting the pipeline object, calling the set function for each key and then calling execute on that pipe object; After that, we try to do the same thing without using pipe-lining, by sending each set call to the server separately. For my machine, code with pipelining took approx 1 sec, while code without pipelining took close 3.6 sec, thus highlighting the time saved when using pipelining.   

[Previous](https://github.com/joed7/Redis/blob/master/pubsub.md)  |  [Home](https://github.com/joed7/Redis/blob/master/home.md)  |  [Next](https://github.com/joed7/Redis/blob/master/transaction.md)