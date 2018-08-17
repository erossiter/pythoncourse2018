import re

# open text file of 2008 NH primary Obama speech
with open("obama-nh.txt", "r") as f:
	obama = f.readlines()


## TODO: print lines that do not contain 'the' using what we learned
## (although you ~might~ think you could do something like
## [l for l in obama if "the" not in l]
the_patt = re.compile(r"\bThe|the\b")
teststring = ["hello there", "together", "the.", "the  ", "hi there hi" "The", "The school", "hi the cat", "hi the"]
for i in teststring:
	print i
	print the_patt.findall(i)
	print ""
nothe = [l for l in obama if not the_patt.search(l)]
len(nothe)


# TODO: print lines that contain a word of any length starting with s and ending with e
test = "sasdfasfe   asaved"
patt = re.compile(r"\bs[a-z]*e\b")
patt.findall(test)

se_patt = re.compile(r'\b[Ss][a-zA-Z]*[eE]\b')
se = [l for l in obama if se_patt.search(l)]
len(se)


## TODO: Print the date input in the following format
## Month: MM
## Day: DD
## Year: YY
date = raw_input("Please enter a date in the format MM.DD.YY: ")
pattern = re.compile(r"(\d\d)\.(\d\d)\.(\d\d)")
d = pattern.search(date)
print "Month: %s \nDay: %s \nYear: %s" % (d.group(1), d.group(2), d.group(3))





date = raw_input("Please enter a date in the format MM.DD.YY: ")

pattern=re.compile(r'(\d*)\.(\d*)\.(\d*)')
x = pattern.search(date)
print "Month: %r \nDay: %r \nYear: %r"%(x.groups(0)[0],x.groups(0)[1],x.groups(0)[2])




date = raw_input("Please enter a date in the format MM.DD.YY: ")
pattern3=re.compile(r'(\d{2})\.(\d{2})\.(\d{2})')
unit=pattern3.search(date.encode('utf-8'))
print 'Month: ' + unit.group(1) + '\n' + 'Day: ' +unit.group(2) + '\n'+'Year: ' +unit.group(3)
