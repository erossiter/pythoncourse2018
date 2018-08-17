#### Class05
#### Meetup API

## Load keys ------------------------------------------------------

#pip install meetup-api
import imp

## first arg is folder name, second arg is navigating to file
meetup = imp.load_source('pythoncourse2018', '../../pythoncourse2018-prep/day05/erinkeys/meetupkeys.py')
api = meetup.client

## methods we can use
## https://meetup-api.readthedocs.io/en/latest/meetup_api.html#api-client-details

## group object
rladies = api.GetGroup({"urlname" : "R-Ladies-St-Louis"})


## check out what info is available
rladies.__dict__.keys()
rladies.members
rladies.state

for k in rladies.__dict__.keys():
	print k
	print rladies.__dict__[k]
	print ""

rladies.category["name"]


## member object
rladies_members = api.GetMembers({"group_urlname" : "R-Ladies-St-Louis"})
rladies_members.__dict__.keys()

## member objects
ppl = rladies_members.__dict__["results"]
len(ppl)
ppl[0].keys()

for k in ppl[0].keys():
	print k
	print ppl[0][k]
	print ""

for p in ppl:
	if p["name"] == "Erin R.":
		print p["id"]


mygroups = api.GetGroups({"member_id" : "235714231"})
mygroups.meta
mygroups.results



## more group searches
stlgroups = api.GetFindGroups({"zip" : "63112"})
len(stlgroups)

for g in stlgroups:
	print g.category["name"]



polgroups = api.GetFindGroups({"zip" : "63112", "text" : "political"})
len(polgroups)

[g.members for g in polgroups]
[g.urlname for g in polgroups]



simgroups = api.GetGroupSimilarGroups({"urlname" : "Great-Conversations"})
len(simgroups)

[g.name for g in simgroups]


