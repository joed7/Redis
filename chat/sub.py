''' Python script to subscribe to a channel, arg1=channelName
'''
import redis
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'Incorrect arguments'
        print 'usage: python sub.py channel_name'
        sys.exit()    
    channel = sys.argv[1]
    r = redis.Redis(host='localhost',port=6379)        

    pubsub = r.pubsub()
    pubsub.subscribe(channel)

    print 'Listening to '+channel

    while True:
        for item in pubsub.listen():
            msg=item['data']
            print msg
                    
