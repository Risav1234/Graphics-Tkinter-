from tkinter import  *
import math
class Example(Frame):
  
    def __init__(self):
        super().__init__()   
         
        self.initUI()
        
        
    def initUI(self):
        
        start_angle = 45
        start_velocity = 10
        canvas = Canvas(self)
        canvas.configure(background='white')
        for t in range(200):
            self.master.title("Lines")        
            self.pack(fill=BOTH, expand=1)
            iniX = 200
            iniY = 300
            iniVX = start_velocity * math.cos(start_angle) 
            ininVY = -start_velocity * math.sin(start_angle)
            accX = 0
            accY = 0.098
            X = (0.5 * accX * t*t) + (iniVX * t) + iniX
            Y = (0.5 * accY * t * t) + (ininVY * t) + iniY  
    
            canvas.create_oval(X-1,Y-1, X+1,Y+1,outline="blue", fill="blue")
        canvas.create_oval(530,150,550,250,outline="blue", fill="blue")
        canvas.create_oval(535,183,540,217,outline="blue", fill="red")
        canvas.create_line(200,300,500,300)
        canvas.create_rectangle(200,300,550,1000,fill="green")
        canvas.pack(fill=BOTH, expand=1)
        


def main():
    
    root = Tk()
    root["bg"] = "black"
    root.configure(background='black')
    ex = Example()
    root.mainloop()  


if __name__ == '__main__':
    main()  
