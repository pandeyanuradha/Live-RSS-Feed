import hashlib
import feedparser

URL = 'https://www.wired.com/feed/rss'

def get_feed():
    
    # GET request, parse, and store the XML in a var
    data = feedparser.parse(URL)
    feed = []
    
    # list for storing titles
    for entry in data.entries: 
        feed.append(entry.title)
    return feed

def get_hash():
    
    # GET request, parse, and store the XML in a var
    feed_parse = feedparser.parse(URL)
    
    # Create initial hash of the timestamp
    hashVal = hashlib.sha224((str(feed_parse.feed.updated).encode('utf-8'))).hexdigest()
    return hashVal
