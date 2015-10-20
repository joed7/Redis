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

    pubsub = r.pubsub(ignore_subscribe_messages=True)
    pubsub.subscribe(channel)

    print 'Listening to '+channel

    while True:
        for item in pubsub.listen():
            msg=item['data']
            if str(msg).find('exit') != -1:
                pubsub.unsubscribe()
                print 'Unsubscribed from the channel'
                sys.exit()
            print msg
            
                    
