#This is a basic example showing just how tkiner can be used to display data from csv and png files as well as having buttons that run commands

#Imports
import tkinter as tk
import csv
import pandas as pd
from PIL import Image, ImageTk

#Building the program, making it always on the top.
root=tk.Tk()
root.title("Textbox Input")
root.attributes('-topmost', 1)
root.wm_attributes("-transparent")

#Setting the window size
window_width = 900
window_height = 500

#finding screen info of what ever the program is running on
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

#finding the center of the screen 
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

#This can make it not resizable but rn it's not useful bc the design isnt final
#root.resizable(0,0)


##The background layer doesn't work rn so you can ignore this part.
##########################################
#background Layer
backg=tk.Frame(root)
backg.place(y=0,x=0)

background = Image.open("Image.png")
#background=background.resize((window_width,window_height))
#background=background.resize((1000,1000))
test1=ImageTk.PhotoImage(background)

##########################################

#Main Layer
frame=tk.Frame(root)
frame.place(y=0,x=0)

#Each passport has data associated
passport=0
#^ the certain passport to get the data from

#functions

#Changing the text in lbl to what ever is in inputtxt
def retrieve_input():
    inp = inputtxt.get("1.0","end-1c")
    lbl.config(text="Input Text : "+inp)

#going to the next passport and updating the data
def nextpass():
    global passport
    passport = passport+1
    
    #This goes to the [passport](just a number) row in the csv and it sets it to PassData
    Temp=pd.read_csv("Testing.csv")
    PassData=Temp.iloc[passport]
    #Goes through every data in PassData and creates a label for each one
    for i in range(0,len(Cat)):
        df=tk.Label(frame, text=Cat[i]+" : "+PassData[i]).grid(column=2,row=i)

#going to the prev passport and updating the data
def prevpass():
    global passport
    passport = passport-1
    Temp=pd.read_csv("Testing.csv")
    #same as above
    PassData=Temp.iloc[passport]
    for i in range(0,len(Cat)):
        df=tk.Label(frame, text=Cat[i]+" : "+PassData[i]).grid(column=2,row=i)

#showing how .txt file can be shown in labels
with open("text.txt", "r") as h:
    tk.Label(frame, text="I wrote this in the py and this is a txt file : "+h.read(),bg='SteelBlue1').grid(column=1,row=0)

#reading in a csv
Temp=pd.read_csv("Testing.csv")

#Creating a 1d csv with all the data in a row
PassData=Temp.iloc[passport]

#This is a list of all possible categories in order 
Cat=list(pd.read_csv("Testing.csv", nrows =1))

#Making a column filed with data from the csv
for i in range(0,len(Cat)):
    df=tk.Label(frame, text=Cat[i]+" : "+PassData[i]).grid(column=2,row=i)

#Creating an image
image1 = Image.open("ExamplePassport.png")
image1=image1.resize((350,250))
test=ImageTk.PhotoImage(image1)
PassportImage=tk.Label(frame, image=test).grid(column=1,row=3)

#Creating an textbox
inputtxt=tk.Text(frame, height=5,width=20,bg="#e4f5e8")
inputtxt.grid(column=0,row=0)

#Creating a next passport button and a label above it to say what button it is
Next=tk.Label(frame,text="Next Passport").grid(columnspan=1,row=3)
Buttonnext=tk.Button(frame,height=1,width=15,text="Next Passport", command = nextpass)
Buttonnext.grid(columnspan=1,row=4)

#Creating a prev passport button and a label above it to say what button it is
Prev=tk.Label(frame,text="Previous Passport").grid(columnspan=1,row=5)
Buttonprev=tk.Button(frame,height=1,width=15,text="Previus Passport", command = prevpass)
Buttonprev.grid(columnspan=1,row=6)

#Creating a get text in textbox button and a label above it to say what button it is
InputLabel=tk.Label(frame, text="Get the input").grid(columnspan=1,row=1)
buttonCommit=tk.Button(frame, height=1, width=15, text="get input",
                    command = retrieve_input)
buttonCommit.grid(columnspan=1,row=2)

#creating a label for the retrieve_input function
lbl=tk.Label(frame,text="Input Text : ")
lbl.grid(column=1,row=1)

#Running the app 
#idk what this does tbh but its needed
root.mainloop()

