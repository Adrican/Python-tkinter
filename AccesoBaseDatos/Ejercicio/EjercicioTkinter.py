'''
Created on 18 feb. 2017

@author: Adri
'''
from tkinter import *
from tkinter import ttk


    
root = Tk()
root.title("Agencia de viajes")
logo = PhotoImage(file="icono.png")
var = IntVar()




Label(root, compound = TOP, image = logo).pack(side = "top")


        

titulo = Label(root, text = "Viajes de senderismo", font = "Times 20 bold italic").pack(fill=X, pady=20)

opciones = Label(root, text = "Opciones")
opciones.place(x=650, y=230)
R1 = Radiobutton(root, text= "Montaña", variable = var, value=1)
R1.place(x=650, y=250)

R2 = Radiobutton(root, text="Montaña Nevada", variable=var, value=2)
R2.place(x=650, y=270)

R3 = Radiobutton(root, text="Sendero", variable=var, value=3)
R3.place(x=650, y=290)

R4 = Radiobutton(root, text="Desierto", variable=var, value=4)
R4.place(x=650, y=310)



        
utensilios = Label(root, text = "Accesorios")
utensilios.place(x=800, y=230)
checkvar1 = IntVar()
checkvar2 = IntVar()
checkvar3 = IntVar()
checkvar4 = IntVar()
checkvar5 = IntVar()
chb1=Checkbutton(root, text="Linterna", variable=checkvar1)
chb2=Checkbutton(root, text="GPS", variable=checkvar2)
chb3=Checkbutton(root, text="Mapa", variable=checkvar3)
chb4=Checkbutton(root, text="Cantimplora", variable=checkvar4)
chb5=Checkbutton(root, text="Crema Solar", variable=checkvar5)
chb1.place(x=800, y=250)
chb2.place(x=800, y=270)
chb3.place(x=800, y=290)
chb4.place(x=800, y=310)
chb5.place(x=800, y=330)


nombre = Label(root, text = "Nombre")
nombre.place(x=650, y=400)
name = StringVar()
campoTexto = Entry(root, textvariable=name)
campoTexto.place(x=650, y=420)
apellidos = Label(root, text = "Apellidos")
apellidos.place(x=650, y=440)
surname = StringVar()
campoTexto = Entry(root, textvariable=surname)
campoTexto.place(x=650, y=460)
direccion = Label(root, text = "Direccion")
direccion.place(x=650, y=480)
address = StringVar()
campoTexto = Entry(root, textvariable=address)
campoTexto.place(x=650, y=500)
telefono = Label(root, text = "Telefono")
telefono.place(x=650, y=520)
phone = StringVar()
campoTexto = Entry(root, textvariable=phone)
campoTexto.place(x=650, y=540)

lb1=Listbox(root, width=40)
lb1.place(x=650, y=620)

           
def mi_funcion():
    if var.get() == 1:
        lb1.insert(1, "Montaña")
    elif var.get() == 2:
        lb1.insert(1, "Montaña Nevada")
    elif var.get() == 3:
        lb1.insert(1, "Sendero")
    elif var.get() == 4:
        lb1.insert(1, "Desierto")
        
    if checkvar1.get() == 1:
        lb1.insert(2, "Linterna")
        checkvar1.set(0)
    if checkvar2.get() == 1:
        lb1.insert(3, "GPS")
        checkvar1.set(0)
    if checkvar3.get() == 1:
        lb1.insert(4, "Mapa")
        checkvar1.set(0)
    if checkvar4.get() == 1:
        lb1.insert(5, "Cantimplora")
        checkvar1.set(0)
    if checkvar5.get() == 1:
        lb1.insert(6, "Crema Solar")
        checkvar1.set(0)
    if name.get() != "":
        lb1.insert(7, name.get())
        name.set("")
    if surname.get() != "":
        lb1.insert(7, surname.get())
        surname.set("")
    if address.get() != "":
        lb1.insert(7, address.get())
        address.set("")
    if phone.get() != "":
        lb1.insert(7, phone.get())
        phone.set("")
                  

   
                
boton=Button(root, text="Introducir datos", command=mi_funcion)
boton.pack()
boton.place(x=730, y=580)



root.geometry("1920x1080")

root.mainloop()