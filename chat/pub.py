'''Python script to publish a message to a channel, arg1=sender's name, arg2=channel's name
'''
import redis
import sys

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print 'Incorrect arguments'
        print 'usage: python pub.py sender_name channel_name'
        sys.exit()
        
    r = redis.Redis(host='localhost',port=6379)    
    name = sys.argv[1]
    channel = sys.argv[2]

    print 'Welcome to '+channel

    while True:
        message = raw_input('Enter a message: ')

        if message.find('exit') != -1:
            print 'Closing the channel'
            r.publish(channel, message)                        
            break            
        else:
            r.publish(channel, message)            
