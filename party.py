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
            self.attendees = random.randrange(1,100)
        else:
            self.attendees = attendees
            
        self.party_hatted_attendees = 0
        
        for drink in VALID_DRINKS_PLURAL:
            quantity = kwargs.pop(drink, random.randrange(1, 101))
            setattr(self, drink, quantity)
            
        print("Let's get this party started!")
            
    def inventory(self):
        
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
            raise WeDontHaveThatDrink('Valid substances to drink are {0}'.format(VALID_DRINKS))
            
        substance = substance_name + 's'
            
        quantity = getattr(self, substance)
        if quantity == 0:
            raise WeAreOutOfThatDrink()
            
        quantity -= 1
        setattr(self, substance, quantity)
        msg = "Another {0} drunk. We have {1} left!".format(substance_name, quantity)
        print(msg)
            
    def put_hat_on_attendee(self):
        
        if self.party_hatted_attendees == self.attendees:
            raise EveryoneHasPartyHat()
        self.party_hatted_attendees += 1            
        msg = "{0} of {0} attendees are wearing party hats.".format(self.party_hatted_attendees, self.attendees)
        print(msg)        
            
if __name__ == '__main__':
    p = Party(  )
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
        except WeAreOutOfThatDrink:
            print("Party called on account of running out of a drink.")            
            break
    p.inventory()
        
        
    