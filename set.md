##Sets

Redis Sets are __unordered__ collections of unqiue strings. Some of the common operations with sets are testing if a given element already exists, performing the intersection, union or difference between multiple sets, and so forth. Key point to note is that set can perform add, remove, find operations in constant time.

__Important [Set](http://redis.io/commands#set) functions__

* __SADD key member [member ...]__: Add one or more members to a set. Returns number of added elements.  
`SADD set1 Hello`  

* __SREM key member [member ...]__: Removes one or more members from a set. Returns number of removed elements.  
`SREM set1 Hello`  

* __SISMEMBER key member__: Checks if member is a member of a set. Returns 1 is a member of the set  or 0 if it does not.  
`SISMEMBER set1 one`   

* __SMEMBERS key__: Returns all the members of a set.  
`SMEMBERS set1`  

* __SINTER key1 key2 key3__: Returns the members of the set resulting from the intersection of the given sets.  
`SINTER set1 set2`  

* __SUNION key1 key2__: Returns the members of the set resulting from the union of all the given sets.  
`SUNION set1 set2`  

* __SCARD key__: Returns the number of elements of a set.

__Common Use Cases__

* For a site like stackoverflow.com, it can be used to store tags for  questions.  
`sadd question:100 1 4 7 #Question with tags 1,4,7`

* For a social networking site, it can be used to store followers, friends etc.  

* Keeping track of unique visitor, storing ip addresses of the visitors in a set.  

* Multi Parameter search can be performed using SINTER. For e.g. 
```
#Find all the questions with tags x,y,z
SADD tag:x 1 2 3 #Questions with tag x
SADD tag:y 3 4 5 #Questions with tag y
SADD tag:z 2 3 7 #Questions with tag z

SINTER tag:x tag:y tag:z #Questions with tags x,y,x
```
