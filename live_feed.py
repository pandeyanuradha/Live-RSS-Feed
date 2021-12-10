import time
from utils import get_feed, get_hash

URL = 'https://www.wired.com/feed/rss'

print('--------Running on : %s-------' % URL)
time.sleep(10)

while True:
    try:

        # current hash
        currentHash = get_hash()

        # wait for 30 seconds
        time.sleep(30)

        # create a new hash
        newHash = get_hash()

        # check if new hash is same as the previous hash
        if newHash == currentHash:
            continue

        # if something changed in the hashes
        else:
            
            # notify
            print("\n -------Reloading-------- \n")
            
            # print data
            feed = get_feed()
            for entry in feed:
                print('%s' % (entry))

            # create a hash
            currentHash = get_hash()
            
            # wait for 30 seconds
            time.sleep(30)
            continue
    
    # handle exceptions
    except Exception as e:
        print(e)