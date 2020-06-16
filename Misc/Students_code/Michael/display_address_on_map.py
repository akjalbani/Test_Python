# author: Michael Atkinson
# 16/06/2020

import webbrowser
name = input("Enter your full name - ").title()
print (name + ", Let's see where you live...")
print()
print()
print()
print ("After each entry press \"Enter\"")
print()
print()
print()
unit = input ("Enter your unit number, or press enter - ")
house = input ("Enter your house number - ")
streettype = input ("What type of thoroughfare do you reside on? (etc :- Street, Avenue, Road) ? - ").title()
street = input ("What is the name of your " + streettype + "? - ").title()
suburb = input ("What suburb is that in? ").title()
town = input ((name) + " What city is that in? ").title()
sub2 = suburb.replace(" ","+")
address = (unit+"+"+house+"+"+street+"+"+streettype+"+"+sub2)
print (name + ", you live at " + unit +" "+ house +" "+ street +" "+ streettype + ", "+ suburb + ", " + town )
gmap = ("https://www.google.com/maps/place/"+address)
#print ("The weather where you live is" + )
maps = input ("Would you like to see a map of your address? (Yes/No): ").title()

if maps == "Yes":
    webbrowser.open(gmap)
elif maps =="No":

    print ('''Here's the link to your map if you'd like to see it later '''+ (gmap))
