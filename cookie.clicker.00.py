import tkinter as tk
import threading
import time

Value = 0
clickerAmout = 1
clickerAmout3 = 5

autoclickerAmout = 2
Upgradeclickerprice = 10
Upgradeclickerprice2 = 100
Upgradeclickerprice3 = 30
Upgradeclickerprice4 = 50

Upgradeclicker = False
Upgradeautoclicker = False
temp = True

window = tk.Tk()
window.geometry("900x600")

leftFrame = tk.Frame(window)
leftFrame.pack(side="left", fill="both", expand=True)
rightFrame = tk.Frame(window, bg="PeachPuff3")
rightFrame.pack(side="right", fill="both", expand=True)

photo = tk.PhotoImage(file='susienka.png')

pocet = tk.Label(leftFrame, text="Cookie = 0", font=("Lucida Console", 14), fg="black")
pocet.place(x=50, y=50)

def myThread():
    global Value
    while temp==True:
        time.sleep(1)
        if Upgradeautoclicker==True:
            #window.after(1000, myThread)
            Value = Value + autoclickerAmout
        pocet.configure(text="Cookies = " + str(Value))


def press():
    global Value
    Value = Value + clickerAmout
    pocet.configure(text="Cookies = " + str(Value))
    pocet.place(x=50, y=50)


def cookieclickupgrade():
    global Value, Upgradeclicker, clickerAmout
    if Value >= Upgradeclickerprice:
        Value = Value - Upgradeclickerprice
        Upgradeclicker = True
        pocet.configure(text="Cookies = " + str(Value))
        clickerAmout = clickerAmout + 1

def cookieclickupgrade3():
    global Value, Upgradeclicker, clickerAmout
    if Value >= Upgradeclickerprice3:
        Value = Value - Upgradeclickerprice3
        Upgradeclicker = True
        pocet.configure(text="Cookies = " + str(Value))
        clickerAmout = clickerAmout + 5

def cookieclickupgrade4():
    global Value, Upgradeclicker, clickerAmout
    if Value >= Upgradeclickerprice4:
        Value = Value - Upgradeclickerprice4
        Upgradeclicker = True
        pocet.configure(text="Cookies = " + str(Value))
        clickerAmout = clickerAmout + 10

def cookieclickupgrade2():
    global Value, Upgradeclicker2, autoclickerAmout, Upgradeautoclicker
    if Value >= Upgradeclickerprice2:
        Value = Value - Upgradeclickerprice2
        pocet.configure(text="Cookies = " + str(Value))
        Upgradeautoclicker = True

cookie = tk.Button(window, bg="black", width=123, height=123, command=press, image=photo)
cookie.place(x=140, y=120)

upgrade1 = tk.Button(rightFrame, width=4, height=2, font=("Lucida Console", 12), bg="black", fg="white",
                     text="Purchase upgrade + 1, buy for " + str(Upgradeclickerprice), command=cookieclickupgrade)
upgrade1.pack(side="top", fill="x")

upgrade2 = tk.Button(rightFrame, width=4, height=2, font=("Lucida Console", 12), bg="black", fg="white",
                     text="Purchase upgrade + 5, buy for " + str(Upgradeclickerprice3), command=cookieclickupgrade3)
upgrade2.pack(side="top", fill="x")

upgrade3 = tk.Button(rightFrame, width=4, height=2, font=("Lucida Console", 12), bg="black", fg="white",
                     text="Purchase upgrade + 10, buy for " + str(Upgradeclickerprice4), command=cookieclickupgrade4)
upgrade3.pack(side="top", fill="x")

autoclicker = tk.Button(rightFrame, width=4, height=2, font=("Lucida Console", 12), bg="black", fg="white",
                        text="Purchase upgrade + 2 each second, buy for " + str(Upgradeclickerprice2), command=cookieclickupgrade2)
autoclicker.pack(side="top", fill="x")

counter = threading.Thread(target=myThread)
counter.start()

window.mainloop()
