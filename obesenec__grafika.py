import tkinter as tk

okno=tk.Tk()
okno.geometry("600x600")

slovo=tk.StringVar()
pismeno=tk.StringVar()
zadane_slovo=""
zadane_pismeno=""
hadaj_slovo=""
pokus=0

def nacitaj_slovo():
    global slovo, pismeno, zadane_pismeno, zadane_slovo, hadaj_slovo
    zadane_slovo=slovo.get()
    hadaj_slovo="-"*len(zadane_slovo)
    hadaj=tk.Label(okno, text=hadaj_slovo,font=("calibre",30, "bold"))
    hadaj.place(relx=0.5, rely=0.2, anchor="center")

def nacitaj_pismeno():
    global pismeno, slovo, zadane_pismeno, zadane_slovo, hadaj_slovo, pokus
    zadane_pismeno=pismeno.get()
    bolo=0

    for i in range(0,len(zadane_slovo)):
        if zadane_slovo[i]==zadane_pismeno:
            hadaj_slovo=hadaj_slovo[:i]+zadane_pismeno+hadaj_slovo[i+1:]
            bolo=1
            
    if bolo==1:
        hadaj=tk.Label(okno, text=hadaj_slovo,font=("calibre",30, "bold"))
        hadaj.place(relx=0.5, rely=0.2, anchor="center")

    else:
        pokus=pokus+1
        if pokus==1:
            platno.create_rectangle( 30, 320, 320, 300, fill='white' )
        if pokus==2:
            platno.create_line( 300, 320, 300, 30, fill='white', width='10' )
        if pokus==3:
            platno.create_line( 300, 30, 100, 30, fill='white', width='10' )
        if pokus==4:
            platno.create_line( 100, 30, 100, 60, fill='yellow', width='5' )
        if pokus==5:
            platno.create_oval( 80, 60, 120, 100, fill="palegoldenrod" )
        if pokus==6:
            platno.create_oval( 90, 100, 110, 160, fill="palegoldenrod", width='5' )
        if pokus==7: 
            platno.create_line( 100, 100, 80, 140, fill='palegoldenrod', width='5' )
        if pokus==8:
            platno.create_line( 100, 100, 120, 140, fill='palegoldenrod', width='5' )
        if pokus==9:
            platno.create_line( 100, 160, 80, 200, fill='palegoldenrod', width='5' )
        if pokus==10:
            platno.create_line( 100, 160, 120, 200, fill='palegoldenrod', width='5' )

    if pokus>10:
        koniec=tk.Label(okno, text="Neuhadol si!",font=("calibre",20, "bold"))
        koniec.place(relx=0.5, rely=0.95, anchor="center")

    if not "-" in hadaj_slovo:
        koniec=tk.Label(okno, text="Uhadol si!",font=("calibre",20, "bold"))
        koniec.place(relx=0.5, rely=0.95, anchor="center")

nadpis_slovo=tk.Label(okno, text="Zadaj slovo:",font=("calibre",10, "bold"))
nadpis_slovo.place(x=100, y=10)

ramcek_slovo=tk.Entry(okno,textvariable=slovo, font=("calibre",10,"bold"), show = '*')
ramcek_slovo.place(x=200, y=10)

tlacitko_slovo=tk.Button(okno,text="Potvrd slovo", command=nacitaj_slovo)
tlacitko_slovo.place(x=360, y=8)

nadpis_pismeno=tk.Label(okno, text="Zadaj pismeno:",font=("calibre",10, "bold"))
nadpis_pismeno.place(x=100, y=50)

ramcek_pismeno=tk.Entry(okno,textvariable=pismeno, font=("calibre",10,"bold"))
ramcek_pismeno.place(x=200, y=50)

tlacitko_pismeno=tk.Button(okno,text="Potvrd pismeno", command=nacitaj_pismeno)
tlacitko_pismeno.place(x=360, y=50)

platno=tk.Canvas(okno, width=350, height=350, bg="black")
platno.place(relx=0.5, rely=0.6, anchor="center")


okno.mainloop()
