#Go to https://polisci.wustl.edu/faculty/specialization
#Go to the page for each of the professors.
#Create a .csv file with the following information for each professor:
# 	-Specialization
# 	-Name
# 	-Title
# 	-E-mail
# 	-Web page
	

from bs4 import BeautifulSoup
import urllib2
import re
import csv

with open('lab04_profs_erin.csv', 'wb') as f:
	w = csv.DictWriter(f, fieldnames = ("name", "specialization", "title", "email", "website"))
	w.writeheader()

	web_address='https://polisci.wustl.edu/faculty/specialization'
	web_page = urllib2.urlopen(web_address)

	all_html = BeautifulSoup(web_page.read())
	all_ppl = all_html.find_all("a", {"class" : "person-view-primary-field"})

	for p in all_ppl:
		prof = {} ## empty dictionary to fill in
		prof["name"] = p.get_text()

		## specialization
		prof["specialization"] = p.find_previous("h3").get_text()

		extension = p.attrs["href"]

		if "http" in extension:
			prof["email"] = "NA"
			prof["website"] = "NA"
			prof["title"] = "NA"

		else:
			prof_page = urllib2.urlopen('https://polisci.wustl.edu%s' % extension)
			prof_html = BeautifulSoup(prof_page.read())
			
			## email
			email_div = prof_html.find("div", {"class" : "field field-name-field-person-email field-type-email field-label-inline clearfix"})
			prof["email"] = email_div.a.get_text().strip()
		
			## website
			website_div = prof_html.find("div", {"class" : "field field-name-field-person-website field-type-link-field field-label-inline clearfix"})
			try:
				prof["website"] = website_div.a.attrs["href"].strip()
			except AttributeError:
				prof["website"] = "NA"

			## fancy titles
			title = prof_html.find("div", {"class" : "field field-name-field-person-titles field-type-text field-label-hidden"})
			prof["title"] = title.get_text().strip()

			## write observation to csv
			w.writerow(prof)


