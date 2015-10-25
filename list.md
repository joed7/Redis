##Lists

List is Redis a sequence of ordered elements: 1,2,3,4,5. Lists in Redis are implemented via Linked List, which means that even in a list with millions of items, the operation of adding a new element at the beginning or end is performed in constant time;  Redis Lists are implemented with linked lists because for a database system it is crucial to be able to add elements to a very long list in a very fast way.

__Important [List](http://redis.io/commands#list) functions__

* __LPUSH Key Value__: Adds an element or more than one element on the left of the list(at the beginning).  
`LPUSH mylist A #Adds A at the beginning of the list`  
`LPUSH grand_slam "US OPEN" "Wimbeldon" "French Open" "Australian Open"` #list with grand slams in chronological order   

* __RPUSH Key Value__: Adds an element or more than one element on the right of the list(at the end)  
`RPUSH mylist B #Adds B at the end of the list`  
`RPUSH grand_slam "Australian Open" "French Open" "Wimbeldon" "US OPEN"` #list with grand slams in chronological order 

* __LRANGE Key Start Stop__: Returns the specified elements of the list stored at key.  
`LRANGE mylist 0 2 #print the first 3 elements of the list`  
`LRANGE mylist 0 -1 #print all the elements of the list`  

* __LTRIM key Start Stop__: Trim an existing list so that it will contain only the specified range of elements specified.   
```
LPUSH mylist element1
LPUSH mylist element2
LPUSH mylist element3

LTRIM mylist 0 99 #Trim the list to 100 element
```

* __RPOP Key__: Remove and return the last element of list.  
* __LPOP Key__: Remove and return the first element of list.  
* __LLEN key__: Returns the length of the list.

__Common Use cases__

* Maintaining fixed number of latest items, like 10 latest stories, 10 latest blogs etc.
```
LPUSH news item1
LPUSH news item2
LPUSH news item3

LTRIM news 0 10
LRANGE news 0 -1
``` 

* Maintaining items like message, blogs etc on a website.
```
LPUSH posts post1
LPUSH posts post2
LPUSH posts post3
....

```

[Previous](https://github.com/joed7/Redis/blob/master/hash.md)  |  [Home](https://github.com/joed7/Redis/blob/master/home.md)  |  [Next](https://github.com/joed7/Redis/blob/master/set.md)