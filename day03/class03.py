#### Class 03
#### Excepting handing and tests


## Types of errors ------------------------------------------------

## Syntax errors ## 
if x == 1:
    print "x equals 1"
else
    print "x does not equal 1"

## Wrong indentation.. ipython helps me here.
for i in range(1,5):
  print i

## colors help, too
x = 0
While x < 5:
    x += 1
print x

## brackets and parentheses
print (10*2) + (5*3))



## Runtime errors ##
print a 
print 5/0


## Another way to think about runtime vs syntax errors
def runtime_error():
    print 5/0

def syntax_error():
    If 2 < 4:
        print "hi"


## Semantic errors ##

## I want to print all numbers in this list
l = [10, 20, 30, 40]
for i in range(1,4):
    print l[i]




## Exceptions ------------------------------------------------

## easy as this
raise Exception

def exception_func(x):
    if x == 0:
        raise Exception
    else:
        return 5.0/x

print exception_func(1)
print exception_func(0)

## but you probably won't need to do this....
## use built-ins

def exception_func(x):
    try:
        ans = 5.0/x
    except ZeroDivisionError:
        ans = None
    finally:
        return ans 

print exception_func(1)
print exception_func(0)


## Most basic format
## We don't know what caused the error though!
try:
    "hi" / 12 ## type error
    5/0 ## zero division error
    print var/12 ## name error
except:
    print "caught an exception"


## Add more nuance for things we might expect
def divide_two_things(thing1, thing2):
    try:
        thing1 / thing2
    except TypeError:
        print "Make sure you have two numbers, returning 0."
        out = 0
    except ZeroDivisionError:
        print "Can't divide by 0, returning 0."
        out = 0
    except:
        print "I caught an unexpected error! Returning 0."
        out = 0
    else:
        out = thing1 / thing2
    finally:
        return out

x = divide_two_things("hi", 12)
x = divide_two_things(12, 0)
x = divide_two_things(5, 5)

## Doesn't catch semantic errors, though!
divide_two_things(10,3)

## helpful so our code doesn't break!
## very helpful when scraping
list1 = [10, 9, 8]
list2 = [1, 1, 0]
newlist = [divide_two_things(i,j) for i,j in zip(list1, list2)]



## Another example of when and how to use

## Let's say we don't care about floats... rounding down is cool.
## What type of error would occur?  How to fix?
def print_integer(integer):
    return "Here is my integer: " + str(integer)

print_integer(2)
print_integer('22')
print_integer('banana')



def print_integer(integer):
    try:
        int(integer)
    except ValueError:
        print "Put in a single number."
    else:
        print "Here is my integer: " + str(integer)

print_integer(2)
print_integer('22')
print_integer('banana')



## Note: you likely won't be raising errors as much as catching them
def print_integer(integer):
    if type(integer)==int: 
        return "Here is my integer: " + str(integer)
    else:
        raise TypeError, "Enter an integer!"

print_integer('22')
        


def print_integer(integer):
    try:
        ## if a whole number
        if integer%1==0:
            return "Here is my integer: " + str(integer)
        else:
            return "This has decimals!"
    except:
        raise TypeError, "Enter a number!"

print_integer('22')
print_integer(1.2)        



def print_integer(integer):
    try:
        if integer%1==0:
            print "Here is my integer: " + str(integer)
        else:
            raise Exception
    except TypeError:
        print "Enter a number!"
    except:
        print "Integers can't have decimals!"

                

        
## Create your own exception      
class CustomException(Exception): 
  def __init__(self, value):
    self.value = value
  def __str__(self):
    return self.value

## use
raise CustomException("That's wrong!!")
    

## Our custom exception is the integer cannot be 10, 20, or 30.
## Since this is a ValueError unique to our situation, we need to catch it outselves.
def print_integer(integer):
    bad_numbers = [10, 20, 30]
    try:
        if integer in bad_numbers:
            ## raise it ourselves
            raise CustomException(integer)
        if integer %1==0:
            print "Congratulations! You entered an integer!"
    ## then catch it
    except CustomException as e:
        ## and print our message
        raise ValueError, "Your number cannot be: %d" % e.value
        return None
    except TypeError:
        print "You didn't enter a number."
        return None
    else:
        return integer




## fix this!
mylist = [1, 2, 3, 4.5, "6", "7.8", 8, 9, "done"]
out = [mylist.pop(0)]
for i in mylist:
    out.append(out[-1] + i)



## Break, continue, else ------------------------------------------------

## continue stops current iteration, goes on
for i in range(10):
    if i == 2:
        continue
    print i
else:
    print "Loop is over"

## break stops entire loop
## else is only used if loop is completed.
for i in range(10):
    if i == 2:
        break
    print i
else:
    print "Loop is over"



## check all digits 2-9
for n in range(2, 10):
    ## check all digits < it
    for x in range(2, n):
        if n % x == 0:
            print "%d equals %d * %d" % (n, x, n//x)
        else:
            print "%d is a prime number" % n

## How do we fix this loop?
## We have 2 semantic errors:
## Printing message for non-prime numbers
## Printing it several times!

