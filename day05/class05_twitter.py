#### Class05
#### Twitter API

## Load keys ------------------------------------------------------

#sudo pip install tweepy
import tweepy
import imp

## first arg is folder name, second arg is navigating to file
twitter = imp.load_source('pythoncourse2018', '../../pythoncourse2018-prep/day05/erinkeys/twitterkeys.py')
api = twitter.api


## Twitter API ------------------------------------------------------
## http://docs.tweepy.org/en/v3.5.0/api.html

## See rate limit
limit = api.rate_limit_status()
limit.keys() ## look at dictionary's keys
limit["resources"] ## another dictionary
limit["resources"].keys()
limit["resources"]["tweets"] ## another dictionary!!

for i in limit["resources"]["tweets"].keys():
	print limit["resources"]["tweets"][i] ## another dictionary!


## Create user objects
don = api.get_user('realDonaldTrump')
don ## biiiig object 
type(don)
dir(don)


## Trying some of these methods
print don.id
print don.name
print don.screen_name
print don.location


## Check his tweets
don.status
don.status.text
don.status._json
don.statuses_count

## Check his followers
don.followers_count

## Gives back user objects
don_20 = don.followers() ## only the first 20!
[f.screen_name for f in don_20]

don_200 = api.followers(don.id, count = 200) ## up to 200
[f.screen_name for f in don_200]

## A more round-about way, look up each user
don.followers_ids() #creates a list of user ids - up to 5000

for follower_id in don.followers_ids()[0:100]:
	user = api.get_user(follower_id)
	print user.location

## Normally count = 200 is limit, let's go around that.
don_statuses = []
for p in range(25):
	don_statuses.extend(api.user_timeline('realDonaldTrump', page = p))

# msc:
# x = [1,2]
# x.append([3,4])
# x.extend([3,4])

source = [x.source for x in don_statuses]
[x.text for x in don_statuses if x.source == "Media Studio"]


## Rate limits ------------------------------------------------

## Cursor performs pagination easily for you
histweets = [] ## tweet objects
for status in tweepy.Cursor(api.user_timeline, id = 'realDonaldTrump').items(500):
    histweets.append(status)

## You should definitely hit the rate limit here.....
hisfollowers = []
for item in tweepy.Cursor(api.followers_ids, 'realDonaldTrump').items():
	hisfollowers.append(item)


## API's will not always be this friendly!


