'''Twitter design using redis
'''

import redis



'''Keys for Redis Objects
'''
counter='users'#user counter for user id
followers='followers:'#followers
following='following:' #users following
users = 'users:' #User Object
usernames='unames' #mapping between username and userid
tweets='tweets:' #list containing tweets

'''Keys for user object
'''
uname='username'
pwd='password'
sname='screenname'
email='email'

#Redis Connection
r = redis.Redis(host='localhost',port=6379) 

#list keeping track of all of the users
usrs=[]



def reset():
    '''Function resetting the application, delete all the tweets, users and resets the coutner
    '''
    r.set(counter,0)
    r.delete(usernames) #delete all the username-userId mapping
    global usrs
    
    for u in usrs:
        r.delete(followers+str(u))
        r.delete(following+str(u))
        r.delete(users+str(u))
        r.delete(tweets+str(u))
        
    usrs=[]
    
def createUser(userdetails):    
    '''Create a user for the given user details
    '''
    
    username=userdetails[uname]
    
    #check if user name exists
    if r.hget(usernames,username) != None:
        print 'User Name already exists'
        return False
        
    #create a new user      
    userid = r.incr(counter)
    usrs.append(userid)
    
    r.hset(usernames,username,userid) #assign userId to this userName
    r.hmset(users+str(userid),userdetails) #creating the user object in redis
    
    return True
    
    
    

def tweet(sUname,text):
    '''Function handling tweet action for a user
    '''
    sUserId = r.hget(usernames,sUname)
    r.lpush(tweets+str(sUserId),text)

def follow(sUname,tUname):
    '''Follower a user
    '''    
    sUserId = r.hget(usernames,sUname)
    tUserId = r.hget(usernames,tUname)
    
    r.sadd(following+str(sUserId),tUserId)
    r.sadd(followers+str(tUserId),sUserId)
    
def unfollow(sUname,tUname):
    '''Unfollow a user
    '''
    sUserId = r.hget(usernames,sUname)
    tUserId = r.hget(usernames,tUname)
    
    r.srem(following+str(sUserId),tUserId)
    r.srem(followers+str(tUserId),sUserId)    


def info(userName):
    '''Print details for a userNmae
    '''
    
    if r.hget(usernames,userName) == None:
        print 'The userName does not exist'
        return False
    
    userid = r.hget(usernames,userName) #Get userId from the userNmae   
    udetails = r.hgetall(users+str(userid)) #Get user details corresponding to userId
    uFollowers = r.smembers(followers+str(userid)) #Get followers for this ID
    uFollowing = r.smembers(following+str(userid)) #Get all of the followers this user is following
    uTweets = r.lrange(tweets+str(userid),0,4) #Get the latest 5 tweets
    followerString = ''
    followingString = ''
    
    for eFollower in uFollowers:
        eFollowerScreenName = r.hget(users+str(eFollower),'screenname')
        followerString = followerString + eFollowerScreenName + ','
        
    for eFollowing in uFollowing:
        eFollowerScreenName = r.hget(users+str(eFollowing),'screenname')        
        followingString = followingString + eFollowerScreenName + ','                
    
    print('Printing details for '+str(userName) )
    print('')
    print('Screen Name '+ udetails[sname])
    print('Total Followers:'+str(len(uFollowers)))
    print('Follwers: '+followerString)
    print('Total Following:'+str(len(uFollowing)))     
    print('Following: '+followingString)
    print('Total Tweets: '+str(len(r.lrange(tweets+str(userid),0,-1))))
    print('Printing latest tweets(last five)')
    for t in uTweets:
        print t
    
    

createUser({uname:'rohit',pwd:'rohit',sname:'joed7',email:'xxx'})
createUser({uname:'yankees',pwd:'pwd',sname:'NY yankees',email:'xxx'})
createUser({uname:'mets',pwd:'pwd',sname:'NY mets',email:'xxx'})
createUser({uname:'giants',pwd:'pwd',sname:'SF giants',email:'xxx'})
createUser({uname:'rockies',pwd:'pwd',sname:'Colorado rockies',email:'xxx'})

follow('rohit','mets')
follow('rohit','giants')

tweet('rohit','tweet1')
tweet('rohit','tweet2')
tweet('rohit','tweet3')
tweet('rohit','tweet4')
tweet('rohit','tweet5')
tweet('rohit','tweet6')
tweet('rohit','tweet7')
tweet('rohit','tweet8')

info('rohit')

#comment out reset to not to reset twitter data
reset()
