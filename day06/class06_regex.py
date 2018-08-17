import re

## I use this to test our my regular expressions
## https://pythex.org/

## Load example text --------------------------------------------------------

## read in example text
## remember, readlines makes a list of each line break in file
with open("obama-nh.txt", "r") as f:
	text = f.readlines()

## How is this file structured?
## How does it impact our 'text' object?
print text[0:3]
print text[0]
print text[1]
print text[2]

## Join into one string
## What could we have done at the outset instead?
alltext = ''.join(text)


## Regular Expressions --------------------------------------------------------
## Help us find patterns in the string.

# re.findall
# re.split
# re.match
# re.search
# re.compile


## Can find a string


re.findall(r"Yes we can", alltext)
re.findall(r"American", alltext)
re.findall(r"\n", alltext)


## Basic special characters

re.findall(r"\d", alltext) ##\d digits
re.findall(r"\D", alltext) ##\D non-digits
re.findall(r"[a]", alltext) ## any chars in []
re.findall(r"[a-d]", alltext) ## any chars in []
re.findall(r"[^a-d]", alltext) ## ^ except
re.findall(r"[a-zA-Z0-9]", alltext)
re.findall(r"\w", alltext) ## \w alphanumeric
re.findall(r"\W", alltext) ## \W non-alphanumeric
re.findall(r"\s", alltext) ## \s whitespace
re.findall(r"\S", alltext) ## \S non-whitespace
re.findall(r".", alltext) ## . any char
re.findall(r"\.", alltext) ## \ is escape


## Now, how much of these things?

re.findall(r"\d", alltext)
re.findall(r"\d*", alltext) ## * 0 or more 
re.findall(r"\d+", alltext) ## + 1 or more
re.findall(r"\d?", alltext) ## ? 0 or 1
re.findall(r"\d{3}", alltext) ## {x} exactly x times
re.findall(r"\d{1,3}", alltext) ## {x, y} from x to y times


## Parentheses give us just that portion

re.findall(r"Yes we can", alltext)
re.findall(r"(Yes) we can", alltext)


## Exercise: How would we grab 01/10 as it appears in text?
x = "Hi 10/10 hello 9/18 asdf 9/9"
re.findall(r"\d{2}/\d{2}", x)



## Explain what's happening:
x = "American's lov\we McDonalds"
re.findall(r"\w", x)
re.findall(r"America[a-z]*", x)
re.findall(r"([A-Z]+\w*)\W*", alltext)



## 'r' means raw string -- read string literally
## used instead of escape character "\" 
"\n"
print "\n"

"\\n"
print "\\n"

r"\n"
print r"\n"



## We can split too

re.split(r'\d', alltext) ## splits at digits, deletes digits

## What is this doing?
re.split(r'\.', alltext) 
re.split(r'(\.)', alltext) ## () splits and keeps separator



## compile the regular expression as an object
## then the regular expression has methods!
keyword = re.compile(r"America[a-z]*")

## search file for keyword in line by line version
for i, line in enumerate(text):
  if keyword.search(line):
  	print i
    print line 


pattern = re.compile(r'\d') #Create a regex object

pattern.findall(alltext)
pattern.split(alltext)


## Can also search across lines in single strings
## with re.MULTILINE

mline = 'bin\nban\ncan'

## ^ is start of the string
## looking for b
pattern = re.compile(r'^b\w*')
pattern.findall(mline)

pattern = re.compile(r'^b\w*', re.MULTILINE)
pattern.findall(mline)

## Now back to the speech as a single string...
## Explain the difference between thes two lines
re.findall(r'^b\w*', alltext, re.MULTILINE)
re.findall(r'^b\w*', alltext)


## Exercise
## Check if a line ends in a period
## How is this working?
re.findall(r'^.*\.$', alltext, re.MULTILINE)



## search, match, and groups
t = '12 twelve'

pattern = re.compile(r'(\d*)\s(\w*)')
tsearch = pattern.search(t)
tsearch.groups() #tuple of all groups
tsearch.group(0) #the complete match
tsearch.group(1) #the first group
tsearch.group(2) #the second group


## Similar to using () alone, but the text
## matched by the group is then accessible
pattern = re.compile(r'(?P<number>\d*)\s(?P<name>\w*)')
tsearch = pattern.search(t)
tsearch.groups()
tsearch.groupdict()



mytext = '12 24'
pattern = re.compile(r'(\d*)\s(\d*)')
pattern.search(mytext).groups()
pattern.search(mytext).group(0)
pattern.search(mytext).group(1)
pattern.search(mytext).group(2)


## match starts search at beginning of string
## like an invisible ^
pattern.match(r"12 24").groups()
pattern.match(r"a12 24").groups()






