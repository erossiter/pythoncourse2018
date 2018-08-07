#### Class 02
#### Namespace and classes
#### In class practice

## Namespace practice----------------------------------------------------
type(2)

def print_int(int):
  int = 5
  print 'Here is an integer: %s' %int ## blue means built-in


print_int(1)
print_int('b')

## Check scope by commenting out int = 5 above
def hi():
  int = 2
  print_int(int)

## now coment out int = 2 above
int = 5
hi()


## Review from slides

## Why did this throw an error?  What does the error say?
def random_product(lower, upper):
	random1
	random2
	return random1 * random2

print random_product(0,1)


## How did we fix this?
import random
def random_product(lower, upper):
	random1=uniform(lower, upper)
	random2=uniform(lower, upper)
	return random1 * random2

print random_product(0,1)


## This syntax means
## - we are importing 1 thing: the 'random' module
## - 'random' becomes a global name vs. all contained within it
## - easily and unambiguously access member functions with .
import random
def random_product(lower, upper):
	random1=random.uniform(lower, upper)
	random2=random.uniform(lower, upper)
	return random1 * random2

print random_product(0,1)

## Could also do this to call without modul name
## Not considered best practice because it
## - imports everything
## - "pollutes" namespace
## - unclear which names are present in namespace
from random import *
uniform(-1,1)


## Classes practice----------------------------------------------------
## A class is a grouping of attributes (data/info) and methods (functions)

## basic class syntax is kindof like a function
## convention is to capitalize, no underscores, definitely no dots
class Human(object):
	latin_name = 'homo sapien'

## instances of the class
me = Human()
you = Human()

## stored in memory somewhere
me

## all instances share this attribute
me.latin_name
you.latin_name


## Now require class instantiation to take more info
class Human(object):
	latin_name = 'homo sapien'
  ## __init__ is one of several special built-in functions that Python uses 
  ## 'self' refers to current instance of class
  ## need it as first arg so function can refer to other attributes and methods of the class!
	def __init__(self, age, sex, name):
		self.age = age
		self.sex = sex
		self.name = name


me = Human(age = 25, sex = 'Female', name = "Erin")
print me.name
print me.age

you = Human() ## why doesn't this work?



## Add some function objects
class Human(object):
	latin_name = 'homo sapien'
	def __init__(self, age, sex, name=None):
		self.age = age
		self.sex = sex
		self.name = name

	def speak(self, words):
		return words

	def introduce(self):
		if self.sex=='Female': return self.speak("Hello. I'm Ms. %s" % self.name)
		elif self.sex=='Male': return self.speak("Hello. I'm Mr. %s" % self.name)
		else: return self.speak("Hello. I'm %s" % self.name)

dir(Human)
me = Human(25, 'Female', "Erin")
me.speak('Hello')
me.introduce()


## Add definitions to built-in functions, like print() or summary() in R
class Human(object):
	latin_name = 'homo sapien'
	def __init__(self, age, sex, name=None):
		self.age = age
		self.sex = sex
		self.name = name

	def speak(self, words):
		return words

	def introduce(self):
		if self.sex=='Female': return self.speak("Hello. I'm Ms. %s" % self.name)
		elif self.sex=='Male': return self.speak("Hello. I'm Mr. %s" % self.name)
		else: return self.speak("Hello. I'm %s" % self.name)

  ## for users--nicely printable representation of an object
	def __str__(self):
		return 'Human: %d year-old %s.' % (self.age, self.sex)



me = Human(25, 'Female', "Erin")
print me



## A more complicated example ----------------------------------------------------

# - Add a student's name to the roster for a grade
# - Get a list of all students enrolled in a grade
# - Get a sorted list of all students in all grades.
# 
# Note that all our students only have one name.

class School():
    def __init__(self, school_name): #initialize instance of class School with parameter name
        self.school_name = school_name #user must put name, no default
        self.db = {} #initialize empty dictionary to store kids and grades
        
    def add(self, name, student_grade): #add a kid to a grade in instance of School
        if student_grade in self.db: #need to check if the key for the grade already exists, otherwise assigning it will return error
            self.db[student_grade].append(name) #add kid to the set of kids within the dictionary
        else: self.db[student_grade] = [name] #if the key doesn't exist, create it and have kid start new list 

    def sort(self): #sorts kids alphabetically and returns them in tuples (because they are immutable)
        sorted_students={} #sets up empty dictionary to store sorted tuples
        for key in self.db.keys(): #loop through each key, automatically ordered
            sorted_students[key] = tuple(sorted(self.db[key])) #add dictionary entry with key being the grade and the entry the tuple of kids
        return sorted_students

    def grade(self, check_grade):
        if check_grade not in self.db: return None #if the key doesn't exist, there are no kids in that grade: return None
        return self.db[check_grade] #if None wasn't returned above, return elements within dictionary, or kids in grade

    def __str__(self): #print function will display the school name on one line, and sorted kids on other line
        return "%s\n%s" %(self.school_name, self.sort())


washu = School("Washington University in St. Louis")
washu.add("min hee", 5)
washu.add("ryden", 4)
washu.add("erin", 4)
print washu.db
sorted_students = washu.sort()
print sorted_students
print washu

print washu.grade(4)
print washu.grade(2)

## Can we add a different sort method to sort the students ~within~ the object?
## We'd need to change the __str__ method, too.




## Another example  ----------------------------------------------------

class Parent():
  def __init__(self, sex, firstname, lastname):
    self.sex = sex
    self.firstname = firstname
    self.lastname = lastname
    self.kids = []

  def role(self):
    if self.sex == "Male":
      return "Father"
    else:
      return "Mother"

  def have_child(self, name):
    child = Child(name, self)
    print self.firstname + " is having a child named " + child.name()
    print "They will make a very good " + self.role()
    self.kids.append(child)
    return child

  def list_children(self):
    for kid in self.kids:
      print "I am the " + self.role() + " of " + kid.name()


