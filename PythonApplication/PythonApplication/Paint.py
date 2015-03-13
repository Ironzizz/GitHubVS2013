from tkinter import *

canvas_width = 500
canvas_height = 150

def paint( event ):
   x1, y1 = ( event.x - 5 ), ( event.y - 5 )
   x2, y2 = ( event.x + 5 ), ( event.y + 5 )
   w.create_oval( x1, y1, x2, y2, fill = "#000000" )

master = Tk()
master.title( "A simple paint program" )
w = Canvas(master, 
           width=canvas_width, 
           height=canvas_height)
w.pack(expand = YES, fill = BOTH)
w.bind( "<B1-Motion>", paint )

message = Label( master, text = "Drag the mouse to draw" )
message.pack( side = BOTTOM )
    
mainloop()