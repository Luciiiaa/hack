import tkinter as tk
import tkinter.font as font

okno=tk.Tk()
okno.geometry("300x457")

cislo=()
vyraz=""

buttonFont = font.Font(family='Helvetica',weight='bold')

display= tk.Label(okno, height=2, width=20, bg="black", fg="yellow", font=("Lucida Console", 18))
display.pack()

def stlacene(akcia):
    global vyraz, display

    if akcia in ("AC"):
        display.config(text = "")
        vyraz=""

    if akcia in("0") and len(vyraz)>0:
        if vyraz[-1].isdigit():
            vyraz= vyraz + akcia
        
    if akcia in ("1", "2", "3", "4", "5", "6", "7", "8", "9"):
        vyraz= vyraz + akcia

    if akcia in ("+", "-", "*", "/") and len(vyraz)>0:
        if vyraz[-1].isdigit():
            vyraz= vyraz + akcia
            #print("Vyraz: ", vyraz)
        else:
            vyraz = vyraz[:-1] + akcia

    display.config(text = vyraz)

    if akcia=="=":
        display.config(text = eval(vyraz)) 
        vyraz=""
    
#--------------------------------------------#

t_ac=tk.Button(okno,text="AC", width=10, height=2, font=buttonFont, command=lambda x="AC": stlacene(x))
t_ac.place(x=0, y=106)

#------#

t_7=tk.Button(okno,text="7", width=9, height=4, command=lambda x="7": stlacene(x))
t_7.place(x=0, y=160)

t_8=tk.Button(okno,text="8", width=9, height=4, command=lambda x="8": stlacene(x))
t_8.place(x=75, y=160)

t_9=tk.Button(okno,text="9", width=9, height=4, command=lambda x="9": stlacene(x))
t_9.place(x=150, y=160)

t_d=tk.Button(okno,text="÷", width=6, height=3, font=buttonFont, command=lambda x="/": stlacene(x))
t_d.place(x=225, y=160)

#-------------------------#

t_4=tk.Button(okno,text="4", width=9, height=4, command=lambda x="4": stlacene(x))
t_4.place(x=0, y=235)

t_5=tk.Button(okno,text="5", width=9, height=4, command=lambda x="5": stlacene(x))
t_5.place(x=75, y=235)

t_6=tk.Button(okno,text="6", width=9, height=4, command=lambda x="6": stlacene(x))
t_6.place(x=150, y=235)

t_x=tk.Button(okno,text="x", width=6, height=3, font=buttonFont, command=lambda x="*": stlacene(x))
t_x.place(x=225, y=235)

#-------------------------#

t_1=tk.Button(okno,text="1", width=9, height=4, command=lambda x="1": stlacene(x))
t_1.place(x=0, y=310)

t_2=tk.Button(okno,text="2", width=9, height=4, command=lambda x="2": stlacene(x))
t_2.place(x=75, y=310)

t_3=tk.Button(okno,text="3", width=9, height=4, command=lambda x="3": stlacene(x))
t_3.place(x=150, y=310)

t_p=tk.Button(okno,text="+", width=6, height=3, font=buttonFont, command=lambda x="+": stlacene(x))
t_p.place(x=225, y=310)

#-------------------------#

t_0=tk.Button(okno,text="0", width=20, height=4, command=lambda x="0": stlacene(x))
t_0.place(x=0, y=385)

t_min=tk.Button(okno,text="_", width=6, height=3, font=buttonFont, command=lambda x="-": stlacene(x))
t_min.place(x=153, y=385)

t_r=tk.Button(okno,text="=", width=6, height=3, font=buttonFont, command=lambda x="=": stlacene(x))
t_r.place(x=225, y=385)
