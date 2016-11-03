#TwitterMotion
 - Final project, COMS 3103 Fall 2016
 - by Justin Bleuel,  jmb2372
 
# Project description
 
This project takes live tweets and converts it into an image that, through its color, represents the overall sentiment on whatever given search.
 
The colors of the image are determined by the polarity of the tweet (aka pleasantness) and its subjectivity (aka energy), these correspond to each of the four quandrants on the [Mood Meter](http://moodmeterapp.com/science/), a tool developed by psychologists to help promote emotional literacy.
 
 <b>Yellow</b> corresponds to positive sentiment and subjective (aka high-energy) tweets.
 <br><b>Green</b> corresponds to positive sentiment and objective tweets.
 <br><b>Red</b> corresponds to negative and subjective tweets.
 <br><b>Blue</b> corresponds to negative and objective tweets.
 
The subjectivity and polarity of the tweets are determined by TextBlob, a Python library for processing textual data and performing common NLP tasks (like sentiment analysis, see Dependencies, below).
 
It's been shown that different moods are better for different tasks: for example, most people are blue while they mourn. Friends consoling those mourning do best when they themselves are green (which is why it's so cool seeing the sentiment on #NationalStressAwarenessDay over 3600 tweets be so overwhelmingly green, [see Graphics section, below])
 
There is rarely a consensus of which emotion a topic will elicit related to tweets (see examples for Clinton and Trump tweets, below), but by applying this program on a macro level (looking at several hundred, even thousand tweets [though this might take 10m+ to run]), we can see whether people are regulating their emotions in a way that is most beneficial to the topic at hand.

 # How to run
 - Make sure all proper dependencies are installed (see Dependencies section, below)
 - Run the code below in the .ipynb
 - Open new tab, direct to localhost:2372
 - Fill in first form with desired search term (I suggest something that likely has a high volume of tweets, like "election" "clinton" "trump" etc.)
 - Fill in the second form with the desired image size (i.e. the number of tweets you'd like to make up an image, this should be a square value [else it'll be rounded down to one])
 - Once submitted wait, created image will then be displayed and saved to director "/img/img_name.jpg" (img naming described above in previous section)
 - The forms are reset and the user can continue creating images on new terms / of different sizes
 - Note Twitter streaming limits (status printed when reaching limit) and note for large streams can take several minutes, I suggest testing on smaller squarenumbers like 49, 64, 81, etc. but really cool seeing the images from larger streams (like 900, 1600, 2500, etc.)
 
 - if you encounter a problem, interuppt the kernal in ipynb, run the code again, and refresh the localhost:2372 page
 
 # Dependencies
 - [Tweepy](http://www.tweepy.org/) , Twitter's API to stream live tweets
 - [TextBlob](http://textblob.readthedocs.io/en/dev/) , Python library for processing textual data / simple API for common NLP tasks (used for sentiment analysis of each tweet)
 - [PIL](http://www.pythonware.com/products/pil/), Python Imaging Library (used to create mood image)
 - [NumPy](http://www.numpy.org/), API for scientific computing (used to manage sentiment array to then create image from it)
 - [Flask](http://flask.pocoo.org/), web framework to run UI / allow for user input
 - [Math](https://docs.python.org/3/library/math.html), perform mathematical functions (i.e. sqrt() for block sizes)
 
 Can install each with: pip install 'dependency_name'
 
 # Graphics
 Example images created (stored in /img folder when run) 
 - Stress (60x60 tweets): 
 <br><img src='img/stress3600.jpg'>
     - NOTE: 11/2 was #NationalStressAwarenessDay on Twitter -- great to see such positivity and objectiveness re: stress on this day! [From a psych point of view, this is the best quadrant of the mood meter to be in for combatting stress :)]
     - Also note: taking a stream of 3600 tweets took approx. 15m to run. Still works fine (and image result looks nicer) but easier to test with smaller square numbers like 25, 49, 64, etc.
 - Clinton (50x50 tweets): <br><img src='img/clinton2500.jpg'>
 - Trump (40x40 tweets): <br><img src='img/trump1600.jpg'>
 - Excited (30x30 tweets): <br><img src='img/excited900.jpg'>
 - Mad (10x10 tweets): <br><img src='img/mad100.jpg'>
 
 # Files included
 jmb2372_project.ipynb -- this file
 <br>/templates -- directory with index.html file (used for Flask page)
 <br>/img -- director with several example #TweetMotion .jpg files as well as location where images stored when program run
