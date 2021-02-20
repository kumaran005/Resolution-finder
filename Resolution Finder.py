from tkinter import *
from tkinter import filedialog,messagebox,Button
from tkinter.ttk import Combobox
import os
import tkinter as ttk
import tkinter as tk
from PIL import Image,ImageTk
import random

root = Tk()


class Load_image:
   
    def show_image(self):
         
            self.filename = filedialog.askopenfilename(
                initialdir = os.getcwd(),title = "Select Image File",
                filetypes=(("JPG FILE","*.jpg"),("PNG FILE","*.png"),("ALL FILE","*.*")))
            
            filename = self.filename
            image = Image.open(filename)
            image.thumbnail((400,500))
            image = ImageTk.PhotoImage(image)
            label.configure(image = image)
            label.image = image
        
        

class Find_size(Load_image):
   
    def check_resolution(self):
        
        filename = self.filename
        img = Image.open(filename,'r')

        width = img.size[0]

        height = img.size[1]

        resolution =f'{width}x{height}'
        messagebox.showinfo('Resolution',resolution)


class Find_Pixels(Find_size):
    

    def Pixels(self):
    
        window = tk.Tk()
        window.title("Pixel finder")
        window.geometry("300x200")

        filename = self.filename
        ttk.Label(window,text="select X:").grid(column=0,row=5,padx=10,pady=25)
        ttk.Label(window,text="select Y:").grid(column=2,row=5,padx=10,pady=25)
        
       
        self.img = Image.open(filename,'r')
        value = []
        value1 = []
        

        for x in range(self.img.width):
            value.append(x)
        for y in range(self.img.height):
            value1.append(y)    
             

        self.var  = IntVar()
        self.var1  = IntVar()

        choose = Combobox(window,width=5,values=value,textvariable=self.var,state='readonly')
        choose.grid(column=1,row=5)
        choose.current()
        choose1 = Combobox(window,width=5,values=value1,textvariable=self.var1,state='readonly')
        choose1.grid(column=3,row=5)
        choose1.current()
        
        #Button to find a Pixel value     
        Button(window, text="Pixel", command=find_2.onpressed,
        width = 7,bg="#4b7fa4",fg="#fcfcec",font=(os.times,10)).grid(row=10,column=2,pady=5)

        #Close window
        Button(window,text='Close',command=lambda:window.destroy(),
        width = 7,bg="#4b7fa4",fg="#fcfcec",font=(os.times,10)).grid(row=12,column=2,pady=5)

        #Button to find All Pixel value
        Button(window,text = "Find All",command=find_2.findall,
        width = 7,bg="#4b7fa4",fg="#fcfcec",font=(os.times,10)).grid(row=11,column=2,pady=5)
        window.mainloop()
  

    def onpressed(self):
        x = self.var.get()
        y = self.var1.get()

        print(x,y)
        z = 'Pixel value:',self.img.getpixel((x,y))
        messagebox.showinfo('pixel',z)
        print(self.img.getpixel((x,y)))  
     
    def findall(self):
        
        filename = self.filename

        im = Image.open(filename,'r')

        im.load()

         
        name = random.randint(0,50)

        f = open(f'Value_{name}.pdf','a',)

        values=[]
        for i in range (im.width):               
            for j in range(im.height):
                x=f'(X:{i},Y:{j}):{im.getpixel((i,j))}'
                values.append(x)

        f.write(str(values))
        f.close()

        f = open(f"Value_{name}.pdf",'r')
     
        
frame = Frame(root)
frame.pack(side=RIGHT, padx=15 , pady= 15)

label = Label(root)
label.pack()


find = Load_image()
find_1 = Find_size()
find_2 = Find_Pixels()


#Button to browse image
button_1 = Button(frame, text="Browse image", command=find_2.show_image,
width = 10,bg="#4b7fa4",fg="#fcfcec",font=(os.times,10))
button_1.pack(side=tk.TOP,pady=10)

#Button to find Resolution
button_2 = Button(frame, text = "Resolution" ,command=find_2.check_resolution,
width = 10,bg="#4b7fa4",fg="#fcfcec",font=(os.times,10))
button_2.pack(side=tk.TOP,pady=10)

#Button to find pixels
button_4 = Button(frame,text = "Pixels",command=find_2.Pixels,
width = 10,bg="#4b7fa4",fg="#fcfcec",font=(os.times,10))
button_4.pack(side=tk.TOP,pady=10)

#Exit App
button_3 = Button(frame, text="Exit", command= lambda:exit(),
width = 10,bg="#4b7fa4",fg="#fcfcec",font=(os.times,10))
button_3.pack(side=tk.TOP,pady=10)


root.title("Resolution Finder")
root.geometry("500x250")
root.mainloop()
