def increment(value, pottype):
    if value < 250:
        value += 1
        if pottype == 1:
            #Write to dual pot the new value
        else:
            #Write to singular pot the new value

def decrement(value, pottype):
    if value > 0:
        value -= 1
        if pottype == 1:
            #Write to dual pot the new value
        else:
            #Write to singular pot the new value

def comtosw(dev, value)
    if value == 1:
        #Turn off specified bypass switch (Filter = ON)
    if value == 0:
        #Turn on specified bypass switch (Filter = OFF)
