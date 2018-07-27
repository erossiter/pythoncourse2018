## Fill in the following methods for the class 'Clock'

class Clock(object):
    def __init__(self, hour, minutes):
        self.minutes = minutes
        self.hour = hour

    @classmethod
    def at(cls, hour, minutes=0):
        return cls(hour, minutes)

    ## Print the time
    def __str__(self):
    
    ## Add time
    ## Don't return anythhing
    def __add__(self,minutes):
    
    ## Subtract time
    ## Don't return anything
    def __sub__(self,minutes):
    
    ## Are two times equal?
    def __eq__(self, other):
    
    ## Are two times not equal?
    def __ne__(self, other):
