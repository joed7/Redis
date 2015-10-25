##Putting it all together

In the previous section, we took a look at the various data-types of redis, and in what scenarios we can use them. In this section, we will create a data-model of a twitter like application using redis. Please find the sourcecode of this data-model [here](https://github.com/joed7/Redis/blob/master/twitter.py). 

The application consists of the following entities:

* __Users(Hashes)__: Users of the application. The hash will consist of user information like username, password, email, screenname. Each user will be assigned a user_id, which will be used in the key for user hashes; For e.g. users:1, users:2.

* __Followers(Sets)__: Follower of Users. The set will consist of the user_ids of all of the users following a particular user. Sample keys, followers:1,followers:2.

* __Following(Sets)__: Users a user is following, The set will consist of the user_id of all the user, a particular is following. Sample keys following:1, following:2.

* __Tweets(Lists)__: List of the tweets of a particular user. Sample keys tweets:1, tweets:2

* __Counter(String)__: Counter keeping track of the users in the application, Used to assign user_id to the user. Key in the database for this entity __users__.

* __Usernames(Hash)__: A hash storing the mapping for usernames and userid.


__Implementation Details__

* __CreateUser__: This method takes userdetails hashmap as a parameter. First, we check if the username for this user exists in the system; If yes, we terminate the execution, else we increment the counter, and create a hash corresponding to this user.

* __Tweet__: This method takes a tweet string and a userId as arguments, and append the tweet to tweet list corresponding to the userId.

* __Follow__: The methods takes two parameters source_user_id(user following), target_user_id(user being followed). Appropriate followers, following sets are then modified using `sadd`.

* __Unfollow__:  The methods takes two parameters source_user_id(user following), target_user_id(user being followed). Appropriate followers, following sets are then modified using `srem`.

* __Info__: The method takes username as a parameter. For that parameters, we fetch the user_id is fetched, and fetch the data from follow, following, tweet keys.

[Previous](https://github.com/joed7/Redis/blob/master/redispy.md)  |  [Home](https://github.com/joed7/Redis/blob/master/home.md)  |  [Next](https://github.com/joed7/Redis/blob/master/pubsub.md)