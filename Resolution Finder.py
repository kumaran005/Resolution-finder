from tkinter import *
from tkinter import filedialog
import os
import tkinter as tk
from PIL import Image,ImageTk

root = Tk()


        
class Load_image:
   
    def show_image(self):
         
            self.filename = filedialog.askopenfilename(initialdir = os.getcwd(),title = "Select Image File",filetypes=(("JPG FILE","*.jpg"),("PNG FILE","*.png"),("ALL FILE","*.*")))
            
            filename = self.filename
            image = Image.open(filename)
            image.thumbnail((350,350))
            image = ImageTk.PhotoImage(image)
            label.configure(image = image)
            label.image = image
        
        
class Find_size(Load_image):
   
    def check_resolution(self):
        
        filename = self.filename
        with open(filename,"rb") as image_file:

    
            image_file.seek(163)

            img = image_file.read(2)

            height = (img[0] << 8) + img[1]
        
            img = image_file.read(2)

            width = (img[0] << 8) + img[1]

            resolution = width,"x",height

        #print(width ,"x",height)
        var = StringVar()    
        label = Label(root, textvariable=var)
        var.set(resolution)
        label.pack(side=tk.TOP,padx=10)
    

frame = Frame(root)
frame.pack(side=BOTTOM, padx=15 , pady= 15)

label = Label(root)
label.pack()


find = Load_image()
find_1 = Find_size()

#Button to browse image
button_1 = Button(frame, text="Browse image", command=find_1.show_image)
button_1.pack(side=tk.LEFT,padx=10)

#Button to find Resolution
button_2 = Button(frame, text = "Resolution" ,command=find_1.check_resolution)
button_2.pack(side=tk.LEFT,padx=10)

#Exit App
button_3 = Button(frame, text="Exit", command= lambda:exit())
button_3.pack(side=tk.LEFT ,padx=10)


root.title("Resolution Finder")
root.geometry("500x350")
root.mainloop()