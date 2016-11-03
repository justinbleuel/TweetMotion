# # #TwitterMotion
# - Final project, COMS 3103 Fall 2016
# - by Justin Bleuel


from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy
from textblob import TextBlob
import numpy
import math
from PIL import Image
from flask import Flask, request, render_template, redirect

consumer_key = "EAofZ9BX9dsvPISE81QClPYv4"
consumer_secret = "fHqMZtJKTYTu48383aSZBERFispEQIM1sRysoTQUMPcYseK6G0"

access_token = "376276385-FhGsRAFZFhmWL5Rdpx9D705KDyY4pVjPGHhtZzEl"
access_token_secret = "Ha27fJyhQBPPC99onhnR0X61wl09rOWZz4gYGaws4CfLg"


tweet_list = []

#square numbers only, i.e. 25, 49, 100, ..., 900
TWEET_TOTAL = 49

def set_tweet_total(num):
    global TWEET_TOTAL
    if int(math.sqrt(num))%1 != 0:
        return ('please enter square number')
    else:
        TWEET_TOTAL=num

def stream_tweets(term):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    #polarity ranges between -1 and 1, negative = negative opinion
    #subjectivity ranges between 0 and 1, lower value = more objective
    sentiment_list = []
    
    stream = Stream(auth, StdOutListener())
    stream.filter(track=[term])

    #determining tweet sentiment using TextBlob API
    for tweet in tweet_list:
        tb = TextBlob(tweet)
        sentiment = tb.sentiment
        sentiment_list.append(sentiment)
    
    #clear tweet_list for next search
    for tweet in tweet_list:
        tweet_list.remove(tweet)
    
    #color dictionary
    color_dict = {}
    color_dict['red'] = (255, 0, 0)
    color_dict['blue'] = (0, 0, 255)
    color_dict['yellow'] = (255, 255, 0)
    color_dict['green'] = (0, 255, 0)

    #image array
    width = 300
    height = 300
    arr = numpy.random.rand(width, height, 3)

    #filling array with color values based on sentiment of tweets
    counter=0
    length = int(math.sqrt(TWEET_TOTAL))
    for i in range(length):
        for j in range(length):
            polarity = sentiment_list[counter][0]
            sentiment = sentiment_list[counter][1]
            if polarity==0 and sentiment==0:
                color = (200,200,200) #set to gray
            elif polarity > 0:
                if sentiment >= .5:
                    color = color_dict['yellow']
                else:
                    color = color_dict['green']
            else:
                if sentiment >= .5:
                    color = color_dict['red']
                else:
                    color = color_dict['blue']
            counter+=1
            ri = int(i*(width/length))
            rj = int(j*(height/length))
            for x in range(ri, ri+int(width/length)):
                for y in range(rj, rj+int(height/length)):
                    arr[x][y] = color
                
    #print(arr)
    img = Image.fromarray(arr.astype('uint8')).convert('RGBA')
    img.save('img/'+term+str(TWEET_TOTAL)+'.jpg')
    img.show()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/add', methods=['POST'])
def add():
    tweet_num = request.form['tweet']
    set_tweet_total(int(tweet_num))
    name = request.form['name']
    stream_tweets(name)
    return redirect('/')

if __name__ == "__main__":
    app.run(port=2372)
    
class StdOutListener(StreamListener):
    def __init__(self, api=None):
        super(StdOutListener, self).__init__()
        self.num_tweets = 0

    def on_status(self, status):
        tweet_list.append(status.text)
        self.num_tweets += 1
        if self.num_tweets < TWEET_TOTAL:
            return True
        else:
            return False

    def on_error(self, status):
        print ('Error on status', status)

    def on_limit(self, status):
        print ('Limit threshold exceeded', status)

    def on_timeout(self, status):
        print ('Stream disconnected; continuing...')



