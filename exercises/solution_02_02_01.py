# Given a __distance__ in miles, find its value in __kilometers__.

def mileToKilometers(mile):
    if mile > 100 or mile < 0:
        print("{} is not valid. Please make sure it is between 0 and 100.".format(mile))
        return None
    else:
        kilo = mile*1.6
        print("{} mile(s) is roughly () kilometer(s).".format(mile, kilo))
        return kilo