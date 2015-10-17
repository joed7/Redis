##Sorted Sets

Redis Sorted Sets are similar to Redis Sets in the sense that they non repeating collections of Strings. Additionally, every member of a Sorted Set is associated with score, that is used in order to make the sorted set ordered, from the smallest to the greatest score. In sorted-sets, we can add, delete, update elements in logarithmic time. Since the elements in a set are ordered, we can get range of elements(top 5, top 10 etc.) or element by rank(5th highest score) in a very fast time. Thus, with sorted sets we can do a lot of tasks with great performance that are really hard to model in other kinds of databases 

__Important Sorted-Sets functions__
    
* __ZADD key score member [score member...]__: Adds all the specified members with the specified scores to the sorted set stored at key. If a specified member is already a member of the sorted set, the score is updated and the element reinserted at the right position to ensure the correct ordering.   
`ZADD myset 5 "player1"`

* __ZREM key member [member..]__:Removes all the specified members from the sorted set.
`ZREM myset "player1"`

* __ZRANGE key start stop__: Returns the specified range of elements from the sorted set. It is important to note that in sorted sets elements are ordered from lowest to highest score.
`ZRANGE myset 0 4 #returns the members with four lowest scores`

* __ZRANGEBYSCORE key min max__: Returns all the elements in the sorted with a score between min and max (inclusive).
`ZRANGEBYSCORE myset 0 5`

* __ZRANK key member__: Returns rank of a member in the sorted set.
`ZRANK myset player1`

* __ZSCORE key member__: Returns the score of a member in the sorted set.
`ZSCORE myset player1`

__Common Use Cases__

* A common use case of sorted sets is Leader Board implementation for a online game. Score for a user can be added or updated using ZADD. In order to fetch Top X players by score we can use ZRANGE.

* For a website like Reddit or Stackoverflow, Sorted Sets can be used to return posts exceeding certain number of votes or views using ZRANGEBYSCORE.


