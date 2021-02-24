from tkinter import *
from tkinter import filedialog,messagebox,Button
<<<<<<< HEAD
import os
from tkinter.ttk import *
import tkinter as ttk
import tkinter as tk
from PIL import Image,ImageTk,ImageFilter
import random
import PIL
=======
from tkinter.ttk import Combobox
import os
import tkinter as ttk
import tkinter as tk
from PIL import Image,ImageTk
import random
>>>>>>> 3f1a2bac6cf13af5c30b8d174a54fff81634fb7b

root = Tk()
menubar = Menu(root)

<<<<<<< HEAD
=======

>>>>>>> 3f1a2bac6cf13af5c30b8d174a54fff81634fb7b
class Load_image:
   
    def show_image(self):
         
<<<<<<< HEAD
        self.filename = filedialog.askopenfilename(
            initialdir = os.getcwd(),title = "Select Image File",
            filetypes=(("JPG FILE","*.jpg"),("PNG FILE","*.png"),("ALL FILE","*.*")))

        global filename
        filename = self.filename
        image = Image.open(filename)
        image.thumbnail((image.size[0],image.size[1]))
        image = ImageTk.PhotoImage(image)
        label.configure(image = image)
        label.image = image
             
=======
            self.filename = filedialog.askopenfilename(
                initialdir = os.getcwd(),title = "Select Image File",
                filetypes=(("JPG FILE","*.jpg"),("PNG FILE","*.png"),("ALL FILE","*.*")))
            
            filename = self.filename
            image = Image.open(filename)
            image.thumbnail((400,500))
            image = ImageTk.PhotoImage(image)
            label.configure(image = image)
            label.image = image
        
        

>>>>>>> 3f1a2bac6cf13af5c30b8d174a54fff81634fb7b
class Find_size(Load_image):
   
    def check_resolution(self):
        
        filename = self.filename
        img = Image.open(filename,'r')

<<<<<<< HEAD
        

=======
>>>>>>> 3f1a2bac6cf13af5c30b8d174a54fff81634fb7b
        width = img.size[0]

        height = img.size[1]

        resolution =f'{width}x{height}'
        messagebox.showinfo('Resolution',resolution)

<<<<<<< HEAD

class Find_Pixels(Find_size):
    

    def Pixels(self):
    
        root2 = Tk()
        root2.title("Pixel finder")
        root2.geometry("250x150")

        ttk.Label(root2,text="EDGE & PIXEL",font=(os.times,10)).grid(column=5,padx=5,pady=2)
       
        filename = self.filename

        self.img = Image.open(filename,'r')
                
        #Find Edges    
        Button(root2, text="EDGE", command=self.Edge,
        width = 7).grid(row=10,column=5,pady=5)

        #Close window
        Button(root2,text='CLOSE',command=lambda:root2.destroy(),
        width = 7).grid(row=12,column=6,pady=5)

        #Button to find All Pixel value
        Button(root2,text = "PIXELS",command=self.findall,
        width = 7).grid(row=10,column=15,pady=5)

        Button(root2,text="FLIP-H",command=self.flip_H,
        width=7).grid(row=11,column=5,pady=5)

        Button(root2,text="FLIP-V",command=self.flip_V,
        width=7).grid(row=11,column=15,pady=5)

   
    #flip image horizontally
    def flip_H(self):
        filename = self.filename
        flip = Image.open(filename,'r')
        H_flip = flip.transpose(Image.FLIP_LEFT_RIGHT)
        H_flip.show()

    #flip image vertically
    def flip_V(self):
        filename = self.filename
        flip = Image.open(filename,'r')
        V_flip = flip.transpose(Image.FLIP_TOP_BOTTOM)
        V_flip.show()    
     
    #Edges
    def Edge(self):
        filename = self.filename
        
        image = Image.open(filename)
        
        #converting image to greyscale,as edge detection
        #requires input imageto be of mode = Greyscale(L)
        image = image.convert("L")
        image = image.filter(ImageFilter.FIND_EDGES)
        name = random.randint(0,50)
        image.save(f"Edge_{name}.png") 
        image.show()
        

    #finds all the pixel value
    def findall(self):
        
        filename = self.filename

        im = Image.open(filename,'r')

        im.load()

         
        name = random.randint(0,50)

        f = open(f'Value_{name}.txt','a',)

        values=[]
        for i in range (im.width):               
            for j in range(im.height):
                x=f'(X:{i},Y:{j}):{im.getpixel((i,j))}'
                values.append(x)

        f.write(str(values))
        f.close()

        f = open(f"Value_{name}.txt",'r')

