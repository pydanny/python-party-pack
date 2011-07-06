import random

class DontHaveThatDrink(Exception): 
    """ This is thrown when someone asks for a drink not supplied."""
    pass

class OutOfThatDrink(Exception):
    """ This is thrown when someone asks for a drink whose supply has been exhausted."""    
    pass

class EveryoneHasPartyHat(Exception): 
    """ This is thrown when everyone has managed to get their hat on."""
    pass

VALID_DRINKS = ('beer','sangria','wine','lemonade')
VALID_DRINKS_PLURAL = ('beers','sangrias','wines','lemonades')

class Party(object):
    """ A programmatic representation of a party. Accepts the following parameters:
    
        * attendees (numeric)
        * beers (numeric)
        * sangrias (numeric)
        * wines (numeric)
        * lemonades (numeric)
        
        .. note:: If you don't supply a value for any of the parameters, the Party will act like all parties do and these parameter will show up in random quantities.
        
    """
    
    def __init__(self, attendees=None, **kwargs):
                
        if attendees is None:
            self.attendees = random.randrange(1,100)
        else:
            self.attendees = attendees
            
        self.party_hatted_attendees = 0
        
        for drink in VALID_DRINKS_PLURAL:
            quantity = kwargs.pop(drink, random.randrange(1, 101))
            setattr(self, drink, quantity)
            
        print("Let's get this party started!")
            
    def inventory(self):
        """ Display an inventory of guests and available drinks """
        
        print("What do we got at this party?")
        print("Attendees: {0}".format(self.attendees))
        print("Attendees w/hats: {0}".format(self.party_hatted_attendees))
        print("Beers: {0}".format(self.beers))
        print("Sangrias: {0}".format(self.sangrias))
        print("Wines: {0}".format(self.wines))
        print("Lemonades: {0}".format(self.lemonades))
        print("="*40)
        
    def drink(self, substance_name):
        """ Drink an available substances specified in VALID_DRINKS constant"""
        
        if substance_name.endswith('s'):
            substance_name = substance[:-1]
            
        if substance_name not in VALID_DRINKS:
            raise DontHaveThatDrink('Valid substances to drink are {0}'.format(VALID_DRINKS))
            
        substance = substance_name + 's'
            
        quantity = getattr(self, substance)
        if quantity == 0:
            raise OutOfThatDrink()
            
        quantity -= 1
        setattr(self, substance, quantity)
        msg = "Another {0} drunk. We have {1} left!".format(substance_name, quantity)
        print(msg)
            
    def put_hat_on_attendee(self):
        """ Put a hat on an attendee """
        
        if self.party_hatted_attendees == self.attendees:
            raise EveryoneHasPartyHat()
        self.party_hatted_attendees += 1            
        msg = "{0} of {0} attendees are wearing party hats.".format(self.party_hatted_attendees, self.attendees)
        print(msg)
        
def random_party():
    """ Use this function to hold a completely party. """
    
    p = Party()
    p.inventory()
    while True:
        try:
            p.put_hat_on_attendee()        
        except EveryoneHasPartyHat:
            print("Party called on account of everyone having a hat!")
            break
        try:
            substance = VALID_DRINKS[random.randrange(0, len(VALID_DRINKS))]
            p.drink(substance)
        except OutOfThatDrink:
            print("Party called on account of running out of a drink.")            
            break
    p.inventory()    
            
if __name__ == '__main__':

    random_party()