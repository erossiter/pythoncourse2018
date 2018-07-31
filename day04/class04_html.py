#### Class 04
#### Parsing HTML


## Parsing HTML ------------------------------------------------

## pip install beautifulsoup4

from bs4 import BeautifulSoup
import urllib2 
import random
import time
import os

## Open a web page
web_address = 'https://polisci.wustl.edu/faculty/specialization'
web_page = urllib2.urlopen(web_address)

## Parse it
soup = BeautifulSoup(web_page.read())
soup.prettify()

## Find all cases of a certain tag
soup.find_all('a')
soup.find_all('h3')

## Get the script of a certain tag
fields = soup.find_all('h3') ## list of html entries
[i.text for i in fields] ## grab just the text from each one

# Get the attributes
all_a_tags = soup.find_all('a')
all_a_tags[22].attrs ## a dictionary with the attributes
all_a_tags[22].attrs.keys()
all_a_tags[22]['alt']

## Use this info about HTML elements to grab them
soup.find_all('a', {'class' : "person-view-primary-field"})

## There may be tags within tags
sections = soup.find_all('div')
sections[2].a ## FIRST 'a' tag within the 'div' tag
sections[2].find_all('a') ## ALL 'a' tags within the 'div' tag


## Creating a tree of objects
all_fields = soup.find_all('div')
randy = all_fields[50]

randy.find_all("a")

randy.contents ## Gives a list of all children
randy.children ## Creates an iterator for children

for i, child in enumerate(randy.children):
	print "Child %d: %s" % (i,child)

for sib in randy.next_siblings:
	print sib

for sib in randy.previous_siblings:
	print sib


# Other methods to check family:
# parent
# parents
# next_siblings
# previous_siblings
# descendants

# Beautiful Soup documentation
# http://www.crummy.com/software/BeautifulSoup/bs4/doc/



## Function to save a web page ------------------------------------------------

def download_page(address, filename, wait = 5):
	time.sleep(random.uniform(0,wait))
	page = urllib2.urlopen(address)
	page_content = page.read()
	if os.path.exists(filename) == False:
		with open(filename, 'w') as p_html:
			p_html.write(page_content)
	else:
		print "Can't overwrite file" + filename

download_page('https://polisci.wustl.edu/faculty/specialization', "polisci_ppl.html")

## You can also parse a page that is saved on your computer
## Useful to scrape now, parse later.
with open('polisci_ppl.html') as f:
  myfile = f.read()
  
soup = BeautifulSoup(myfile)
soup.prettify()