#Rotate axis
class Rotate(Find_Pixels):            

    def rotate_90(self):
       
        filename = self.filename
        img_1 = Image.open(filename,'r')
        width = img_1.size[0]

        height = img_1.size[1]
        image = img_1.rotate(90,PIL.Image.NEAREST,expand = 1)
        image.thumbnail((width,height))
        image = ImageTk.PhotoImage(image)
        label.configure(image = image)
        label.image = image
    
    def rotate_180(self):
       
        filename = self.filename
        img_1 = Image.open(filename,'r')
        width = img_1.size[0]

        height = img_1.size[1]
        image = img_1.rotate(180,PIL.Image.NEAREST,expand = 1)
        image.thumbnail((width,height))
        image = ImageTk.PhotoImage(image)
        label.configure(image = image)
        label.image = image
    
    def rotate_270(self):
       
        filename = self.filename
        img_1 = Image.open(filename,'r')
        width = img_1.size[0]

        height = img_1.size[1]
        image = img_1.rotate(270,PIL.Image.NEAREST,expand = 1)
        image.thumbnail((width,height))
        image = ImageTk.PhotoImage(image)
        label.configure(image = image)
        label.image = image
    
    def rotate_360(self):
       
        filename = self.filename
        img_1 = Image.open(filename,'r')
        width = img_1.size[0]

        height = img_1.size[1]
        image = img_1.rotate(360,PIL.Image.NEAREST,expand = 1)
        image.thumbnail((width,height))
        image = ImageTk.PhotoImage(image)
        label.configure(image = image)
        label.image = image    
    

        
frame = Frame(root)
frame.pack(side=RIGHT, padx=15 , pady= 15)

=======

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
>>>>>>> 3f1a2bac6cf13af5c30b8d174a54fff81634fb7b

label = Label(root)
label.pack()


find = Load_image()
find_1 = Find_size()
find_2 = Find_Pixels()
<<<<<<< HEAD
find_3 = Rotate()
=======

>>>>>>> 3f1a2bac6cf13af5c30b8d174a54fff81634fb7b

#,bg="#4b7fa4"fg="#fcfcec",
#Button to browse image
<<<<<<< HEAD
button_1 = Button(frame, text="Browse", command=find_3.show_image,
width = 10)
button_1.pack(side=tk.TOP,pady=10)

#Button to find Resolution
button_2 = Button(frame, text = "Resolution" ,command=find_3.check_resolution,
width = 10,)
button_2.pack(side=tk.TOP,pady=10)

#Button to find pixels
button_4 = Button(frame,text = "Ed-Px",command=find_3.Pixels,
width = 10)
=======
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
>>>>>>> 3f1a2bac6cf13af5c30b8d174a54fff81634fb7b
button_4.pack(side=tk.TOP,pady=10)

#Exit App
button_3 = Button(frame, text="Exit", command= lambda:exit(),
<<<<<<< HEAD
width = 10)
button_3.pack(side=tk.TOP,pady=10)


file = Menu(menubar,tearoff=1)

file.add_command(label="Open",command=find_3.show_image)

file.add_separator()
file.add_command(label="Exit",command=lambda:exit())
menubar.add_cascade(label='File',menu=file)


rotate = Menu(menubar,tearoff=1)
rotate.add_command(label="90 Degree",command=find_3.rotate_90)
rotate.add_command(label="180 Degree",command=find_3.rotate_180)
rotate.add_command(label="270 Degree",command=find_3.rotate_270)
rotate.add_command(label="360 Degree",command=find_3.rotate_360)
menubar.add_cascade(label='Rotate',menu=rotate)

=======
width = 10,bg="#4b7fa4",fg="#fcfcec",font=(os.times,10))
button_3.pack(side=tk.TOP,pady=10)
>>>>>>> 3f1a2bac6cf13af5c30b8d174a54fff81634fb7b

root.config(menu=menubar)

root.title("Resolution Finder")
<<<<<<< HEAD
root.geometry("1200x700")
=======
root.geometry("500x250")
>>>>>>> 3f1a2bac6cf13af5c30b8d174a54fff81634fb7b
root.mainloop()
