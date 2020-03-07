import tweepy
import requests
import os
import sys
from dotenv import load_dotenv

#get API keys within heroku environment
consumer_key=str(os.environ.get('CONSUMER_KEY'))
consumer_secret=str(os.environ.get('CONSUMER_SECRET'))
access_token_key=str(os.environ.get('ACCESS_TOKEN_KEY'))
access_token_secret=str(os.environ.get('ACCESS_TOKEN_SECRET'))

#if using script outside of heroku environment
if consumer_key == 'None':
    load_dotenv()
    consumer_key=str(os.environ.get('CONSUMER_KEY'))
    consumer_secret=str(os.environ.get('CONSUMER_SECRET'))
    access_token_key=str(os.environ.get('ACCESS_TOKEN_KEY'))
    access_token_secret=str(os.environ.get('ACCESS_TOKEN_SECRET'))


#init API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)

api = tweepy.API(auth)

#search tweets
def search(tag, count = 10, likes = 0, lang = None):
    # like_str = ""
    # if likes > 0:
    #     like_str = "%20min_faves%3A" + str(likes)

    if not lang:
        return api.search(q=tag + " filter:native_video -filter:retweets", rpp=count, count=count, min_faves=likes, include_entities=True)
    else:
        return api.search(q=tag + " filter:native_video -filter:retweets", rpp=count, count=count, min_faves=likes, lang=lang, include_entities=True)

#get video url
def get_media(tweet):
    try:
        variants = tweet.extended_entities['media'][0]['video_info']['variants']
        return get_best_video(variants)
    except:
        return False

#select highest quality url
def get_best_video(variants):
    highest = variants[0]
    for v in variants:
        if v['content_type'] == 'video/mp4':
            if highest['bitrate'] < v['bitrate']:
                highest = v

    return highest['url']

#save media to device
def save_media(url, path):
    file = requests.get(url)
    path = path + ".mp4"

    i = 1
    while os.path.isfile(path):
        path = path[:-4] + "(" + str(i) + ").mp4"
        i += 1

    open(path, 'wb').write(file.content)

#main method
def scrape(tag, path, count=10, likes=0, lang=None):
    for i in search(tag, count = count, likes=likes, lang=lang):

        url = get_media(i)
        if url:
            save_media(url, path + i.user.screen_name)

#usage:
#on terminal write python media_scraper.py [tag] [folder path] [tweet count]
if __name__ == '__main__':
    print(sys.argv)
    if len(sys.argv) > 1:
        tag = sys.argv[1]
        path = sys.argv[2]
        count = int(sys.argv[3])
        likes=None
        if len(sys.argv) > 4:
            likes = count = int(sys.argv[4])
        scrape(tag, path, count=count, likes=likes)
    else:
        scrape("meme", "results/")
