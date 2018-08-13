#### Class 03
#### Reading and writing files


## Reading text files ------------------------------------------------
import sys

## Read all lines as one string
with open('test_readfile.txt') as f:
  the_whole_thing = f.read()
  print the_whole_thing


## Read line by line
with open('test_readfile.txt') as f:
  lines_list = f.readlines()
  for l in lines_list:
    print l

## More efficiently we can loop over the file object
## (i.e. we don't need the variable lines)
with open('test_readfile.txt') as f:   
  for l in f:
    print l
    
    
## We can also manually open and close files,
## now we need to handle exceptions and close
## I never do this
f =  open('test_readfile.txt')
print f.read()
f.close()


## Writing text files ------------------------------------------------

## Writing files is easy,
## open command takes r, w, a, plus some others
with open('test_writefile.txt', 'w') as f:
  ## wipes the file clean and opens it
  f.write("Hi guys.")
  f.write("Does this go on the second line?")
  f.writelines(['a\n', 'b\n', 'c\n'])

with open('test_writefile.txt', 'a') as f:
  ## appends
  f.write("I got appended!")



## Writing csv files ------------------------------------------------
import csv

## Open a file stream and create a CSV writer object
with open('test_writecsv.txt', 'wb') as f:
  my_writer = csv.writer(f)
  for i in range(1, 100):
    my_writer.writerow([i, i-1])


## Now read in the csv
with open('test_writecsv.txt', 'rb') as f:
  my_reader = csv.reader(f)
  mydat = []
  for row in my_reader:
    mydat.append(row)
print mydat

    
## Adding column names
with open('test_csvfields.txt', 'wb') as f:
  my_writer = csv.DictWriter(f, fieldnames = ("A", "B"))
  my_writer.writeheader()
  for i in range(1, 100):
    my_writer.writerow({"B":i, "A":i-1})
    
    
with open('test_csvfields.csv', 'rb') as f:
  my_reader = csv.DictReader(f)
  for row in my_reader:
    print row


# Copyright (c) 2014 Matt Dickenson
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
