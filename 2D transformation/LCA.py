from tkinter import *

#defining region codes
INSIDE = 0  #0000
LEFT = 1    #0001
RIGHT = 2   #0010
BOTTOM = 4  #0100
TOP = 8     #1000
 
#defining clipping area
x_max = int(input("X max: "))
y_max = int(input("Y max: "))
x_min = int(input("X min: "))
y_min = int(input("X min: "))

#defining the point, take 150, 250, 250, 70
x1 = int(input("X1: "))
x11 = x1
y1 = int(input("Y1: "))
y11 = y1
x2 = int(input("X2: "))
x22 = x2
y2 = int(input("Y1: "))
y22 = y2
 
# Function to compute region code for a point(x,y)
def computeCode(x, y):
    code = INSIDE
    if x < x_min:      # to the left of rectangle
        code |= LEFT
    elif x > x_max:    # to the right of rectangle
        code |= RIGHT
    if y < y_min:      # below the rectangle
        code |= BOTTOM
    elif y > y_max:    # above the rectangle
        code |= TOP
 
    return code 

root=Tk()
root.title("Cohen Sutherland line clipping algorithm")
height=700
width=700
canvas=Canvas(root,height=height,width=width)
canvas.pack()

code1 = computeCode(x1, y1)
code2 = computeCode(x2, y2)
accept = False
 
while True:
    if code1 == 0 and code2 == 0:
        accept = True
        break
    
    elif (code1 & code2) != 0:
        break
    else:
        x = 1.0
        y = 1.0
        if code1 != 0:
            code_out = code1
        else:
            code_out = code2
 
        if code_out & TOP:
            x = x1 + (x2 - x1) * \
                            (y_max - y1) / (y2 - y1)
            y = y_max

        elif code_out & BOTTOM:
            x = x1 + (x2 - x1) * \
                            (y_min - y1) / (y2 - y1)
            y = y_min
 
        elif code_out & RIGHT:
            y = y1 + (y2 - y1) * \
                            (x_max - x1) / (x2 - x1)
            x = x_max
 
        elif code_out & LEFT:
            y = y1 + (y2 - y1) * \
                            (x_min - x1) / (x2 - x1)
            x = x_min

        if code_out == code1:
            x1 = x
            y1 = y
            code1 = computeCode(x1,y1)
 
        else:
            x2 = x
            y2 = y
            code2 = computeCode(x2, y2)
 
if accept:
    print ("Line accepted from %.2f,%.2f to %.2f,%.2f" % (x1,y1,x2,y2))
    canvas.create_text(350, 25, text = "Solid line denotes line after clipping")
    canvas.create_text(350, 50, text = "Dashed line denotes part of line that has been clipped")
    canvas.create_rectangle(x_min, y_min, x_max, y_max)
    canvas.create_line(x1, y1, x2, y2)
    canvas.create_line(x11, y11, x22, y22, dash = (4, 2))
 
else:
    print("Line rejected")

root.mainloop()
