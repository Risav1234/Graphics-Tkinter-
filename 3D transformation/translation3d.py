#reflection 3D
# -*- coding: utf-8 -*-
from tkinter import *
from math import sqrt
from math import sin, cos, radians, pi
p=[]
def convert(x,y,z):
	z=z/sqrt(2)
	x=ox+(x-z)
	y=oy-(y-z)
	return x,y

def drawcube(points3d,outline='black'):
	for i in range (len(p3d)):
		points.insert(i,convert(p3d[i][0],p3d[i][1],p3d[i][2]))
		win.create_text(p[i],text=str(i),font="Times 10 bold")
	print (str(p)+"\n")
	win.create_rectangle(p[0],p[2],outline=outline)
	win.create_rectangle(p[4],p[6],outline=outline)
	win.create_line(p[0],p[4],fill=outline)
	win.create_line(p[1],p[5],fill=outline)
	win.create_line(p[2],p[6],fill=outline)
	win.create_line(p[3],p[7],fill=outline)

def translation(x,y,z):
	T = 	[[1, 0, 0, tx],
		 [0, 1, 0, ty],
		 [0, 0, 1, tz],
		 [0, 0, 0, 1]]
	P =     [[x],
		[y],
		[z],
		[1]]

	result= [[0],
	  	 [0],
	   	 [0],
		 [0]]

#Matrix multiplication resultx=Refx.P
	# iterate through rows of Refx
	for i in range(len(T)):
		# iterate through columns of P
		for j in range(len(P[0])):
			# iterate through rows of P
			for k in range(len(P)):
				result[i][j] += T[i][k] * P[k][j]
	return result[0][0],result[1][0],result[2][0]
print("Enter the width,height and depth of cube")
w,h,d=map(int,input().split())
print ("enter the center coordinates xc yc")
xc,yc=map(int,input().split())
zc=0
print("Enter translation factor tx, ty, tz")
tx,ty,tz=map(int,input().split())
master=Tk()
canvas_width=master.winfo_screenwidth()
canvas_height=master.winfo_screenheight()
win=Canvas(master,width=canvas_width,height=canvas_height)
win.pack()
#origin
ox,oy=canvas_width/2,canvas_height/2
#axes
win.create_line(ox,0,ox,oy)
win.create_line(ox,oy,ox*2,oy)
win.create_line(ox,oy,0,oy*2)
#cube points
p3d=[(0,0,0),(w,0,0),(w,h,0),(0,h,0),(0,0,d),(w,0,d),(w,h,d),(0,h,d)]
#displacing cubes by xc,yc
p3dnew=[]
for i in range(len(p3d)):
	points3dnew.insert(i,(p3d[i][0]+xc,p3d[i][1]+yc,p3d[i][2]+zc))
drawcube(p3dnew)
win.create_text(p[1],text="Original cube",font="Times 10 bold")
#calculating points after translation
px=[]
for i in range(len(p)):
	pointsx.insert(i,translation(p3dnew[i][0],p3dnew[i][1],p3dnew[i][2]))
print (px)
drawcube(px,'blue')
win.create_text(p[1],text="cube after translation",font="Times 10 bold")
mainloop()