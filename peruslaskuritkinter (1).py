from tkinter import *

class Tonttu:
    def __init__(self):
        self.rahat = 0
    
class MyWindow:
    def __init__(self, win):
        self.lbl1=Label(win, text='Rahamaara')
        self.lbl2=Label(win, text='Valuuttakurssi')
        self.lbl3=Label(win, text='Result')
        self.t1=Entry(bd=3)
        self.t2=Entry()
        self.t3=Entry()
        self.omatonttu = Tonttu()
        self.btn1 = Button(win, text='Add')
        self.btn2=Button(win, text='Subtract')
        self.lbl1.place(x=100, y=50)
        self.t1.place(x=200, y=50)
        self.lbl2.place(x=80, y=100)
        self.t2.place(x=200, y=100)
        
        self.b1=Button(win, text='Muunna', command=self.add)

        self.b1.place(x=100, y=150)
        self.lbl3.place(x=100, y=200)
        self.t3.place(x=200, y=200)
        
    def add(self):
        self.t3.delete(0, 'end')
        num1=float(self.t1.get())
        num2=float(self.t2.get())
        result=num1 * num2
        self.omatonttu.rahat = result
        self.t3.insert(END, str(result))
        

window=Tk()
mywin=MyWindow(window)
window.title('SSKKY VALUTAKONVERTER')
window.geometry("400x300+10+10")
window.mainloop()