class Child():
  def __init__(self, firstname, parent):
    self.parent = parent 
    self.lastname = parent.lastname
    self.firstname = firstname

  def set_name(self, new_first_name, new_last_name):
    self.firstname = new_first_name
    self.lastname = new_last_name

  def name(self):
    return "%s %s" % (self.firstname, self.lastname)

  def introduce(self):
    return "Hi I'm " + self.name()

  def siblings(self):
    for kid in self.parent.kids:
      if kid != self:
        print "I have a sibling named " + kid.name()
        


mom = Parent("Female", "Jane", "Smith")
mom.list_children()
jill = mom.have_child("Jill")
jill.set_name("Jillian", "Jones")
print jill.introduce()
print jill == mom.kids[0]
jack = mom.have_child("Jack")
print jack.introduce()
jack.parent.kids[0].parent.list_children()
jack.siblings()


## Inheritance and Polymorphism  ----------------------------------------------------
## Inheritance -- child gets all method of the parent class(es)
## Polymorphism -- child methods can override parent methods of same name


## "parent" or general class
class Animal(object):

  living = "Yes!" ## attribute of all Animal objects

  def __init__(self, name): # Constructor of the class
      self.name = name
      
  def talk(self): # Abstract method, defined by convention only
  	raise NotImplementedError("Subclass must implement abstract method")

  def furry(self): ## function object of all Animals
    return True


## "children" or specific classes
class Cat(Animal):
  def talk(self):
    return self.meow() 
  def meow(self):
    return 'Meow!'

 
class Dog(Animal):
  def talk(self):
    return self.bark()
  def bark(self):
    return 'Woof! Woof!'


class Fish(Animal):  
  def bubbles(self):
    return 'blubblub'
  def furry(self):
    return False



leonard = Cat("Len")
gus = Dog("Gus")
nemo = Fish("nemo")

animals = [leonard, gus, nemo]

## Why did this happen?  How do we fix it?
for animal in animals:
    print animal.name + ': ' + animal.talk()

## What happened here?
for animal in animals:
    print animal.name + ': ' + str(animal.furry())



## Another example (if time) -----------------------------------------------------------------------

class Burger():
    def __init__(self, filling, doneness, size, toppings_ordered, container):
        self.filling = filling
        self.doneness= doneness
        self.size = size
        self.toppings = self.toppings_allowed(toppings_ordered)
        self.containter = container
    
    def toppings_allowed(self, attempted_toppings):
        allowed_toppings = ["cheese", "tomato", "onion", "lettuce", "bacon"]
        toppings=[]
        for topping in attempted_toppings:
            if topping in allowed_toppings:
                toppings.append(topping)
        return toppings
            
    def __str__(self):
        return "I'm a %s %s burger" % (self.doneness,self.filling)
    
    def tastiness(self):
        if "cheese" in self.toppings:
            return "VERY GOOD"
        elif self.doneness == "raw":
            return "yuck!"
        else:
            return "meh"
        
    def cook(self):
        time_for_doneness = 0
        if self.doneness == "raw":
            time_for_doneness = 0
        elif self.doneness == "rare":
            time_for_doneness = 5
        elif self.doneness == "medium":
            time_for_doneness = 6
        elif self.doneness == "well":
            time_for_doneness = 8
        else:
            return "UNKNOWN"

        return self.size * 4 * time_for_doneness
        

class VeggieBurger(Burger):
    def __init__(self, toppings_ordered, container):
      ## when initializing, you're calling burger initialization
      ## but using presets for some arguments
      ## subclass only needs the 2 arguments 
        Burger.__init__(self,"veggie patty", "medium", 0.25, toppings_ordered, container)

    ## burger uses this version of toppings allowed...
    def toppings_allowed(self, attempted_toppings):
        allowed_toppings = ["cheese", "tomato", "onion", "lettuce"]
        toppings=[]
        for topping in attempted_toppings:
            if topping in allowed_toppings:
                toppings.append(topping)
        return toppings

    def cooking_time(self):
        return 6
        

rare_burger=Burger("beef","rare",0.25,["cheese"],"bread")
veggie_burger = VeggieBurger(["tomato","onion","bacon"],"bread")


rare_burger = Burger("beef", "rare", 0.25, ["cheese"], "bread")
print rare_burger.cooking_time()
print rare_burger.tastiness()
print rare_burger


well_done_burger = Burger("turkey", "well done", 0.33, ["ice cream", "bacon"], "bread")
print well_done_burger.cooking_time()
print well_done_burger.tastiness()
print well_done_burger


veggie_burger = VeggieBurger(["tomato", "bacon"], "bread")
print veggie_burger.cooking_time()
print veggie_burger.tastiness()
print veggie_burger


## Another example (if time) -----------------------------------------------------------------------

class Senator():
  def __init__(self, name):
    self.name = name
    self.bills_voted_on = []

  def vote(self, bill, choice):
    #update the bill object--add the senator's name to the the list of yes/no/abstain
    #update the senator object--add this bill to the bills this senator has voted on
    #print an informative message announcing the vote 


class Bill():
  def __init__(self, title):
    self.title = title
    self.votes = {"yes" : [], "no" : [], "abstain" : []}
    self.passed = None

  def result(self):
    ## update and return the "passed" variable to indicate True/False if the bill passed

## should be able to do these things
jane = Senator("Jane")
jack = Senator("Jack")
environment = Bill("Environmental Protection")
jane.vote(environment, "yes")
jack.vote(environment, "no")
environment.result()
print environment.votes
print environment.passed
print jack.bills_voted_on[0].passed





