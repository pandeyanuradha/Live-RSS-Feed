import hashlib
import feedparser

URL = 'https://www.wired.com/feed/rss'

def get_request():
    
    # GET request, parse, and store the XML in a var
    feed_parse = feedparser.parse(URL)
    return feed_parse
    
def get_feed():
    
    # GET request, parse, and store the XML in a var
    data = get_request()
    feed = []
    
    # list for storing titles
    for entry in data.entries: 
        feed.append(entry.title)
    return feed

def get_hash():
    
    data = get_request()
    
    # create initial hash of the timestamp
    
    entry = str(data.entries[0].title)
    hashVal = hashlib.sha224(entry.encode('utf-8')).hexdigest()
    return hashVal
