""" what are the Mouse Coordinates? """
## practical example to show tuples
## x,y cordinates stored as tuple, once created can not be changed.
## use python IDLE to test this code.
## 08/06/2020

import tkinter

def mouse_click(event):

    # retrieve XY coords as a tuple
    coords = root.winfo_pointerxy()
    print('coords: {}'.format(coords))
    print('X: {}'.format(coords[0]))
    print('Y: {}'.format(coords[1]))
    
root = tkinter.Tk()
root.bind('<Button>', mouse_click)
root.mainloop()
