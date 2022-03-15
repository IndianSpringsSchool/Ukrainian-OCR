import tkinter as tk
import csv
import pandas as pd
from PIL import Image, ImageTk

#df=read_csv("Testing.csv",index=False)

root=tk.Tk()
root.title("Textbox Input")
#root.configure(background='systemTransparent')
root.attributes('-topmost', 1)
root.wm_attributes("-transparent")

window_width = 900
window_height = 500

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

#root.resizable(0,0)



#background Layer
backg=tk.Frame(root)
backg.place(y=0,x=0)

background = Image.open("Image.png")
#background=background.resize((window_width,window_height))
#background=background.resize((1000,1000))
test1=ImageTk.PhotoImage(background)



#Main Layer
frame=tk.Frame(root)
#frame.wm_attributes("-transparent")
frame.place(y=0,x=0)

passport=0

def retrieve_input():
    inp = inputtxt.get("1.0","end-1c")
    lbl.config(text="Input Text : "+inp)

def nextpass():
    global passport
    passport = passport+1
    Temp=pd.read_csv("Testing.csv")
    PassData=Temp.iloc[passport]
    for i in range(0,len(Cat)):
        df=tk.Label(frame, text=Cat[i]+" : "+PassData[i]).grid(column=2,row=i)

def prevpass():
    global passport
    passport = passport-1
    Temp=pd.read_csv("Testing.csv")
    PassData=Temp.iloc[passport]
    for i in range(0,len(Cat)):
        df=tk.Label(frame, text=Cat[i]+" : "+PassData[i]).grid(column=2,row=i)


with open("text.txt", "r") as h:
    tk.Label(frame, text="I wrote this in the py and this is a txt file : "+h.read(),bg='SteelBlue1').grid(column=1,row=0)

Temp=pd.read_csv("Testing.csv")
PassData=Temp.iloc[passport]
Cat=list(pd.read_csv("Testing.csv", nrows =1))

for i in range(0,len(Cat)):
    df=tk.Label(frame, text=Cat[i]+" : "+PassData[i]).grid(column=2,row=i)


#df=tk.Label(frame, text=df).grid(column=1,row=2)

image1 = Image.open("ExamplePassport.png")
image1=image1.resize((350,250))
test=ImageTk.PhotoImage(image1)
PassportImage=tk.Label(frame, image=test).grid(column=1,row=3)

inputtxt=tk.Text(frame, height=5,width=20,bg="#e4f5e8")
inputtxt.grid(column=0,row=0)


Next=tk.Label(frame,text="Next Passport").grid(columnspan=1,row=3)
Buttonnext=tk.Button(frame,height=1,width=15,text="Next Passport", command = nextpass)
Buttonnext.grid(columnspan=1,row=4)

Prev=tk.Label(frame,text="Previous Passport").grid(columnspan=1,row=5)
Buttonprev=tk.Button(frame,height=1,width=15,text="Previus Passport", command = prevpass)
Buttonprev.grid(columnspan=1,row=6)

InputLabel=tk.Label(frame, text="Get the input").grid(columnspan=1,row=1)
buttonCommit=tk.Button(frame, height=1, width=15, text="get input",
                    command = retrieve_input)
buttonCommit.grid(columnspan=1,row=2)


lbl=tk.Label(frame,text="Input Text : ")
lbl.grid(column=1,row=1)

root.mainloop()

