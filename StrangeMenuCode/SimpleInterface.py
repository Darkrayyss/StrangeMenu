import DiegoSapp as Ds
import tkinter as tk
import tkinter.font as TkFont
from Functions import console_print

def action():
    Data = Ds.login()
    if Data == False:
        return console_print("Error. Try later")
    else:
        Ds.MenuForo(Data[0])
    return console_print("Close the window to continue")

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # A label
        self.PrimerSaludo = tk.Label(text = "A very long title for a good reception")
        # To underline
        f = TkFont.Font(self.PrimerSaludo, self.PrimerSaludo.cget("font")) 
        f.configure(underline = True) 
        self.PrimerSaludo.configure(font=f) 
        self.PrimerSaludo.pack(side = "top", pady = 40, padx = 20)

        # Button
        self.actionbutton = tk.Button(text = "Do something",
                                  command = self.nothing)
        self.actionbutton.pack()
        

        # Exit
        self.quit = tk.Button(text = "QUIT",
                              command = self.master.destroy,
                              relief = "raised", bd = 10,
                              fg="black", bg = "red",
                              cursor = "hand2", font = ("helv36", 18)
                              ).pack(side = tk.BOTTOM)

    def nothing(self):
        print("You don't have any action yet.")



def SimpleInterface():
    # Creating the window
    fakesapp = tk.Tk()
    # Personalizing the root
    fakesapp.title("FakesAPP")
    fakesapp.iconbitmap("Whatsapp.ico")
    background= tk.PhotoImage(file="background.gif")
    tk.Label(fakesapp, image = background).place(x = 0, y = 0)
    # Creating an app
    myapp = App(fakesapp)
    # configurating the app
    myapp.PrimerSaludo.config(bg = "aquamarine1", relief = "raised", bd = 10,
                              fg = "black", font = ("Times New Roman", 28),
                              text = "Welcome to my first and simple interface !")
    myapp.actionbutton.config(text = "Open and enter to the forum.", command = action,
                              relief = "raised", bd = 10, cursor = "hand2",
                              font = ("helv36", 18), bg = "cyan4")
    myapp.mainloop()
    return