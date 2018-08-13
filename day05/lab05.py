# TODO: write code to answer the following questions: 
# which embassy is closest to the White House in meters? how far? 
# what is its address? 
# if I wanted to hold a morning meeting there, which cafe would you suggest?
# if I wanted to hold an evening meeting there, which bar would you suggest? 


import imp
imported_items = imp.load_source('FOLDER', 'PATH/TO/KEY/FILE')
gmaps = imported_items.gmaps

whitehouse = '1600 Pennsylvania Avenue, Washington, DC'

embassies = [[38.917228,-77.0522365], 
	[38.9076502, -77.0370427], 
	[38.916944, -77.048739] ]