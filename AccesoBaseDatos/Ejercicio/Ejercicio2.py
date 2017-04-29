'''
Created on 13 feb. 2017

@author: Adri
'''
'''
from tkinter import *
from tkinter import ttk
ventana = Tk()
ttk.Button(ventana, text="HOLA MUNDO PYTHON").grid()
ventana.mainloop()
'''


'''
from tkinter import * # Interfaz para Tk widgets

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
    def createWidgets(self):
        self.quitButton = Button ( self, text="SALIR", command=self.quit )
        self.quitButton.grid()
            
app = Application() # Instancia la clase Application
app.master.title("Ventana con Botón")
app.mainloop() # Espera a eventos

'''

'''
from tkinter import * # Interfaz para Tk widgets

def funcion():
 v.set("Hola alumnos de DAM")
frame = Frame()
button=Button(frame, text="hola", command=funcion)
button.pack(side=LEFT)
v = StringVar()
text = Entry(frame, textvariable=v )
text.pack(side=LEFT);
frame.pack()
frame.mainloop()
'''
'''
import tkinter as tk
class Application(tk.Frame):
 def __init__(self, master=None):
     tk.Frame.__init__(self, master)
     self.pack()
     self.createWidgets()
 def createWidgets(self):
     self.hola = tk.Button(self)
     self.hola ["text"] = "Hola Mundo Python\n(clic aquí)"
     self.hola ["command"] = self.di_hola
     self.hola.pack(side="top")
     self.salir = tk.Button(self, text="SALIR", fg="red", command=root.destroy)
     self.salir.pack(side="bottom")
 def di_hola(self):
     print("Hola a todos, DAM ALCOBENDAS!")
root = tk.Tk()
app = Application(master=root)
app.mainloop()

'''

'''
from tkinter import *
# Definición de variables y funciones en Python
# Espera 1000 milisegundos para incrementar y mostrar el contador
counter = 0
def counter_label(label):
    counter = 0
    def count():
        global counter
        counter += 1
        label.config(text=str(counter))
        label.after(1000, count)
    count()
root = Tk()
root.title("Aplicación DAM Alcobendas")
logo = PhotoImage(file="giphy.gif")
explanation = "Por el momento, sólo se soportan archivos GIF y PPM/PGM."
# OPCIONES: BOTTOM, LEFT, RIGHT, CENTER, TOP
Label(root, compound = TOP, text = explanation, image = logo).pack(side = "right")
helvetica = Label(root, text = "Helvetica 16", fg = "light green", bg = "dark green", font = "Helvetica 16 bold italic").pack(fill=X, pady=20)
verdana = Label(root,text="Verdana 10 bold", fg = "blue",bg = "yellow", font = "Verdana 10 bold").pack(fill=X, pady = 30)
label = Label(root, fg = "orange", font = "Courier 36 bold")
label.pack()
counter_label(label) # Se llama a la función counter_label
button = Button(root, text='Parar y Salir', width = 10, command=root.destroy)
button.pack(side = "bottom")
root.mainloop()
'''

'''
from tkinter import *
from tkinter import ttk
def calculate(*args):
 try:
     value = float(feet.get())
     meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
 except ValueError:
     pass

root = Tk()
root.title("Conversor Pies - Metros")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
feet = StringVar()
meters = StringVar()
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Calcular", command=calculate).grid(column=3, row=3, sticky=W)
ttk.Label(mainframe, text="pies").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="es equivalente a").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="metros").grid(column=3, row=2, sticky=W)
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
feet_entry.focus()
root.bind('<Return>', calculate)
root.mainloop()

'''

'''
from tkinter import Tk, Frame, Button, BOTH, SUNKEN, colorchooser 
class Example(Frame):
 def __init__(self, parent):
     Frame.__init__(self, parent)
     self.parent = parent
     self.initUI()

 def initUI(self):
     self.parent.title("Color chooser")
     self.pack(fill=BOTH, expand=1)
    
     self.btn = Button(self, text="Choose Color", command=self.onChoose)
     self.btn.place(x=30, y=30)
    
     self.frame = Frame(self, border=1, relief=SUNKEN, width=100, height=100)
     self.frame.place(x=160, y=30)
 def onChoose(self):
     (rgb, hx) = colorchooser.askcolor()
     self.frame.config(bg=hx)
def main():
 root = Tk()
 ex = Example(root)
 root.geometry("300x150+300+300")
 root.mainloop()
if __name__ == '__main__':
 main() 
'''
