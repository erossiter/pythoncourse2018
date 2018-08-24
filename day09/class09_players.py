# install sqlite from sqlite.org
# pip install sqlalchemy
# pip install pysqlite
# Check: http://pythoncentral.io/introductory-tutorial-python-sqlalchemy/
import sqlalchemy

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, and_, or_
from sqlalchemy.orm import relationship, backref, sessionmaker

# - Connect to the local database
# - The return value of create_engine() is an instance of Engine,
#         and it represents the core interface to the database
# - We could use it to talk to databse directly,
# - but we'd rather use Session object to work with ORM
engine = sqlalchemy.create_engine('sqlite:///players.db', echo=True)

# - ORM: object relational mapping
# - no need to write raw SQL!
# - rather, class-like syntax to do three things at once:
#     1. describe database table
#     2. define our own python class object
#     3. "mapper" to map the python object to SQL table
# - All done together using Declarative system
# - In other words, create classes that include directives to describe the actual 
#     database table they will be mapped to
# - Classes mapped using the Declarative system are defined in terms of a Base class
# - Base class maintains a catalog of classes and tables relative to that base
Base = declarative_base() 

# Define some schemas
# One to Many example
# - foreign key on child (player)
# - relationship() then specified by parent (team) to reference many items
class Player(Base):
  __tablename__ = 'players'
  
  ## primary_key is unique, non-nullable identifier for row
  ## Have an ID column because player attributes (name, etc) are not unique
  ## at least 1 per table
  id = Column(Integer, primary_key=True) 
  name = Column(String)
  number = Column(Integer)
  
  ## ForeignKey tells us we have a relationship with another table ("teams") by the ("id") variable
  ## This info constrained to only come from that table
  ## What we are referencing is usually the primary key for that table
  team_id = Column(Integer, ForeignKey("teams.id")) 
  
  def __init__(self, name, number, team=None):
    self.name = name
    self.number = number
    self.team = team
    
  def __repr__(self):
    return "<Player('%s', '%s')>" % (self.name, self.number)


class Team(Base):
  __tablename__ = "teams"
  
  id = Column(Integer, primary_key=True)
  name = Column(String)
  ## - use strings because these things aren't created yet
  ## - relationship() tells us another table wants to reference us
  ## - now notice we use "Player" object synatx and "team" member variable syntax
  ## - Note: this is NOT a column
  ##          but we can call <team obj>.players
  ##          or <player obj>.team
  players = relationship("Player", backref="team")
  
  def __init__(self, name):
    self.name = name
  
  def __repr__(self):
    return "<team('%s')>" % (self.name)
    
# - First time create tables
# - The MetaData is a registry which includes the ability make schema commands
#    to database.
# - Our SQLite database does not actually have a players table present, so we use
#     MetaData to issue CREATE TABLE statements to the database
#     for all tables that don’t yet exist.

Base.metadata.create_all(engine) 

# - SQLAlchemy represent info for specific table with Table object
# So what columns do we have?
Player.__table__  



## Very similar logic to what we've done before!
## one instance each table
p1 = Player(name = "Erin", number = 25)
t1 = Team(name = "WashU")
## add team reference to player 
p1.team = t1
## now a part of team object
t1.players



## Again,...
# - Create a player
# - Just like we do with Python objects
mason = Player("Mason Plumlee", 5)
print str(mason.id)
# - Nothing?
# - Even though we didn’t specify it in the constructor, the id attribute still produces a value
# of None when we access it (as opposed to Python’s usual behavior of raising AttributeError 
# for an undefined attribute).
# - when put in db it will be assigned

# - Create a session to actually store things in the db
# - The ORM’s "way into" to the database is the Session.
# - Session hasn't opened any connections yet
# - not until first used when calling Session()
# - will hold session until we commmit or close
Session = sessionmaker(bind=engine)
session = Session()

# add player
session.add(mason)

# add multple players
session.add_all([Player("Miles Plumlee", 40),
  Player("Seth Curry", 30), Player("Austin Rivers", 0),
  Player("The other Plumlee", 100)])

# see what we've done this session
session.new 

# now make changes to actual db
session.commit()


# Test again... (it keeps the count in the order they entered the database)
print str(mason.id)

# Some querying
# order the results
# you can think of it as... session.query(TABLE).order_by(COLUMN)
for player in session.query(Player).order_by(Player.number):
  print player.number, player.name, player.id
  
# limit the results 
for player in session.query(Player).order_by(Player.number)[1:3]:
  print player.number, player.name

# Some filters
# lots of options: http://docs.sqlalchemy.org/en/latest/orm/tutorial.html#common-filter-operators
for player in session.query(Player).filter(Player.name == "Mason Plumlee").order_by(Player.number):
  print player.number, player.name
  
for player in session.query(Player).filter(Player.name != "Mason Plumlee").order_by(Player.number):
  print player.number, player.name

# or_()
for player in session.query(Player).filter(or_(Player.name == "Mason Plumlee", Player.name == "Miles Plumlee")).order_by(Player.number):
  print player.number, player.name
  
# .like()
## return all the rows with 'name' column contains the partial string "Plumlee"
for player in session.query(Player).filter(Player.name.like("%Plumlee%")).order_by(Player.number):
  print player.number, player.name

# and_()
for player in session.query(Player).filter(and_(Player.name.like("%Plumlee%"), Player.number > 10)).order_by(Player.number):
  print player.number, player.name

# Results are lists
results = session.query(Player).filter(and_(Player.name.like("%Plumlee%"), Player.number > 10)).order_by(Player.number)
results.first()
results[0]
results[1]

# why use .count()?
session.query(Player).filter(and_(Player.name.like("%Plumlee%"), Player.number > 10)).order_by(Player.number).count()

## Now to relations
## Player and Team tables
duke = Team('Duke')

## query all players
players = session.query(Player).all()
mason.team = duke
players[1].team = duke

## see additions in team object
duke.players

## or through mason object
mason.team.players

## Now note the id:
session.commit()
mason.team_id


# Lets load the two things together
# query(TABLE1, TABLE2)
for player, team in session.query(Player, Team).filter(Player.name == "Mason Plumlee").filter(Team.name == "Duke").order_by(Player.number):
  print player.number, player.name, team.name

# or,
# query(TABLE1).join(TABLE2)
for player in session.query(Player).join(Team).filter(Player.name == "Mason Plumlee").filter(Team.name == "Duke").order_by(Player.number):
  print player.number, player.name, player.team.name

# now deletion
# list we queried above
players
session.query(Player).filter(Player.number == 30).count()

# query 1 player
# now we have the representation of him
seth = session.query(Player).filter(Player.number == 30).first()

# now we can delete him
session.delete(seth)

# he's gone!
session.query(Player).filter(Player.number == 30).count()
session.query(Player).filter(Player.name.like("%Seth%")).count()
players
players = session.query(Player).all()
players 




## Updating
other_plumlee = players[3]
other_plumlee.name = "Marshall Plumlee"

# The Session is paying attention!
session.dirty

# commit our changes
session.commit()


# How to convert data to csv
players = session.query(Player).all()
for player in players:
  ## apply skils we've learned already
  print player.name, player.number, player.team

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