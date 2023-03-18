import tkinter

d=140

#pole
board=[ [0, 0, 0],    
        [0, 0, 0],
        [0, 0, 0] ]

canvas=tkinter.Canvas(height=d*3,width=d*3,bg="yellow")
canvas.pack()

#hraci plan
for n in range(0,3):
    for i in range(0,3):
        A=0+i*d,0+n*d
        B=140+i*d,140+n*d
#        print ("P"+str(n) + str(i))
        canvas.create_rectangle(A,B,outline='black',fill="yellow", tags="P" + str(i) + str(n)) 
        nazov="P" + str(n) + str(i)
        canvas.tag_bind("P"+str(n)+str(i),"<Button-1>",lambda event, meno=nazov: clicked(event, meno, 1))
        canvas.tag_bind("P"+str(n)+str(i),"<Button-3>",lambda event, meno=nazov: clicked(event, meno, -1 ))

##-------------------------------------##

def clicked(event, meno, button):
    #print("You clicked: ",meno, button)
    xx=int(meno[1])
    yy=int(meno[2])
    board[xx][yy]=button
    if button==1:
        a = (x // d) * d + d/2
        b = (y // d) * d + d/2
        #print (x//d, y//d)
        canvas.create_text(a, b, text='O',font=("Arial",32), fill="blue" )

    if button==-1:
        a = (x // d) * d + d/2
        b = (y // d) * d + d/2
        #print (x//d, y//d)
        canvas.create_text(a, b, text='X',font=("Arial",32),fill="red" )

    vyhodnotenie()
    
##-------------------------------------##

def vyhodnotenie():
    if (board[0][0]+board[1][0]+board[2][0] == 3):
        text_vyhra("O")
    elif(board[0][1]+board[1][1]+board[2][1] == 3):
        text_vyhra("O")
    elif(board[0][2]+board[1][2]+board[2][2] == 3):
        text_vyhra("O")

    elif(board[0][0]+board[0][1]+board[0][2] == 3):
        text_vyhra("O")
    elif(board[1][0]+board[1][1]+board[1][2] == 3):
        text_vyhra("O")
    elif(board[2][0]+board[2][1]+board[2][2] == 3):
        text_vyhra("O")

    elif(board[0][0]+board[1][1]+board[2][2] == 3):
        text_vyhra("O")
    elif(board[2][0]+board[1][1]+board[0][2] == 3):
        text_vyhra("O")
    ### ------------------------------------------- ###
    if (board[0][0]+board[1][0]+board[2][0] == -3):
        text_vyhra("X")
    elif(board[0][1]+board[1][1]+board[2][1] == -3):
        text_vyhra("X")
    elif(board[0][2]+board[1][2]+board[2][2] == -3):
        text_vyhra("X")

    elif(board[0][0]+board[0][1]+board[0][2] == -3):
        text_vyhra("X")
    elif(board[1][0]+board[1][1]+board[1][2] == -3):
        text_vyhra("X")
    elif(board[2][0]+board[2][1]+board[2][2] == -3):
        text_vyhra("X")

    elif(board[0][0]+board[1][1]+board[2][2] == -3):
        text_vyhra("X")
    elif(board[2][0]+board[1][1]+board[0][2] == -3):
        text_vyhra("X")

    if ( not any( 0 in sublist for sublist in board) ):
        canvas.create_rectangle(0,0,d*3,d*3, fill="yellow",outline="yellow")
        canvas.create_text(d+d/2, d+d/2, text='Remíza',font=("Arial",16))            

##-------------------------------------##

def text_vyhra(symbol):
    canvas.create_rectangle(0,0,d*3,d*3, fill="yellow",outline="yellow")
    canvas.create_text(d+d/2, d+d/2, text='Vyhral hráč so symbolom '+symbol ,font=("Arial",16))

##-------------------------------------##
def motion(event):
      global x,y
      x = event.x
      y = event.y
      
canvas.bind('<Motion>', motion)
