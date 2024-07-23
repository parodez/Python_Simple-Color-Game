from tkinter import *
from tkinter import messagebox
import random

class Window(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.master = master
        #Widget Container
        self.init__window()

    def init__window(self):
        #RADIO BUTTON START-----

        #Create container for radio buttons
        radioButtonFrame = Frame(self)

        #Organize radio button container
        radioButtonFrame.grid(row = 0, column = 0, columnspan = 5)

        #Set shared variable for radio buttons
        self.color = StringVar()
        self.color.set(None)

        #Create radio buttons
        optYellow = Radiobutton(radioButtonFrame,
                                text = "YELLOW",
                                variable = self.color,
                                value = "yellow",
                                font = 'Times 10 bold',
                                width = 10,
                                pady = 5,
                                bg = 'yellow',
                                relief = 'sunken')                      
        optGreen = Radiobutton(radioButtonFrame,
                                text = "GREEN",
                                variable = self.color,
                                value = "green",
                                font = 'Times 10 bold',
                                width = 10,
                                pady = 5,
                                bg = 'green',
                                relief = 'sunken')
        optBlue = Radiobutton(radioButtonFrame,
                                text = "BLUE",
                                variable = self.color,
                                value = "blue",
                                font = 'Times 10 bold',
                                width = 10,
                                pady = 5,
                                bg = 'blue',
                                relief = 'sunken')
        optPink = Radiobutton(radioButtonFrame,
                                text = "PINK",
                                variable = self.color,
                                value = "pink",
                                font = 'Times 10 bold',
                                width = 10,
                                pady = 5,
                                bg = 'pink',
                                relief = 'sunken')
        optRed = Radiobutton(radioButtonFrame,
                                text = "RED",
                                variable = self.color,
                                value = "red",
                                font = 'Times 10 bold',
                                width = 10,
                                pady = 5,
                                bg = 'red',
                                relief = 'sunken')
        optOrange = Radiobutton(radioButtonFrame,
                                text = "ORANGE",
                                variable = self.color,
                                value = "orange",
                                font = 'Times 10 bold',
                                width = 10,
                                pady = 5,
                                bg = 'orange',
                                relief = 'sunken')

        #Organize radio buttons
        optYellow.grid(row = 0, column = 0)
        optYellow.grid_propagate(True)
        optGreen.grid(row = 0, column = 1)
        optGreen.grid_propagate(True)
        optBlue.grid(row = 0, column = 2)

        optPink.grid(row = 1, column = 0,sticky = 'n')
        optRed.grid(row = 1, column = 1)
        optOrange.grid(row = 1, column = 2)

        #RADIO BUTTON END-------

        #LABELS START-----

        #Create label container
        labelFrame = Frame(self)

        #Organize label container
        labelFrame.grid(row = 1, column = 0, columnspan = 5)

        #Set up colorbox variable
        self.colorbox = list()

        #Create labels
        self.colorbox.append(Label(labelFrame,
                        width = 20,
                        height = 10,
                        relief = 'sunken'))
        self.colorbox.append(Label(labelFrame,
                        width = 20,
                        height = 10,
                        relief = 'sunken'))
        self.colorbox.append(Label(labelFrame,
                        width = 20,
                        height = 10,
                        relief = 'sunken'))

        #Organize labels
        self.colorbox[0].grid(row = 0, column = 0)
        self.colorbox[1].grid(row = 0, column = 1)
        self.colorbox[2].grid(row = 0, column = 2)

        #LABELS END-------

        #COINS, BET, AND ROLL START-----

        #Create and organize label for coin and bet
        Label(self,text = 'Coin:').grid(row = 2, column = 1,sticky = 'nwse')
        Label(self,text = 'Bet:').grid(row = 2, column = 2,sticky = 'nwse')

        #Set up coin variable
        self.coin = '100'

        #Create label for coin value
        self.coinLabel = Label(self,text = self.coin)

        #Organize coin value label
        self.coinLabel.grid(row = 3, column = 1,sticky = 'nwse')

        #Create spinbox
        self.betAmount = Spinbox(self,from_=1,to=self.coin,width=5)

        #Organize spinbox
        self.betAmount.grid(row = 3, column = 2)

        #Create roll button
        roll = Button(self,
                      text = 'Roll',
                      height = 2,
                      width = 3,
                      command = self.rollColors)

        #Organize roll button
        roll.grid(row = 2, column = 3,rowspan = 2,sticky = 'nwse')

        #COINS, BET, AND ROLL END-------

        #ROLLED COLOR START-----

        #Create label for rolled color
        self.colorValue = Label(self,bg='black')

        #Organize label for rolled color
        self.colorValue.grid(row = 4, column = 0, columnspan = 5,sticky = 'nswe')

        #ROLLED COLOR END-------
        
        #Place widgets in window
        self.pack()

    def rollColors(self, *args):
        #Check if there is a radio button checked
        colorbutton = str(self.color.get())
        #Shows messagebox if no radio button checked
        if colorbutton not in ['yellow','green','blue','pink','red','orange']:
            messagebox.showinfo('No color','Choose color first')
        #Shows messagebox if betamount greater than current coins
        elif int(self.betAmount.get()) > int(self.coin):
            messagebox.showinfo('Insufficient coins', 'Not enough coins')
        else:
            #Generate numbers between 0-5
            self.rolledNumber = list()
            self.rolledNumber.append(int(random.randrange(6)))
            self.rolledNumber.append(random.randrange(6))
            self.rolledNumber.append(random.randrange(6))

            #Creates variable to be put inside colorboxes
            self.rolledColor = ['','','']

            #Puts the designated color depending on the rolled number
            for x in range(0,3):
                if self.rolledNumber[x] == 0:
                    self.colorbox[x].config(bg = 'yellow')
                    self.rolledColor[x] = 'yellow'
                elif self.rolledNumber[x] == 1:
                    self.colorbox[x].config(bg = 'green')
                    self.rolledColor[x] = 'green'
                elif self.rolledNumber[x] == 2:
                    self.colorbox[x].config(bg = 'blue')
                    self.rolledColor[x] = 'blue'
                elif self.rolledNumber[x] == 3:
                    self.colorbox[x].config(bg = 'pink')
                    self.rolledColor[x] = 'pink'
                elif self.rolledNumber[x] == 4:
                    self.colorbox[x].config(bg = 'red')
                    self.rolledColor[x] = 'red'
                elif self.rolledNumber[x] == 5:
                    self.colorbox[x].config(bg = 'orange')
                    self.rolledColor[x] = 'orange'

            #Create variable to count how many color matched
            matchCount = 0

            #Count how many colors matched
            for x in range(0,3):
                if colorbutton == self.rolledColor[x]:
                    matchCount += 1

            #Shows messagebox if user lost
            if matchCount == 0:
                self.coin = str(int(self.coin) - int(self.betAmount.get()))
                messagebox.showinfo('Lost',f'You lost {self.betAmount.get()} coin/s')

            #Shows messagebox if user won
            elif matchCount == 2:
                self.coin = str(int(self.coin) + int(self.betAmount.get()))
                messagebox.showinfo('Won',f'You won {self.betAmount.get()} coin/s')

            #Update coinlabel and change max value of betamount
            self.coinLabel.config(text = self.coin)
            self.betAmount.config(to=self.coin)

            #Shows gameover if coin reaches 0
            if int(self.coin) == 0:
                messagebox.showinfo('End','Game Over')
            

root = Tk()
root.title('Simple Color Game')
w = '500'
h = '500'
#root.geometry(w+'x'+h)
app = Window(root)
root.mainloop()
