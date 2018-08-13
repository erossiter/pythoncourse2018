#### Class05
#### Pollster API

## http://elections.huffingtonpost.com/pollster/api/v2
# pip install pollster

## from example.py from https://github.com/huffpostdata/python-pollster

import datetime
import pollster

api = pollster.Api()

## not sure what a tag is!
tags = api.tags_get() ## list of dictionary-looking objects

## check out the slugs, anyway
for t in tags:
	print(t.slug)

## 2016 president looks good
charts = api.charts_get(tags = '2016-president')
len(charts.items)
## what's in a single chart (aka plot)
charts.items[0]
## navigate through it....
charts.items[0].question.name
## let's check out their plot
charts.items[0].url 


## next() does pagination
question_slug = next(c.question.slug for c in charts.items if c.question.n_polls > 30)

## grab polls with get request that matches our question_slug 
polls = api.polls_get(
  question = question_slug,
  sort = 'created_at'
)

## Grabbing info from these polls
[p.mode for p in polls.items]
[p.poll_questions[0].question.charts for p in polls.items]


## charts is our first object up above
## grab first one
chart_slug = charts.items[0].slug
trendlines = api.charts_slug_pollster_trendlines_tsv_get(chart_slug)
trendlines

## We can rearrange data too
by_date = trendlines.pivot(index='date', columns='label', values='value').sort_index(0, ascending=False)



## Now looking at question-level
questions = api.questions_get(
  cursor=None,                             # String | Special string to index into the Array
  tags='2016-president',                   # String | Comma-separated list of tag slugs (most Questions are not tagged)
  election_date=datetime.date(2016, 11, 8) # Date | Date of an election
)

## and responses (question_slug is from above, as well)
question_slug
responses_clean = api.questions_slug_poll_responses_clean_tsv_get(question_slug)


