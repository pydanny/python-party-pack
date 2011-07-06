import random

class WeDontHaveThatDrink(Exception): pass

class WeAreOutOfThatDrink(Exception): pass

class EveryoneHasPartyHat(Exception): pass

VALID_DRINKS = ('beer','sangria','wine','lemonade')
VALID_DRINKS_PLURAL = ('beers','sangrias','wines','lemonades')

class Party(object):
    """ A programmatic representation of a party """
    
    def __init__(self, attendees=None, **kwargs):
                
        if attendees is None:
            self.attendees = 1  # The default is just you
        else:
            self.attendees = attendees
            
        self.party_hatted_attendees = 0
        
        for drink in VALID_DRINKS_PLURAL:
            quantity = kwargs.pop(drink, random.randrange(1, 101))
            setattr(self, drink, quantity)
            
    def inventory(self):
        print("Attendees: {0}".format(self.attendees))
        print("Attendees w/hats: {0}".format(self.party_hatted_attendees))
        print("Beers: {0}".format(self.beers))
        print("Sangrias: {0}".format(self.sangrias))
        print("Wines: {0}".format(self.wines))
        print("Lemonades: {0}".format(self.lemonades))                                        
        
    def drink(self, substance):
        """ Drink an available substances specified in VALID_DRINKS constant"""
        
        if substance.endswith('s'):
            substance = substance[:-1]
            
        if substance not in VALID_DRINKS:
            raise WeDontHaveThatDrink('Valid substances to drink are {0}'.format(VALID_DRINKS))
            
        substance += 's'
            
        quantity = getattr(self, substance)
        if quantity == 0:
            raise WeAreOutOfThatDrink()
            
        quantity -= 1
        setattr(self, substance, quantity)
        msg = "Another {0} drunk. We have {1} left!".format(substance, quantity)
        print(msg)
            
    def put_hat_on_attendee(self):
        
        if self.party_hatted_attendees == self.attendees:
            raise EveryoneHasPartyHat()
        self.party_hatted_attendees += 1            
        msg = "{0} of {0} attendees are wearing party hats.".format(self.party_hatted_attendees, self.attendees)
        print(msg)        
            
if __name__ == '__main__':
    p = Party(5)
    p.inventory()
    while True:
        p.drink('wine')
        
    p.put_hat_on_attendee()
    